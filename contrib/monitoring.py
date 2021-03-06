from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
import math
#
# from sklearn import datasets
#
#
# dataset = datasets.load_iris()
#
#
# n=len(dataset.target)
# trainProp=0.7
#
# rangeTrain=range(0, math.floor(n * trainProp))
# rangeTest=range(math.floor(n * trainProp), n)
#
# perm=np.random.permutation(n)
# X=dataset.data[perm]
# y=dataset.target[perm]
#
# X_train=X[rangeTrain]
# y_train=y[rangeTrain]
# X_test=X[rangeTest]
# y_test=y[rangeTest]

IRIS_TRAINING = "iris_training.csv"
IRIS_TEST = "iris_test.csv"

#Load datasets.
training_set = tf.contrib.learn.datasets.base.load_csv(filename=IRIS_TRAINING,target_dtype=np.int)
test_set = tf.contrib.learn.datasets.base.load_csv(filename=IRIS_TEST,
                                                   target_dtype=np.int)


#Build 3 layer DNN with 10, 20, 10 units respectively.
classifier = tf.contrib.learn.DNNClassifier(hidden_units=[10, 20, 10],
                                            n_classes=3,
                                            model_dir="/tmp/iris_model")

# Fit model.
classifier.fit(x=training_set.data,
               y=training_set.target,
               steps=2000)

# Evaluate accuracy.
accuracy_score = classifier.evaluate(x=test_set.data,y=test_set.target)["accuracy"]
print('Accuracy: {0:f}'.format(accuracy_score))

# Classify two new flower samples.
new_samples = np.array(
    [[6.4, 3.2, 4.5, 1.5], [5.8, 3.1, 5.0, 1.7]], dtype=float)
y = classifier.predict(new_samples)
print('Predictions: {}'.format(str(y)))

