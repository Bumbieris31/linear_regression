#!/usr/bin/env python

import numpy as np
import pandas as pd
from options.options import parser

class LinearRegression():
    def __init__(self, learning_rate=.3, epochs=500):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.theta0 = 0
        self.theta1 = 0

    @staticmethod
    def validate_data(x, y):
        '''
            x = training data
            y = targets
        '''
        if len(x) is not len(y):
            print("Length of training data and target values doesn't match.")
            raise ValueError

    def cost_funct(predictions, y, m):
        return 1/2*m * (np.sum((predictions - y) ** 2))

    def minmax_scale_values(self, data):
        data["km-norm"] = (data['km'] - data['km'].min()) / (data["km"].max() - data["km"].min())
        data["price-norm"] = (data["price"] - data["price"].min()) / (data["price"].max() - data["price"].min())

    def adjust_theta(self, data):
        self.theta1 = (data["price"].max() - data["price"].min()) * self.theta1 / \
                        (data["km"].max() - data["km"].min())
        self.theta0 = data["price"].min() + ((data["price"].max() - data["price"].min()) * \
                        self.theta0) + self.theta1 * (1 - data["km"].min())

    def train_hypothesis(self, data):
        '''
            Data is dataframe of mileage and price values.
        '''
        m = len(data['km'])
        self.minmax_scale_values(data)
        for i in range(self.epochs):
            predictions = self.theta1 * data['km-norm'] + self.theta0 
            derivative0 = 1/m * np.sum((predictions - data['price-norm']))
            derivative1 = 1/m * np.sum((predictions - data['price-norm']) * data['km-norm'])
            self.theta0 = self.theta0 - (self.learning_rate * derivative0)
            self.theta1 = self.theta1 - (self.learning_rate * derivative1)
        self.adjust_theta(data)

    def get_hypothesis(self):
        return self.theta0, self.theta1 

    def save_hypothesis(self):
        with open("saved_hypothesis.txt", "w+") as f:
            f.write(str(self.theta0) + "\n")
            f.write(str(self.theta1))

def set_args(args):
    file_name = args.data
    lr = .3
    epochs = 500
    if args.learning_rate:
        lr = args.learning_rate
    if args.epochs:
        epochs = args.epochs
    return lr, epochs

if __name__ == "__main__":
    args = parser()
    file_name = args.data
    df = pd.read_csv(file_name, sep=',')
    learning_rate, epochs = set_args(args)
    model = LinearRegression(learning_rate, epochs)
    model.train_hypothesis(df)
    model.save_hypothesis()
    print("Model trained. Prameters saved in 'saved_hypothesis.txt'")
