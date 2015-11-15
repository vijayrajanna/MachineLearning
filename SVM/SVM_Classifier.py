'''from sklearn import svm
X = [[0, 0], [1, 1]]
y = [0, 1]
clf = svm.SVC()
clf.fit(X, y)
print clf.predict([[0, 0], [1, 1], [0,1], [1,0]])'''

import sys
from class_vis import prettyPicture
from prep_terrain_data import makeTerrainData

import matplotlib.pyplot as plt
import copy
import numpy as np
import pylab as pl


features_train, labels_train, features_test, labels_test = makeTerrainData()


########################## SVM #################################
### we handle the import statement and SVC creation for you here
from sklearn.svm import SVC


#### now your job is to fit the classifier
#### using the training features/labels, and to
#### make a set of predictions on the test data
#### store your predictions in a list named pred

clf = SVC(kernel="linear")
clf.fit(features_train,labels_train)
pred =clf.predict(features_test)
print 'The predicted classes are'
print '-------------------------'
print pred
print '-------------------------'

from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)
print acc

def submitAccuracy():
    return acc