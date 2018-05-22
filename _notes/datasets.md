### final_project_dataset.pkl

- it seems we have here a dict (keys are persons, len=146) of dict (len=21):
`{'METTS MARK': {...}, 'BAXTER JOHN C': {...}, ...}`
- we have 18 POIs (probably they are in the `poi_names.txt` as well) in this file:
`['HANNON KEVIN P', 'COLWELL WESLEY', 'RIEKER PAULA H', 'KOPPER MICHAEL J', 
'SHELBY REX', 'DELAINEY DAVID W', 'LAY KENNETH L', 'BOWEN JR RAYMOND M', 
'BELDEN TIMOTHY N', 'FASTOW ANDREW S', 'CALGER CHRISTOPHER F', 'RICE KENNETH D', 
'SKILLING JEFFREY K', 'YEAGER F SCOTT', 'HIRKO JOSEPH', 'KOENIG MARK E', 
'CAUSEY RICHARD A', 'GLISAN JR BEN F']`
- keys of the 2nd dict (## of the column (or its name) from the financial 
spreadsheet enron61702insiderpay.pdf): 
`dict_keys(['salary'(1), 'to_messages', 'deferral_payments'(5), 'total_payments'(Total Payments), 
'loan_advances'(6), 'bonus'(2), 'email_address', 'restricted_stock_deferred'(12), 
'deferred_income'(4), 'total_stock_value'(Total Stock Value), 'expenses'(8), 'from_poi_to_this_person', 
'exercised_stock_options'(10), 'from_messages', 'other'(7), 'from_this_person_to_poi', 
'poi', 'long_term_incentive'(3), 'shared_receipt_with_poi', 'restricted_stock'(11), 'director_fees'(9)])`;
- so we have all the information from the financial spreadsheet and also the following keys:
`'to_messages', 'email_address', 'from_poi_to_this_person', 'from_messages', 
'from_this_person_to_poi', 'poi', 'shared_receipt_with_poi'`;


### poi_names.txt

- we have 35 POIs in this file; only 4 of them have folders in `maildir`;

 