"""
    Starter code for the regression mini-project.
    
    Loads up/formats a modified version of the dataset
    (why modified?  we've removed some trouble points
    that you'll find yourself in the outliers mini-project).

    Draws a little scatterplot of the training/testing data

    You fill in the regression code where indicated:
"""

import pickle
from tools.feature_format import featureFormat, targetFeatureSplit
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression


def get_data(features_list):
    dictionary = pickle.load(open("final_project_dataset_modified.pkl", "rb"))
    # list the features you want to look at--first item in the
    # list will be the "target" feature
    data = featureFormat(dictionary, features_list, remove_any_zeroes=True,
                         sort_keys='../tools/python2_lesson06_keys.pkl')
    target, features = targetFeatureSplit(data)

    return train_test_split(features, target, test_size=0.5, random_state=42)


def fit_regression(features_list):
    feature_train, feature_test, target_train, target_test = get_data(features_list)

    # Your regression goes here!
    # Please name it reg, so that the plotting code below picks it up and
    # plots it correctly. Don't forget to change the test_color above from "b" to
    # "r" to differentiate training points from test points.
    reg = LinearRegression()
    reg.fit(feature_train, target_train)

    return reg


def plot_data(features_list):
    feature_train, feature_test, target_train, target_test = get_data(features_list)
    features_list = ["bonus", "salary"]
    reg = fit_regression(features_list)

    # draw the scatterplot, with color-coded training and testing points
    train_color = "b"
    test_color = "r"

    for feature, target in zip(feature_test, target_test):
        plt.scatter(feature, target, color=test_color)
    for feature, target in zip(feature_train, target_train):
        plt.scatter(feature, target, color=train_color)

    # labels for the legend
    plt.scatter(feature_test[0], target_test[0], color=test_color, label="test")
    plt.scatter(feature_test[0], target_test[0], color=train_color, label="train")

    # draw the regression line, once it's coded
    try:
        plt.plot(feature_test, reg.predict(feature_test))

        # build regression on test data
        reg.fit(feature_test, target_test)
        plt.plot(feature_train, reg.predict(feature_train), color="r")
        print(reg.coef_)

    except NameError:
        pass
    plt.xlabel(features_list[1])
    plt.ylabel(features_list[0])
    plt.legend()
    plt.show()


if __name__ == '__main__':
    features_list = ['bonus', 'salary']
    # features_list = ['bonus', 'long_term_incentive']
    # feature_train, feature_test, target_train, target_test = get_data(features_list)
    # reg = fit_regression(features_list)
    # print(reg.coef_, reg.intercept_, reg.score(feature_train, target_train), reg.score(feature_test, target_test))
    plot_data(features_list)
