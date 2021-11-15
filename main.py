from src.linear_regression.linear_regression import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

def normalize_values(data):
    data["km-norm"] = (data['km'] - data['km'].min()) / (data["km"].max() - data["km"].min())
    data["price-norm"] = (data["price"] - data["price"].min()) / (data["price"].max() - data["price"].min())

def plot_line(theta0, theta1, data):
    normalize_values(data)
    plt.scatter(data['km-norm'], data['price-norm'])
    y_val = [(data['km-norm'].min() * theta1) + theta0, (data['km-norm'].max() * theta1) + theta0]
    x_val = [data["km-norm"].min(), data["km-norm"].max()]
    plt.plot(x_val ,y_val, 'r')
    plt.ylabel('Price')
    plt.xlabel('Mileage (km)')
    plt.show()

def main():
    file_name = "data.csv"
    df = pd.read_csv(file_name, sep=',')
    model = LinearRegression()
    model.train_hypothesis(df)
    x, y = model.get_hypothesis()
    print("X and Y", x, y)
    plot_line(x, y, df)

if __name__ == "__main__":
    main()
