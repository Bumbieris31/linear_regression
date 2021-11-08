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


plot_data()