#!/usr/bin/python3

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

import joblib

enron_data = joblib.load(open("./final_project/final_project_dataset.pkl", "rb"))

keys = list(enron_data.keys())
print(f'Number of people in the dataset: {len(keys)}')
print(f'Number of features for each person: {len(enron_data[keys[0]])}')

available_poi = []
for i in enron_data:
    if enron_data[i]['poi'] == True:
        available_poi.append(i)

print(f'Number of POIs in the dataset: {len(available_poi)}')


with open("./final_project/poi_names.txt", 'r') as f:
    poi_names = list(f.readlines())

poi_names = [name.replace(name[:4], '') for name in poi_names]
poi_names = [name.replace('\n', '') for name in poi_names]
poi_names = [name.replace(',', '') for name in poi_names]
poi_names = poi_names[2:]
poi_names = [names.upper() for names in poi_names] #poi names in capital letter

poi = [name.split() for name in poi_names] #list of lists

print(f'Total number of POIs: {len(poi_names)}')
print(f"Total value of stocks belonging to James Prentice: {enron_data['PRENTICE JAMES']['total_stock_value']}")
print(f"Email messages from Wesley Colwell to POIs: {enron_data['COLWELL WESLEY']['from_this_person_to_poi']}")
print(f"Value of stock options exercised by Jeffrey K Skilling: {enron_data['SKILLING JEFFREY K']['exercised_stock_options']}")

print(f"Total payments to Lay, Skilling and Fastow: {enron_data['LAY KENNETH L']['total_payments']}, {enron_data['SKILLING JEFFREY K']['total_payments']}, {enron_data['FASTOW ANDREW S']['total_payments']}")

print(f"Number of those with quantified salary: {len([k for k in enron_data if enron_data[k]['salary'] != 'NaN'])}")
print(f"Number of those with known email address: {len([k for k in enron_data if enron_data[k]['email_address'] != 'NaN'])}")

total_payments_NaN = len([k for k in enron_data if enron_data[k]['total_payments'] == 'NaN'])
print(f"Number of people with NaN for total payments and perentage of total dataset: {total_payments_NaN}, {total_payments_NaN/len(enron_data)*100}%")

total_payments_NaN_POI = len([k for k in enron_data if ( (enron_data[k]['total_payments'] == 'NaN') and (enron_data[k]['poi'] == True) )])
print(f"Number of POIs with NaN for total payments and perentage of total dataset: {total_payments_NaN_POI}, {total_payments_NaN_POI/len(enron_data)*100}%")
#from itertools import islice
#for i in islice(enron_data, 1):
#    print(i, enron_data[i])
