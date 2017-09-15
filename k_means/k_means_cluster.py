#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""

import pickle
import numpy as np
import matplotlib.pyplot as plt
from tools.feature_format import featureFormat, targetFeatureSplit
from sklearn.cluster import KMeans


def draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    # plot each cluster with a different color--add more colors for
    # drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for i, p in enumerate(pred):
        plt.scatter(features[i][0], features[i][1], color=colors[pred[i]])

    # if you like, place red stars over points that are POIs (just for fancies)
    if mark_poi:
        for i, p in enumerate(pred):
            if poi[i]:
                plt.scatter(features[i][0], features[i][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()


def get_data(features_list):
    # load in the dict of dicts containing all the data on each person in the dataset
    data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
    # there's an outlier--remove it!
    data_dict.pop("TOTAL", 0)

    # the input features we want to use
    # can be any key in the person-level dictionary (salary, director_fees, etc.)
    # feature_1 = "salary"
    # feature_2 = "exercised_stock_options"
    # poi = "poi"
    # features_list = [poi, feature_1, feature_2]
    data = featureFormat(data_dict, features_list)
    poi, finance_features = targetFeatureSplit(data)

    return poi, finance_features


def plot_initial_data(features_list):
    # in the "clustering with 3 features" part of the mini-project,
    # you'll want to change this line to
    # for f1, f2, _ in finance_features:
    # (as it's currently written, the line below assumes 2 features)
    poi, finance_features = get_data(features_list)
    for f1, f2 in finance_features:
        plt.scatter(f1, f2)
    plt.show()


def get_clusters(features_list):
    # cluster here; create predictions of the cluster labels
    # for the data and store them to a list called pred
    poi, finance_features = get_data(features_list)
    clf = KMeans(n_clusters=2)
    clf.fit(finance_features)
    return clf.predict(finance_features)


def plot_clusters(features_list):
    # rename the "name" parameter when you change the number of features
    # so that the figure gets saved to a different file
    if len(features_list) == 3:
        feature_1, feature_2 = features_list[1:]
    else:
        feature_1, feature_2, _ = features_list[1:]
    poi, finance_features = get_data(features_list)

    try:
        draw(get_clusters(features_list), finance_features, poi, mark_poi=False, name="clusters.pdf",
             f1_name=feature_1, f2_name=feature_2)
    except NameError:
        print("no predictions object named pred found, no clusters to plot")


def get_feature(feature):
    data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

    options = {person: dic[feature] for person, dic in data_dict.items() if not dic[feature] == 'NaN'}
    return options


if __name__ == '__main__':
    feature_1, feature_2, feature_3, poi = "salary", "exercised_stock_options", "total_payments", "poi"
    features_list = [poi, feature_1, feature_2]
    features_list2 = [poi, feature_1, feature_2, feature_3]
    # plot_clusters(features_list2)
    # feature = 'exercised_stock_options'
    feature = 'salary'
    features = get_feature(feature)
    print(features)
    print(min(features.values()), max(features.values()))
