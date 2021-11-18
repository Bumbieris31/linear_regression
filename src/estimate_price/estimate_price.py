class EstimatePrice():
    def __init__(self, theta0, theta1):
        self.theta0 = theta0
        self.theta1 = theta1

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
