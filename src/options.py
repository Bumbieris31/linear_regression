import argparse

def parser():
    parser = argparse.ArgumentParser(
        prog='ft_linear_regression',
        usage='%(prog)s [options] data',
        description="Linear regression"
    )
    parser.add_argument(
        "data", type=argparse.FileType('r'),
        help="Data used for the model training."
    )
    parser.add_argument(
        "-lr", "--learning-rate", type=float,
        help="Learning rate of the gradient descent"
    )
    parser.add_argument(
        "-e", "--epochs", type=int,
        help="Amount of epochs used for training"
    )
    args = parser.parse_args()
    return args
