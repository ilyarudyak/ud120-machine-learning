import numpy as np
from outliers.data_utils import get_age_worth_data
from sklearn.linear_model import LinearRegression


def outlier_cleaner(predictions, ages_train, net_worths_train):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    # your code goes here
    size = predictions.shape[0]
    cut_off = int(.9 * size)
    errors = np.abs(net_worths_train - predictions)
    index = np.argsort(errors, axis=0)
    ages_train_clean, net_worths_train_clean = ages_train[index].reshape(size, 1), net_worths_train[index, :].reshape(size, 1)

    return ages_train_clean[:cut_off], net_worths_train_clean[:cut_off]


def fit_regression(ages_train, ages_test, net_worths_train, net_worths_test):
    reg = LinearRegression()
    reg.fit(ages_train, net_worths_train)
    predictions = reg.predict(ages_train)
    score = reg.score(ages_test, net_worths_test)
    coef = reg.coef_
    return predictions, score, coef


if __name__ == '__main__':

    ages_train, ages_test, net_worths_train, net_worths_test = get_age_worth_data()
    predictions, score, coef = fit_regression(ages_train, ages_test, net_worths_train, net_worths_test)

    ages_train_clean, net_worths_train_clean = outlier_cleaner(predictions, ages_train, net_worths_train)
    predictions, score, coef = fit_regression(ages_train_clean, ages_test, net_worths_train_clean, net_worths_test)
    print(score, coef)

