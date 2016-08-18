

#Import Library
#Import other necessary libraries like pandas, numpy...
from sklearn import datasets
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation
from sklearn import metrics

from sklearn import tree
import math
import numpy as np

dataset = datasets.load_iris()


'''https://www.analyticsvidhya.com/blog/2016/04/complete-tutorial-tree-based-modeling-scratch-in-python/'''

n=len(dataset.target)
trainProp=0.7

rangeTrain=range(0, math.floor(n * trainProp))
rangeTest=range(math.floor(n * trainProp), n)

perm=np.random.permutation(n)
X=dataset.data[perm]
y=dataset.target[perm]

X_train=X[rangeTrain]
y_train=y[rangeTrain]
X_test=X[rangeTest]
y_test=y[rangeTest]


model = tree.DecisionTreeClassifier(criterion='gini') # for classification, here you can change the algorithm as gini or entropy (information gain) by default it is gini
# model = tree.DecisionTreeRegressor() for regression
# Train the model using the training sets and check score

model.fit(X_train, y_train)
print(model.score(X_train, y_train))


#Predict Output
y_testPredicted= model.predict(X_test)
#print(y_testPredicted,'\n',y_test)
#print(model.score(X_test, y_test))
accuracy = metrics.accuracy_score(y_test,y_testPredicted)
print(accuracy,"Accuracy : %s" % "{0:.3%}".format(accuracy))