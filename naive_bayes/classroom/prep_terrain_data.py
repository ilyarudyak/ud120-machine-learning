#!/usr/bin/python
import random
import matplotlib.pyplot as plt


def makeTerrainData(n_points=1000):
    ###############################################################################
    ### make the toy dataset
    random.seed(42)
    grade = [random.random() for _ in range(0, n_points)]
    bumpy = [random.random() for _ in range(0, n_points)]
    error = [random.random() for _ in range(0, n_points)]
    y = [round(grade[i] * bumpy[i] + 0.3 + 0.1 * error[i]) for i in range(0, n_points)]
    for i in range(0, len(y)):
        if grade[i] > 0.8 or bumpy[i] > 0.8:
            y[i] = 1

    ### split into train/test sets

    X = [[g, s] for g, s in zip(grade, bumpy)]
    split = int(0.75 * n_points)
    X_train, X_test = X[0:split], X[split:]
    y_train, y_test = y[0:split], y[split:]

    # grade_sig = [X_train[ii][0] for ii in range(0, len(X_train)) if y_train[ii] == 0]
    # bumpy_sig = [X_train[ii][1] for ii in range(0, len(X_train)) if y_train[ii] == 0]
    # grade_bkg = [X_train[ii][0] for ii in range(0, len(X_train)) if y_train[ii] == 1]
    # bumpy_bkg = [X_train[ii][1] for ii in range(0, len(X_train)) if y_train[ii] == 1]

    #    training_data = {"fast":{"grade":grade_sig, "bumpiness":bumpy_sig}
    #            , "slow":{"grade":grade_bkg, "bumpiness":bumpy_bkg}}

    # grade_sig = [X_test[ii][0] for ii in range(0, len(X_test)) if y_test[ii] == 0]
    # bumpy_sig = [X_test[ii][1] for ii in range(0, len(X_test)) if y_test[ii] == 0]
    # grade_bkg = [X_test[ii][0] for ii in range(0, len(X_test)) if y_test[ii] == 1]
    # bumpy_bkg = [X_test[ii][1] for ii in range(0, len(X_test)) if y_test[ii] == 1]
    #
    # test_data = {"fast": {"grade": grade_sig, "bumpiness": bumpy_sig}
    #     , "slow": {"grade": grade_bkg, "bumpiness": bumpy_bkg}}

    return X_train, y_train, X_test, y_test
#    return training_data, test_data


if __name__ == '__main__':
    makeTerrainData()
