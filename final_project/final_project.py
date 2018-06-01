import sys
import pickle
import numpy as np
import matplotlib.pyplot as plt

from time import time

from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score

from fix_records import fixBelfer, fixBhatnagar


def get_data():
    return pickle.load(open("final_project_dataset.pkl", "rb"))


def clean_data():
    data = get_data()

    data.pop('THE TRAVEL AGENCY IN THE PARK')
    data.pop('TOTAL')
    data.pop('LOCKHART EUGENE E')

    fixBelfer(data)
    fixBhatnagar(data)

    return data


if __name__ == '__main__':
    data = clean_data()
    print(len(data))
