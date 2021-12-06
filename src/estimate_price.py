#!/usr/bin/env python

import os

class EstimatePrice():
    def __init__(self):
        self.theta0 = 0
        self.theta1 = 0

    def return_hypothesis(self):
        return self.theta0, self.theta1

    def estimate_price(self, mileage):
        price = self.theta1 * mileage + self.theta0
        if price < 0:
            price = 0
        print("Estimated price is: ", round(price, 2))
        return price

    def validate_input(self):
        while True:
            mileage = input("Please write a valid mileage(in km) to estimate the price: ")
            try: 
                mileage_int = int(mileage)
            except ValueError:
                print("Input value is not an integer.")
                continue
            if mileage_int < 0:
                print("Input value is negative")
                continue
            return mileage_int

    def request_mileage(self):
        mileage = self.validate_input()
        self.estimate_price(mileage)

    def check_file(self):
        if os.path.getsize('./saved_hypothesis.txt') == 0:
            print("saved_hypothesis file does not exist. Execute linear_regression first.")
            exit()

    def load_hypothesis(self):
        try:
            with open("saved_hypothesis.txt", "r") as f:
                self.check_file()
                try:
                    self.theta0 = float(f.readline().strip())
                    self.theta1 = float(f.readline().strip())
                except ValueError:
                    print("Hypothesis are wrong values")
        except FileNotFoundError:
            print("saved_hypothesis file does not exist. Execute linear_regression first.")
            exit()


if __name__ == "__main__":
    estimator = EstimatePrice()
    estimator.load_hypothesis()
    estimator.request_mileage()
    