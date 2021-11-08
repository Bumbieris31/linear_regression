from src.linear_regression.linear_regression import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

def main():
    file_name = "data.csv"
    df = pd.read_csv(file_name, sep=',')
    model = LinearRegression()
    model.train_hypothesis(df)
    print("X and Y", model.get_hypothesis)

if __name__ == "__main__":
    main()