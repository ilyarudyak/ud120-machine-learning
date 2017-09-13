"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

from validation.validate_poi import get_data
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.metrics import precision_score, recall_score


def confusion_matrix():
    features_train, features_test, labels_train, labels_test = get_data()
    clf = DecisionTreeClassifier()
    clf.fit(features_train, labels_train)

    predicted_poi = clf.predict(features_test)
    return precision_score(labels_test, predicted_poi)


def quiz_matrix():
    predictions = np.array([0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1])
    true_labels = np.array([0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0])

    positives = predictions[true_labels.nonzero()]
    print(positives)
    true_positives = np.sum(positives)

    negatives = predictions[np.where(true_labels == 0)[0]]
    print(negatives)
    true_negatives = len(negatives) - np.sum(negatives)

    false_positives = np.sum(negatives)
    false_negatives = len(positives) - np.sum(positives)

    return true_positives, true_negatives, false_positives, false_negatives


if __name__ == '__main__':
    print(quiz_matrix())

