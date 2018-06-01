#!/usr/bin/python

import os
import pickle
import re

from tools.parse_out_email_text import parse_out_text
from sklearn.feature_extraction.text import TfidfVectorizer


def vectorize_text():
    """
        Starter code to process the emails from Sara and Chris to extract
        the features and get the documents ready for classification.

        The list of all the emails from Sara are in the from_sara list
        likewise for emails from Chris (from_chris)

        The actual documents are in the Enron email dataset, which
        you downloaded/unpacked in Part 0 of the first mini-project. If you have
        not obtained the Enron email corpus, run startup.py in the tools folder.

        The data is stored in lists and packed away in pickle files at the end.
    """

    SARA = 'sara'
    CHRIS = 'chris'

    from_sara = open("from_sara.txt", "r")
    from_chris = open("from_chris.txt", "r")

    from_data = []
    word_data = []

    # temp_counter is a way to speed up the development--there are
    # thousands of emails from Sara and Chris, so running over all of them
    # can take a long time
    # temp_counter helps you only look at the first 200 emails in the list so you
    # can iterate your modifications quicker
    temp_counter = 0

    for name, from_person in [(SARA, from_sara), (CHRIS, from_chris)]:
        for path in from_person:
            # only look at first 200 emails when developing
            # once everything is working, remove this line to run over full dataset
            # temp_counter += 1
            # if temp_counter < 200:
            path = os.path.join('/', path[:-1])
            # print('{}:{}'.format(temp_counter, path))
            email_file = open(path, "r")

            # use parseOutText to extract the text from the opened email
            email_text = parse_out_text(email_file)

            # use str.replace() to remove any instances of the words
            for word in ["sara", "shackleton", "chris", "germani", "sshacklensf", "cgermannsf"]:
                email_text = email_text.replace(word, "")

            # append the text to word_data
            word_data.append(email_text)

            # append a 0 to from_data if email is from Sara, and 1 if email is from Chris
            from_data.append(0 if name == SARA else 1)

            email_file.close()

    print("emails processed")
    from_sara.close()
    from_chris.close()

    pickle.dump(word_data, open("ir_word_data.pkl", "wb"))
    pickle.dump(from_data, open("ir_email_authors.pkl", "wb"))

    return word_data


def transform(word_data):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(word_data)
    return vectorizer, X


if __name__ == '__main__':
    word_data = vectorize_text()
    # vectorizer, X = transform(word_data)
    #
    # vocabulary = vectorizer.get_feature_names()
    # print(len(vocabulary), vocabulary[34597])

