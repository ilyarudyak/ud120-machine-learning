import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

from tools.generate_terrane_data import make_terrain_data

from mlxtend.plotting import plot_decision_regions
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def dt_classifier_mlxtend():
    plot_decision_regions(X_train, y_train,
                          # clf=dt,
                          clf=lr,
                          legend=2,
                          markers='ooo^v',
                          colors='#66cdaa,#ff0000')
    format_plot()


def format_plot():
    plt.xlabel('bumpy')
    plt.ylabel('grade')
    plt.title('DecisionTreeClassifier for terrain data')
    plt.xlim(0, 1.0)
    plt.ylim(0, 1.0)


if __name__ == '__main__':
    X_train, y_train, X_test, y_test = make_terrain_data()
    dt = DecisionTreeClassifier()
    dt.fit(X_train, y_train)
    # dt50 = DecisionTreeClassifier(min_samples_split=50)
    # dt50.fit(X_train, y_train)

    lr = LogisticRegression()
    lr.fit(X_train, y_train)

    dt_classifier_mlxtend()
    plt.show()
    # print(f'min_samples_split=2 accuracy={accuracy_score(y_test, dt.predict(X_test))*100:.1f}%')
    # print(f'min_samples_split=50 accuracy={accuracy_score(y_test, dt50.predict(X_test))*100:.1f}%')
