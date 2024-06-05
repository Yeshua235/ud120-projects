#!/usr/bin/python3
import os
import joblib
import sys
import matplotlib.pyplot as plt
sys.path.append(os.path.abspath("./tools/"))
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = joblib.load(open("./final_project/final_project_dataset.pkl", "rb") )

data_dict.pop('TOTAL', 0)


features = ["salary", "bonus"]
data = featureFormat(data_dict, features)

salary = data[:,:1]
bonus = data[:,1:]

### your code below
plt.scatter(salary, bonus)
plt.xlabel("salary")
plt.ylabel("bonus")
plt.show()

outlier_salary = 26704229
outlier_bonus = 97343619

#outlier = [person for person in data_dict if ((data_dict[person]['salary'] == outlier_salary) and (data_dict[person]['bonus'] == outlier_bonus))]
#print(data_dict[outlier[0]])
#print(outlier)
