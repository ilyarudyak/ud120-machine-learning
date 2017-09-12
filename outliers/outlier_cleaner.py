import numpy as np
from outliers.data_utils import get_age_worth_data


def outlier_cleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    # your code goes here
    cut_off = int(.9 * predictions.shape[0])

    errors = np.abs(net_worths - predictions)
    index = np.argsort(errors)

    ages, net_worths, errors = ages[index], net_worths[index], errors[index]

    return ages[:cut_off], net_worths[:cut_off]


if __name__ == '__main__':

    ages_train, ages_test, net_worths_train, net_worths_test = get_age_worth_data()
    print(ages_train)


