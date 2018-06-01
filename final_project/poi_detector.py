import sys
import pickle
import numpy as np
import matplotlib.pyplot as plt

from time import time
from copy import deepcopy

from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.tree import DecisionTreeClassifier

from final_project.fix_records import fixBelfer, fixBhatnagar
from tools.feature_format import featureFormat, targetFeatureSplit


def get_data():
    return pickle.load(open("final_project_dataset.pkl", "rb"))


def clean_data(data):

    cleaned_data = deepcopy(data)

    cleaned_data.pop('THE TRAVEL AGENCY IN THE PARK')
    cleaned_data.pop('TOTAL')
    cleaned_data.pop('LOCKHART EUGENE E')

    fixBelfer(cleaned_data)
    fixBhatnagar(cleaned_data)

    return cleaned_data


def add_features(data):

    added_features_data = deepcopy(data)

    fraction_from_poi_email = dict_to_list("from_poi_to_this_person", "to_messages", added_features_data)
    fraction_to_poi_email = dict_to_list("from_this_person_to_poi", "from_messages", added_features_data)

    count = 0
    for i in added_features_data:
        added_features_data[i]["fraction_from_poi_email"] = fraction_from_poi_email[count]
        added_features_data[i]["fraction_to_poi_email"] = fraction_to_poi_email[count]
        count += 1

    return added_features_data


def dict_to_list(key, normalizer, data):
    new_list = []

    for i in data:
        if data[i][key] == "NaN" or data[i][normalizer] == "NaN":
            new_list.append(0.)
        elif data[i][key] >= 0:
            new_list.append(float(data[i][key]) / float(data[i][normalizer]))
    return new_list


def preprocess_data():
    raw_data = get_data()
    cleaned_data = clean_data(raw_data)
    added_features_data = add_features(cleaned_data)
    return added_features_data


def get_data_with_features(data, features):
    data_with_features = featureFormat(data, features)
    labels, features = targetFeatureSplit(data_with_features)
    features_train, features_test, labels_train, labels_test = \
        train_test_split(features, labels, test_size=0.1, random_state=42)
    return features_train, features_test, labels_train, labels_test


def fit_decision_tree():
    dtc = DecisionTreeClassifier(random_state=42)
    dtc.fit(features_train, labels_train)
    labels_pred = dtc.predict(features_test)
    return accuracy_score(labels_test, labels_pred)


if __name__ == '__main__':
    preprocessed_data = preprocess_data()
    features_list = ["poi", "salary", "bonus", "fraction_from_poi_email", "fraction_to_poi_email",
                     'deferral_payments', 'total_payments', 'loan_advances', 'restricted_stock_deferred',
                     'deferred_income', 'total_stock_value', 'expenses', 'exercised_stock_options',
                     'long_term_incentive', 'shared_receipt_with_poi', 'restricted_stock', 'director_fees']

    features_train, features_test, labels_train, labels_test = \
        get_data_with_features(preprocessed_data, features_list)
    print(fit_decision_tree())
