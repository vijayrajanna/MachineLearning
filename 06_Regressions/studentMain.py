#!/usr/bin/python

import numpy
import matplotlib
matplotlib.use('agg')

import matplotlib.pyplot as plt
from studentRegression import studentReg
from class_vis import prettyPicture, output_image
from ages_net_worths import ageNetWorthData

ages_train, ages_test, net_worths_train, net_worths_test = ageNetWorthData()
reg = studentReg(ages_train, net_worths_train)

# Let's print some stats

# Predict
print "Predicting the net-worth for age 27 ", reg.predict([27])

#Slope
print "Slope of the regression line is ", reg.coef_

#What is the Y intercept
print "Y intercept of the regression is ", reg.intercept_

# Here there is an important point to be noted.
# You should look at r-sqr for both test and training data.
# Because, usually, the training data will give you a good r-sqr.
# However, if there is over fitting then the r-sqr for test data set will be low.
# So, checking r-sqr for both test and train simultaneously give you a better understanding of the goodness of fit.

# Since the regression is already fit using the training data, the system already knows
# the relationship between ages_train and net_worths_train
print "\n ########################## stats on training dataset ###########\n"
print "r-squared score", reg.score(ages_train,net_worths_train)

print "\n ########################## stats on test dataset ###########\n"
print "r-squared score", reg.score(ages_test,net_worths_test)

# Now plot the results
plt.clf()
plt.scatter(ages_train, net_worths_train, color="b", label="train data")
plt.scatter(ages_test, net_worths_test, color="r", label="test data")
plt.plot(ages_test, reg.predict(ages_test), color="black")
plt.legend(loc=2)
plt.xlabel("ages")
plt.ylabel("net worths")
plt.savefig("test.png")
output_image("test.png", "png", open("test.png", "rb").read())
plt._show