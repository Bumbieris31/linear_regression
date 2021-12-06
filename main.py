#!/usr/bin/env python

from src.linear_regression import LinearRegression, set_args
from src.estimate_price import EstimatePrice
from src.options import parser
import pandas as pd
import matplotlib.pyplot as plt

def normalize_values(data):
    data["km-norm"] = (data['km'] - data['km'].min()) / (data["km"].max() - data["km"].min())
    data["price-norm"] = (data["price"] - data["price"].min()) / (data["price"].max() - data["price"].min())

def plot(theta0, theta1, data, d, h):
    normalize_values(data)
    if d:
        plt.scatter(data['km'], data['price'])
    y_val = [(data['km'].min() * theta1) + theta0, (data['km'].max() * theta1) + theta0]
    x_val = [data["km"].min(), data["km"].max()]
    if h:
        plt.plot(x_val ,y_val, 'r')
    plt.ylabel('Price')
    plt.xlabel('Mileage (km)')
    plt.show()

def main():
    print("Reading data...")
    args = parser()
    file_name = args.data
    df = pd.read_csv(file_name, sep=',')
    print("Training linear model...")
    learning_rate, epochs = set_args(args)
    model = LinearRegression(learning_rate, epochs)
    model.train_hypothesis(df)
    model.save_hypothesis()
    estimate = EstimatePrice()
    estimate.load_hypothesis()
    estimate.request_mileage()
    if args.print_data or args.print_hypothesis:
        theta0, theta1 = estimate.return_hypothesis()
        plot(theta0, theta1, df, args.print_data, args.print_hypothesis)

if __name__ == "__main__":
    main()
