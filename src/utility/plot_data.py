import pandas as pd
import matplotlib.pyplot as plt

def read_data(file_name):
    df = pd.read_csv(file_name, sep=',')
    return df

def plot_data():
    data = read_data("/Users/abumbier/linear_regression/data.csv")
    plt.scatter(data['km'], data['price'])
    plt.ylabel('Price')
    plt.xlabel('Mileage (km)')
    plt.show()

def normalize_values(data):
    data["km-norm"] = (data['km'] - data['km'].min()) / (data["km"].max() - data["km"].min())
    data["price-norm"] = (data["price"] - data["price"].min()) / (data["price"].max() - data["price"].min())

def plot_norm_data():
    data = read_data("/Users/abumbier/linear_regression/data.csv")
    normalize_values(data)
    plt.scatter(data['km-norm'], data['price-norm'])
    plt.ylabel('Price')
    plt.xlabel('Mileage (km)')
    plt.show()

plot_data()
plot_norm_data()