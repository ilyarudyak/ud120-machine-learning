"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
from tools.feature_format import featureFormat, targetFeatureSplit
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def get_data():

    data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

    # first element is our labels, any added elements are predictor
    # features. Keep this the same for the mini-project, but you'll
    # have a different feature list when you do the final project.
    features_list = ["poi", "salary"]

    data = featureFormat(data_dict, features_list, sort_keys='../tools/python2_lesson13_keys.pkl')
    labels, features = targetFeatureSplit(data)

    # print(labels[:20], features[:20])

    # clf = DecisionTreeClassifier()
    # clf.fit(features, labels)
    # print(accuracy_score(labels, clf.predict(features)))

    return train_test_split(features, labels, test_size=0.3, random_state=42)


def simplest_model():
    features_train, features_test, labels_train, labels_test = get_data()
    clf = DecisionTreeClassifier()
    clf.fit(features_train, labels_train)
    return accuracy_score(labels_test, clf.predict(features_test)), clf


if __name__ == '__main__':
    get_data()


