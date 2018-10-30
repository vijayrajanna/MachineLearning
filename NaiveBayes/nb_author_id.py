#!/usr/bin/python

""" 
    this is the code to accompany the Lesson 1 (Naive Bayes) mini-project 

    use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1

"""
    
import sys
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# Creating the object of the class.
naive_base_classifier = GaussianNB()
naive_base_classifier.fit(features_train,labels_train)
list_predictedLCass = naive_base_classifier.predict(features_test)
print ('Predicted Classes')
print(list_predictedLCass)
print ('Actual Classes')
print (labels_test)
accuracy = '{}'.format(accuracy_score(labels_test,list_predictedLCass,normalize=True)*100) + '%'
print(accuracy)

#########################################################
### your code goes here ###
# Create classifier on the training data set.



#########################################################


