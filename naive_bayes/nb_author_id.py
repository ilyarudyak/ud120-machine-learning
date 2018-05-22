"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""

from time import time
from tools.email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


def classify():
    # features_train and features_test are the features for the training
    # and testing datasets, respectively
    # labels_train and labels_test are the corresponding item labels
    features_train, features_test, labels_train, labels_test = preprocess()

    #########################################################
    # your code goes here #
    clf = GaussianNB()

    tic = time()
    clf.fit(features_train, labels_train)
    toc = time()
    fit_time = toc - tic

    tic = time()
    pred = clf.predict(features_test)
    toc = time()
    pred_time = toc - tic

    return accuracy_score(labels_test, pred), fit_time, pred_time
    #########################################################


if __name__ == '__main__':
    print(classify())
