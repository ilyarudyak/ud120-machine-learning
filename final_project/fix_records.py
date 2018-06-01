def fixBhatnagar(data):

    """
    :param data:
    :return: Fixes out of sync records of Sanjay Bhatnagar and returns a data_dict with the
             updated values
    """
    data['BHATNAGAR SANJAY'] = data.fromkeys(data['BHATNAGAR SANJAY'], 'NaN')
    data['BHATNAGAR SANJAY']['expenses'] = 137864
    data['BHATNAGAR SANJAY']['total_payments'] = 137864
    data['BHATNAGAR SANJAY']['exercised_stock_options'] = 15456290
    data['BHATNAGAR SANJAY']['restricted_stock'] = 2604490
    data['BHATNAGAR SANJAY']['restricted_stock_deferred'] = -2604490
    data['BHATNAGAR SANJAY']['total_stock_value'] = 15456290
    data['BHATNAGAR SANJAY']['from_messages'] = 29
    data['BHATNAGAR SANJAY']['to_messages'] = 523
    data['BHATNAGAR SANJAY']['shared_receipt_with_poi'] = 463
    data['BHATNAGAR SANJAY']['from_this_person_to_poi'] = 1
    data['BHATNAGAR SANJAY']['from_poi_to_this_person'] = 0
    data['BHATNAGAR SANJAY']['poi'] = False
    return data

def fixBelfer(data):
    """
    :param data:
    :return: Fixes out of sync records of Robert Belfer and returns a data_dict with the
             updated values
    """
    data['BELFER ROBERT'] = data.fromkeys(data['BELFER ROBERT'], 'NaN')
    data['BELFER ROBERT']['deferred_income'] = -102500
    data['BELFER ROBERT']['expenses'] = 3285
    data['BELFER ROBERT']['director_fees'] = 102500
    data['BELFER ROBERT']['total_payments'] = 3285
    data['BELFER ROBERT']['restricted_stock'] = 44093
    data['BELFER ROBERT']['restricted_stock_deferred'] = -44093
    data['BELFER ROBERT']['poi'] = False
    return data