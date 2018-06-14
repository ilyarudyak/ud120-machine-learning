# coding=utf-8
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import tensorflow as tf

from tools.generate_terrane_data import make_terrain_data
from mlxtend.plotting import plot_decision_regions
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from tflow.reset import reset_graph


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def fit_logistic_regression_sklearn():
    lr = LogisticRegression()
    lr.fit(X_train, y_train)
    y_pred = lr.predict(X_test)
    print(lr.coef_, lr.intercept_)
    return accuracy_score(y_test, y_pred)


def fit_logistic_regression_tf(learning_rate=0.5, n_steps=50, verbose=True):
    X_train_ph, y_train_ph, W, b, train = set_model(learning_rate)
    Wb_ = run_model(X_train_ph, y_train_ph, W, b, train, n_steps, verbose)

    W, b = Wb_[-1][0], Wb_[-1][1]
    print(W, b)
    y_pred = np.matmul(W, X_test.T) + b > 0
    return accuracy_score(y_test, y_pred.flatten())


def set_model(learning_rate):
    # set variables
    X_train_ph = tf.placeholder(tf.float32, shape=[None, 2], name='X_train')
    y_train_ph = tf.placeholder(tf.float32, shape=None, name='y_train')

    with tf.name_scope('inference') as scope:
        W = tf.Variable([[0, 0]], dtype=tf.float32, name='weights')
        b = tf.Variable(0, dtype=tf.float32, name='bias')
        y_pred = tf.matmul(W, tf.transpose(X_train_ph)) + b

    # set loss
    with tf.name_scope('loss') as scope:
        # y_pred = tf.sigmoid(y_pred)
        # loss = y_train_ph * tf.log(y_pred) - (1 - y_train_ph) * tf.log(1 - y_pred)
        # loss = tf.reduce_mean(loss)
        loss = tf.nn.sigmoid_cross_entropy_with_logits(labels=y_train_ph, logits=y_pred)
        loss = tf.reduce_mean(loss)

    # set optimizer
    with tf.name_scope('train') as scope:
        optimizer = tf.train.GradientDescentOptimizer(learning_rate)
        train = optimizer.minimize(loss)

    return X_train_ph, y_train_ph, W, b, train


def run_model(X_train_ph, y_train_ph, W, b, train, n_steps, verbose):
    Wb_ = []
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)
        for step in range(n_steps+1):
            sess.run(train, {X_train_ph: X_train, y_train_ph: y_train})
            if step % 5 == 0:
                if verbose:
                    print(step, sess.run([W, b]))
                Wb_.append(sess.run([W, b]))
    return Wb_


if __name__ == '__main__':
    sns.set()
    reset_graph()
    X_train, y_train, X_test, y_test = make_terrain_data()
    # print(X_train.shape, y_train.shape)

    # print(f'lr sklearn accuracy = {fit_logistic_regression_sklearn():.4f}')
    # [[ 6.1711326   6.66971201]] [-5.30954405]
    # lr sklearn accuracy = 0.9280

    # print(f'lr tf accuracy = {fit_logistic_regression_tf():.4f}')

    print(fit_logistic_regression_tf(learning_rate=.1, n_steps=500, verbose=False))
