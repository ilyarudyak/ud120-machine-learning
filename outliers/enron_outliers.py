#!/usr/bin/python

import pickle
import matplotlib.pyplot as plt
from tools.feature_format import featureFormat, targetFeatureSplit
import numpy as np


def get_data():
    # read in data dictionary, convert to numpy array
    data_dict = pickle.load(open('final_project_dataset.pkl','rb'))
    del data_dict['TOTAL']
    features = ['salary', 'bonus']
    return featureFormat(data_dict, features)


def plot_data(salary_data):
    salary, bonus = salary_data[:, 0], salary_data[:, 1]
    plt.scatter(salary, bonus)
    plt.xlabel('salary')
    plt.ylabel('bonus')
    plt.show()


# your code below
if __name__ == '__main__':
    salary_data = get_data()
    plot_data(salary_data)


