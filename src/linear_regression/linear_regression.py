from ..utility.exception import InputError
import pandas as pd
import numpy as np

class LinearRegression():
    def __init__(self, learning_rate=.003, iterations=1000):
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

    # def read_data(file_name):
    #     df = pd.read_csv(file_name, sep=',')
    #     return df

    def train_hypothesis(self, data):
        '''
            Data is dataframe of mileage and price values.
        '''
        m = len(data['km'])
        # self.data = read_data(data)
        for i in range(self.num_iterations):
            predictions = self.theta1 * data['km'] + self.theta0 
            derivative0 = (-2/m) * sum(data['km'] * (data['price'] - predictions))
            derivative1 = (-2/m) * sum(data['price'] - predictions)
            self.theta0 = self.theta0 - self.learning_rate * derivative0
            self.theta1 = self.theta1 - self.learning_rate * derivative1

    def get_hypothesis(self):
        return self.theta0, self.theta1