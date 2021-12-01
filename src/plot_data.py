import pandas as pd
import matplotlib.pyplot as plt

def read_data(file_name):
    df = pd.read_csv(file_name, sep=',')
    return df

def plot_data(data):
    plt.scatter(data['km'], data['price'])
    plt.ylabel('Price')
    plt.xlabel('Mileage (km)')
    plt.show()

def plot_line(theta0, theta1, data):
    normalize_values(data)
    plt.scatter(data['km'], data['price'])
    y_val = [(data['km'].min() * theta1) + theta0, (data['km'].max() * theta1) + theta0]
    x_val = [data["km"].min(), data["km"].max()]
    plt.plot(x_val ,y_val, 'r')
    plt.ylabel('Price')
    plt.xlabel('Mileage (km)')
    plt.show()