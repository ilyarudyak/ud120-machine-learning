import pickle
import math


def load_data():
    """
        Starter code for exploring the Enron dataset (emails + finances);
        loads up the dataset (pickled dict of dicts).

        The dataset has the form:
        enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

        {features_dict} is a dictionary of features associated with that person.
        You should explore features_dict as part of the mini-project,
        but here's an example to get you started:

        enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

    """
    enron_data = pickle.load(open("final_project_dataset.pkl", "rb"))
    return enron_data


def process_name(name):
    return ' '.join(name.upper().split()[::-1])


def process_name_init(name):
    split_name = name.upper().split()
    index = [2, 0, 1]
    return ' '.join([split_name[i] for i in index])


def get_stocks(name, enron_data):
    stocks = {key: enron_data[name][key]
              for key in enron_data[name]
              if 'stock' in key}
    return stocks


def contains_guys(key):
    guys = ['LAY', 'SKILLING', 'FASTOW']
    return any([guy in key for guy in guys])


def follow_money():
    return {key: enron_data[key]['total_payments'] for key in enron_data if contains_guys(key)}


def is_nan(value):
    try:
        return math.isnan(float(value))
    except ValueError:
        return False


def quantified(keys):
    """
     return number of people with quantified keys (non NAN)
    """
    quants = [[(1 if not is_nan(enron_data[name][key]) else 0) for name in enron_data] for key in keys]
    return {key: sum(quant) for key, quant in zip(keys, quants)}

if __name__ == '__main__':
    enron_data = load_data()

    james_prentice = process_name('James Prentice')
    wesley_colwell = process_name('Wesley Colwell')
    jeffrey_k_skilling = process_name_init('Jeffrey K Skilling')

    # poi = [person for person in enron_data if enron_data[person]['poi']]
    keys = ['email_address', 'salary']
    print(quantified(keys))


