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


def svm_demo(kernel='linear', C=1.0):
    # features_train and features_test are the features for the training
    # and testing datasets, respectively
    # labels_train and labels_test are the corresponding item labels
    features_train, features_test, labels_train, labels_test = preprocess()
    # features_train = features_train[:len(features_train) // 100]
    # labels_train = labels_train[:len(labels_train) // 100]
    #########################################################
    # your code goes here ###
    clf = svm.SVC(kernel=kernel, C=C)

    tic = time()
    clf.fit(features_train, labels_train)
    fit_time = time() - tic

    tic = time()
    pred = clf.predict(features_test)
    pred_time = time() - tic

    return accuracy_score(labels_test, pred), fit_time, pred_time
    #########################################################


def optimize_c():
    for c in [10, 100, 1000, 10000]:
        accuracy, fit_time, pred_time = svm_demo(kernel='rbf', C=c)
        print(f'C={c} accuracy={accuracy*100:.1f}%')


if __name__ == '__main__':
    # accuracy, fit_time, pred_time = svm_demo(kernel='linear')
    # accuracy, fit_time, pred_time = svm_demo(kernel='rbf')
    # optimize_c()
    accuracy, fit_time, pred_time = svm_demo(kernel='rbf', C=1000)
    print(f'accuracy={accuracy*100:.1f}% fit_time={fit_time:.4f}s pred_time={pred_time:.4f}s')
