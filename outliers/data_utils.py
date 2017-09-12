import numpy as np
import pickle
from sklearn.cross_validation import train_test_split


def get_age_worth_data():
    # load up some practice data with outliers in it
    ages = pickle.load(open("practice_outliers_ages.pkl", "rb"))
    net_worths = pickle.load(open("practice_outliers_net_worths.pkl", "rb"))

    # ages and net_worths need to be reshaped into 2D numpy arrays
    # second argument of reshape command is a tuple of integers: (n_rows, n_columns)
    # by convention, n_rows is the number of data points
    # and n_columns is the number of features
    ages = np.reshape(np.array(ages), (len(ages), 1))
    net_worths = np.reshape(np.array(net_worths), (len(net_worths), 1))

    return train_test_split(
        ages, net_worths, test_size=0.1, random_state=42)