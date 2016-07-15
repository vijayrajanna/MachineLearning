#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from sklearn.svm import SVC
from time import time

sys.path.append("../tools/")
from email_preprocess import preprocess


rightclass = 0

def accuracy_score(listA, listB):
    global rightclass
    for index in range(0,len(listA)):
        if listA[index] == listB[index]:
            rightclass = rightclass +1
    print rightclass
    print len(listA)
    return (float(rightclass)/len(listA))*100


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

svmClassifier = SVC(kernel="linear")
# svmClassifier = SVC(kernel="rbf",C=0.5)
svmClassifier.fit(features_train,labels_train)
pred = svmClassifier.predict(features_test)
acc = accuracy_score(pred, labels_test)
print acc

#########################################################
### your code goes here ###

#########################################################


