#!/usr/bin/python

import pickle
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
def get_data():
    words_file = "word_data_overfit.pkl"
    authors_file = "email_authors_overfit.pkl"
    word_data = pickle.load(open(words_file, "rb"))
    authors = pickle.load(open(authors_file, "rb"))

    features_train, features_test, labels_train, labels_test = \
        train_test_split(word_data, authors, test_size=0.1, random_state=42)

    vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                                 stop_words='english')
    features_train = vectorizer.fit_transform(features_train)
    features_test = vectorizer.transform(features_test).toarray()

    print(vectorizer.get_feature_names()[33604])

    ### a classic way to overfit is to use a small number
    ### of data points and a large number of features;
    ### train on only 150 events to put ourselves in this regime
    features_train = features_train[:150].toarray()
    labels_train = labels_train[:150]
    return features_train, features_test, labels_train, labels_test


def fit_decision_tree():
    dtc = DecisionTreeClassifier()
    dtc.fit(features_train, labels_train)
    labels_pred = dtc.predict(features_test)
    return accuracy_score(labels_test, labels_pred), dtc.feature_importances_


def get_most_important_features():
    return [(i, f) for i, f in enumerate(feature_importance) if f >= .2]


if __name__ == '__main__':
    np.random.seed(42)
    features_train, features_test, labels_train, labels_test = get_data()
    # accuracy, feature_importance = fit_decision_tree()
    # print(get_most_important_features())
