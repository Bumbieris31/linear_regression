from ..utility.exception import InputError
import pandas as pd
import numpy as np

class LinearRegression():
    def __init__(self, learning_rate=.003, iterations=10000):
        self.learning_rate = learning_rate
        self.num_iterations = iterations
        self.theta0 = 0
        self.theta1 = 0

    @staticmethod
    def validate_data(x, y):
        '''
            x = training data
            y = targets
        '''
        if len(x) is not len(y):
            raise InputError(len(x) != len(y), "Length of training data and target values doesn't match.")

    # def cost_funct(predictions, y, m):
    #     return 1/2*m * (np.sum((predictions - y) ** 2))

    def normalize_values(self, data):
        data["km-norm"] = (data['km'] - data['km'].min()) / (data["km"].max() - data["km"].min())
        data["price-norm"] = (data["price"] - data["price"].min()) / (data["price"].max() - data["price"].min())


    def train_hypothesis(self, data):
        '''
            Data is dataframe of mileage and price values.
        '''
        m = len(data['km'])
        print("m is :", m)
        self.normalize_values(data)
        for i in range(self.num_iterations):
            predictions = self.theta1 * data['km-norm'] + self.theta0 
            # print(f"Cycle: {i}\nTheta0 and theta1 :{self.theta0} {self.theta1}")
            # print("Km\n", data['km'])
            # print("ADdded\n", -2 * np.sum(data['km'] * (data['price'] - predictions)) / m)
            derivative0 = 1/m * np.sum((predictions - data['price-norm']))
            derivative1 = 1/m * np.sum((predictions - data['price-norm']) * data['km-norm'])
            # print("difference is:\n", predictions - data['price-norm'])
            # print("derivative1 is:\n", 1/m * np.sum((predictions - data['price-norm'])))
            # print("derivative2 is:\n", 1/m * np.sum((predictions - data['price-norm']) * data['km-norm']))
            self.theta0 = self.theta0 - (self.learning_rate * derivative0)
            self.theta1 = self.theta1 - (self.learning_rate * derivative1)
        print(f"Cycle: {i}\nTheta0 and theta1 :{self.theta0} {self.theta1}")

    def get_hypothesis(self):
        return self.theta0, self.theta1
