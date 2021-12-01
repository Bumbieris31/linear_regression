#!/usr/bin/env python

from src.linear_regression.linear_regression import LinearRegression
from src.estimate_price.estimate_price import EstimatePrice
from src.utility.plot_data import plot_line, plot_data
import pandas as pd
import matplotlib.pyplot as plt

def normalize_values(data):
    data["km-norm"] = (data['km'] - data['km'].min()) / (data["km"].max() - data["km"].min())
    data["price-norm"] = (data["price"] - data["price"].min()) / (data["price"].max() - data["price"].min())

def plot_line(theta0, theta1, data):
    normalize_values(data)
    plt.scatter(data['km'], data['price'])
    y_val = [(data['km'].min() * theta1) + theta0, (data['km'].max() * theta1) + theta0]
    x_val = [data["km"].min(), data["km"].max()]
    plt.plot(x_val ,y_val, 'r')
    plt.ylabel('Price')
    plt.xlabel('Mileage (km)')
    plt.show()

def main():
    file_name = "data.csv"
    df = pd.read_csv(file_name, sep=',')
    model = LinearRegression()
    model.train_hypothesis(df)
    theta0, theta1 = model.get_hypothesis()
    # plot_line(theta0, theta1, df)
    estimate = EstimatePrice(theta0, theta1)
    estimate.request_mileage()

if __name__ == "__main__":
    main()
    