from enron.explore_enron_data import *


def missing(keys):
    return {key: len(enron_data) - quantified(keys)[key] for key in keys}


def missing_poi(keys):
    return {key: total_poi() - quantified_poi(keys)[key] for key in keys }

if __name__ == '__main__':
    james_prentice = process_name('James Prentice')
    total_payments = ['total_payments']

    print(total_poi(), missing_poi(total_payments))

