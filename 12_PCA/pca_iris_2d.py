print(__doc__)
from sklearn import decomposition
from sklearn import datasets
from sklearn.svm import SVC
import matplotlib.pyplot as plt
from sklearn import cross_validation
from sklearn.naive_bayes import GaussianNB
from sklearn import tree

iris = datasets.load_iris()
X = iris.data
Y = iris.target

pca = decomposition.PCA(n_components=2)
pca.fit(X)
X = pca.transform(X)
print 'After PCA'
print X
print Y

newXvalues = []
newYvalues = []

for index in range(0,len(X)):
    newXvalues.append((X[index])[0])
    newYvalues.append((X[index])[1])

flowertype = []

for index1 in range(0,len(Y)):
    if Y[index1] == 0:
        flowertype.append('red')
    elif Y[index1] == 1:
        flowertype.append('green')
    else:
        flowertype.append('blue')

# Go ahead and classify
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(X,Y, test_size=0.4, random_state=0)

# Firs with Naive base classifier
print 'Accuracy of Naive base classifier is ',
naive_base_classifier = GaussianNB()
naive_base_classifier.fit(features_train,labels_train)
print naive_base_classifier.score(features_test, labels_test)

# Next with SVM
print 'Accuracy of SVM classifier is ',
clf = SVC(kernel="linear", C=1.)
clf.fit(features_train, labels_train)
print clf.score(features_test, labels_test)

# Next with Decision Tree
print 'Accuracy of Decision Tree classifier is ',
decisionTree = tree.DecisionTreeClassifier()
decisionTree.fit(features_train,labels_train)
print decisionTree.score(features_test,labels_test)

plt.scatter(newXvalues, newYvalues, c=flowertype, alpha=0.5)
plt.show()