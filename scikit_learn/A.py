
import numpy as np

import matplotlib as plt

from sklearn import datasets

from sklearn import metrics

from sklearn.linear_model import LogisticRegression

from sklearn import cross_validation


'''https://www.analyticsvidhya.com/blog/2015/01/scikit-learn-python-machine-learning-tool/'''

'''Description des donnée : voir wikipedia.
https://en.wikipedia.org/wiki/Iris_flower_data_set'''

dataset = datasets.load_iris()


cv = cross_validation.KFold(dataset.data.shape[0], n_folds=5)
model=LogisticRegression()
#
# model.fit( dataset.data, dataset.target)


for traincv, testcv in cv:
    model.fit(dataset.data[traincv], dataset.target[traincv]) #.predict_proba(train[testcv])
    predicted = model.predict(dataset.data[testcv])
    expected = dataset.target[testcv]
    print(metrics.classification_report(expected, predicted))
    #print(metrics.confusion_matrix(expected, predicted))
    #print(predicted,expected,"\n\n")



#
# expected = dataset.target
# predicted = model.predict(dataset.data)
#
# print(expected)
# print(predicted)





