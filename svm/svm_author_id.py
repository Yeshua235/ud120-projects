#!/usr/bin/python3

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
from sklearn import svm
from sklearn.metrics import accuracy_score

#########################################################

#########################################################
'''
You'll be Provided similar code in the Quiz
But the Code provided in Quiz has an Indexing issue
The Code Below solves that issue, So use this one
'''

#features_train = features_train[:int(len(features_train)/100)]
#labels_train = labels_train[:int(len(labels_train)/100)]
clf = svm.SVC(kernel='rbf', C=10000, gamma='scale')

#########################################################
t0 = time()
clf.fit(features_train, labels_train)
time_fit = round(time()-t0, 3)

t0 = time()
pred1 = clf.predict(features_test)
pred2 = clf.predict(features_train)
pred = list(pred1) + list(pred2)
time_predict = round(time()-t0, 3)

#accuracy = accuracy_score(labels_test, pred)

print(f"Training Time: {time_fit}s")
print(f"Prediction Time: {time_predict}s")
#print(f"Accuracy: {accuracy}")
print(f"Prediction for 10th element: {pred1[10]}")
print(f"Prediction for 26th element: {pred1[26]}")
print(f"Prediction for 50th element: {pred1[50]}")
print(f"Total Predictions for Chris(1): {sum([i for i in pred if i == 1])}")
