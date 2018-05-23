import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns; sns.set()

from sklearn.model_selection import train_test_split
from mlxtend.plotting import plot_decision_regions
from sklearn.svm import SVC


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


def plot_terrain_data():
    grade, bumpy = X_train[:, 0], X_train[:, 1]
    plt.scatter(bumpy, grade, c=y_train, cmap='seismic')
    plt.xlabel('bumpy')
    plt.ylabel('grade')


def svm_classifier_mlxtend():
    plot_decision_regions(X_train, y_train,
                          clf=svm,
                          legend=2,
                          markers='ooo^v',
                          colors='#66cdaa,#ff0000')
    format_plot()


def format_plot():
    plt.xlabel('bumpy')
    plt.ylabel('grade')
    plt.title('Gaussian NB for terrain data')
    plt.xlim(0, 1.0)
    plt.ylim(0, 1.0)


if __name__ == '__main__':
    X_train, y_train, X_test, y_test = make_terrain_data()
    # svm = SVC(kernel="linear").fit(X_train, y_train)
    # svm = SVC(kernel="rbf", C=10000).fit(X_train, y_train)
    svm = SVC(kernel="rbf", gamma=100)
    svm.fit(X_train, y_train)

    svm_classifier_mlxtend()
    plt.show()
