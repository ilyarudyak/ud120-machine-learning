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


def add_features():
    fraction_from_poi_email = dict_to_list("from_poi_to_this_person", "to_messages")
    fraction_to_poi_email = dict_to_list("from_this_person_to_poi", "from_messages")

    count = 0
    for i in data:
        data[i]["fraction_from_poi_email"] = fraction_from_poi_email[count]
        data[i]["fraction_to_poi_email"] = fraction_to_poi_email[count]
        count += 1


def dict_to_list(key, normalizer):
    new_list = []

    for i in data:
        if data[i][key] == "NaN" or data[i][normalizer] == "NaN":
            new_list.append(0.)
        elif data[i][key] >= 0:
            new_list.append(float(data[i][key]) / float(data[i][normalizer]))
    return new_list


if __name__ == '__main__':
    data = clean_data()
    add_features()
    print(data['METTS MARK'])
