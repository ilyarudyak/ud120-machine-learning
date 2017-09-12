import random
import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LinearRegression
from outliers.data_utils import get_age_worth_data


def regression_wo_removal():
    ages_train, ages_test, net_worths_train, net_worths_test = get_age_worth_data()

    reg = LinearRegression()
    reg.fit(ages_train, net_worths_train)

    print(ages_train.shape[0], reg.coef_, reg.score(ages_test, net_worths_test))

    plt.plot(ages_train, reg.predict(ages_train), color="blue")
    plt.scatter(ages_train, net_worths_train)
    plt.show()


def remove_outliers():
    ages_train, ages_test, net_worths_train, net_worths_test = get_age_worth_data()

    print(type(ages_train), ages_train.shape)

    # fill in a regression here!  Name the regression object reg so that
    # the plotting code below works, and you can see what your regression looks like
    # reg = LinearRegression()
    # reg.fit(ages_train, net_worths_train)

    # print(reg.coef_, reg.score(ages_test, net_worths_test))
    #
    # try:
    #     plt.plot(ages, reg.predict(ages), color="blue")
    # except NameError:
    #     pass
    # plt.scatter(ages, net_worths)
    # plt.show()

    # identify and remove the most outlier-y points
    # predictions = reg.predict(ages_train)
    # cleaned_data = outlier_cleaner(predictions, ages_train, net_worths_train)
    # print(cleaned_data)

    # ages, net_worths, errors = zip(*cleaned_data)
    # ages = np.reshape(np.array(ages), (len(ages), 1))
    # net_worths = np.reshape(np.array(net_worths), (len(net_worths), 1))
    #
    # # refit your cleaned data!
    # try:
    #     reg.fit(ages, net_worths)
    #     print(reg.coef_)
    #     plt.plot(ages, reg.predict(ages), color="blue")
    # except NameError:
    #     print("you don't seem to have regression imported/created,")
    #     print("   or else your regression object isn't named reg")
    #     print("   either way, only draw the scatter plot of the cleaned data")
    # plt.scatter(ages, net_worths)
    # plt.xlabel("ages")
    # plt.ylabel("net worths")
    # plt.show()



if __name__ == '__main__':
    regression_wo_removal()
