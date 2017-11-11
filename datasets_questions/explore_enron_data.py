#!/usr/bin/python

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

import pickle
enron_data = pickle.load(open("/Users/megan/Documents/Udacity-ML-Nondegree/ud120-projects-master/final_project/final_project_dataset.pkl", "r"))

from pandas import DataFrame
enron_data_df = DataFrame(enron_data)
# 21 is number of featuer, 146 is total data points
enron_data_df.shape
#(21, 146)

# number of poi in the dataset? 18.  poi: people of interests. 
enron=enron_data_df.T
enron[enron.poi == True]
# loop over dictionary
for key in enron_data:
    if enron_data[key]['poi'] == 1:
        count+=1
    print count

#How Many POIs Exist? 35.
path="/Users/megan/Documents/Udacity-ML-Nondegree/ud120-projects-master/final_project/poi_names.txt"
poi_names = open(path, 'r')
pio_names_full = poi_names.readlines()
len(pio_names_full) - 2
