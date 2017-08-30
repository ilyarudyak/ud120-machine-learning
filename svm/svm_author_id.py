"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
from tools.email_preprocess import preprocess
from sklearn import svm
from sklearn.metrics import accuracy_score
import numpy as np


def svm_demo(c=1.0):
    # features_train and features_test are the features for the training
    # and testing datasets, respectively
    # labels_train and labels_test are the corresponding item labels
    features_train, features_test, labels_train, labels_test = preprocess()
    # features_train = features_train[:len(features_train) // 100]
    # labels_train = labels_train[:len(labels_train) // 100]
    #########################################################
    # your code goes here ###
    clf = svm.SVC(kernel='rbf', C=c)
    clf.fit(features_train, labels_train)
    pred = clf.predict(features_test)
    return accuracy_score(labels_test, pred), np.sum(pred)
    #########################################################


if __name__ == '__main__':
    # for c in [10, 100, 1000, 10000]:
    #     print(svm_demo(c))
    print(svm_demo(10000))
