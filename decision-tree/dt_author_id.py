from time import time
from tools.email_preprocess import preprocess
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def dt_classifier():
    """
        This is the code to accompany the Lesson 3 (decision tree) mini-project.

        Use a Decision Tree to identify emails from the Enron corpus by author:
        Sara has label 0
        Chris has label 1
    """

    #########################################################
    # your code goes here ###
    clf = DecisionTreeClassifier(min_samples_split=40)

    tic = time()
    clf.fit(features_train, labels_train)
    fit_time = time() - tic

    tic = time()
    pred = clf.predict(features_test)
    pred_time = time() - tic

    return accuracy_score(labels_test, pred), fit_time, pred_time
    #########################################################


if __name__ == '__main__':
    features_train, features_test, labels_train, labels_test = preprocess()
    accuracy, fit_time, pred_time = dt_classifier()
    print(f'accuracy={accuracy*100:.1f}% fit_time={fit_time:.4f}s pred_time={pred_time:.4f}s')
    # print(len(features_train[0]))

