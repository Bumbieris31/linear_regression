import os

class EstimatePrice():
    def __init__(self):
        self.theta0 = 0
        self.theta1 = 0

    def reset_hypothesis(self, theta0, theta1):
        self.theta0 = theta0
        self.theta1 = theta1

    def estimate_price(self, mileage):
        price = self.theta1 * mileage + self.theta0
        print("Estimated price is: ", price)
        return price

    def validate_input(self, mileage):
        try: 
            mileage_int = int(mileage)
        except ValueError as e:
            print("Input value is not an integer.")
            raise e
        if mileage_int < 0:
            print("Input value is negative")
            raise ValueError
        return mileage_int

    def request_mileage(self):
        mileage = input("Please input the mileage(in km) to estimate the price: ")
        mileage = self.validate_input(mileage)
        self.estimate_price(mileage)

    def check_file(self):
        if os.path.getsize('./saved_hypothesis.txt') == 0:
            print("saved_hypothesis file does not exist. Execute linear_regression first.")
            raise FileNotFoundError

    def load_hypothesis(self):
        try:
            with open("saved_hypothesis.txt", "r") as f:
                self.check_file()
                try:
                    self.theta0 = float(f.next().strip())
                    self.theta1 = float(f.next().strip())
                except ValueError:
                    print("Hypothesis are wrong values")
        except FileNotFoundError:
            print("saved_hypothesis file does not exist. Execute linear_regression first.")

if __name__ == "__main__":
    estimator = EstimatePrice()
    estimator.load_hypothesis()
    estimator.request_mileage()
    