class estimatePrice():
    def __init__(self, mileage):
        self.mileage = mileage
        self.hypothesis = None

    def set_hypothesis(hypothesis):
        self.hypothesis = hypothesis

    def estimate_price():
        price = self.hypothesis(self.mileage)
        print("Estimated price is: ", price)
        return price

    def request_mileage():
        print("Please write the mileage to estimate the price:")