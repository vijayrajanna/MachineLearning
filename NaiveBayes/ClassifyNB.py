def classify(features_train, labels_train):
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier

    ### your code goes here!
    from sklearn.naive_bayes import GaussianNB
    from sklearn.metrics import accuracy_score
    clf = GaussianNB()
    clf.fit(features_train,labels_train)
    predictedClasses = clf.predict(features_train)
    print (predictedClasses)

    # Now we need to compute the accuracy.
    print 'The accuracy of the classification with training set'
    print accuracy_score(labels_train,predictedClasses,normalize=True)
    return clf #returning the classifier