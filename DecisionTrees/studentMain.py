#!/usr/bin/python

""" lecture and example code for decision tree unit """

import sys
from class_vis import prettyPicture, output_image
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
from classifyDT import classify
from sklearn.metrics import accuracy_score

features_train, labels_train, features_test, labels_test = makeTerrainData()



### the classify() function in classifyDT is where the magic
### happens--it's your job to fill this in!
clf = classify(features_train, labels_train)

# Now we need to compute the accuracy.
predictedClasses = clf.predict(features_test)
print 'The accuracy of the classification is'
print(accuracy_score(labels_test,predictedClasses,normalize=True))

#### grader code, do not modify below this line

prettyPicture(clf, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())
