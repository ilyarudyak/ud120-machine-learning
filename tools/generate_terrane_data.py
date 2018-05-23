import numpy as np
from sklearn.model_selection import train_test_split


def make_terrain_data(n_points=1000):
    np.random.seed(42)
    X, error = np.random.rand(n_points, 2), np.random.rand(n_points)
    bumpy, grade = X[:, 0], X[:, 1]
    y = np.round(grade * bumpy + 0.3 + 0.1 * error).astype(int)
    y[np.logical_or(grade > .8, bumpy > .8)] = 1

    X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                        test_size=.25,
                                                        random_state=42)
    return X_train, y_train, X_test, y_test