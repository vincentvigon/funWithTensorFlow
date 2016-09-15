import random
import math
import tensorflow as tf
import matplotlib.pyplot as plt



sess = tf.InteractiveSession()
def pr(leg,a):
    print(leg+"\n",sess.run(a))


"""on crée le modèle. En entrée une liste de dataX,dataY et un point X dont il faut trouver le Y correspondant"""
def step1():
    dataX = tf.constant([[1., 1], [4, 4]])
    dataY = tf.constant([10.5, -3])

    X = tf.constant([[2., 2]])
    allPairwiseDiff = tf.sub(tf.expand_dims(dataX, 0), tf.expand_dims(X, 1))
    allDist = tf.pow(tf.reduce_sum(tf.pow(tf.abs(allPairwiseDiff), 1.5), 2),0.5)
    allSquaredDistInv = 1. / tf.reshape(allDist, [2])

    weightedValue = tf.mul(dataY, allSquaredDistInv)

    pr("allPairwiseDiff", allPairwiseDiff)
    pr("allSquaredDistInv", allSquaredDistInv)
    pr("weightedValue", weightedValue)
    return




"""maintenant on veut que le programme marche avec plusieurs X (et qu'il ressorte plusieurs Y).
Il s'agit donc d'augmenter la dimension de certains tenseurs"""
def step2(dataX, dataY, X):
    power=2.

    """conversion en tenseur"""
    dataX = tf.constant(dataX)
    dataY = tf.constant(dataY)
    X = tf.constant(X)

    allPairwiseDiff = tf.sub(tf.expand_dims(dataX, 0), tf.expand_dims(X, 1))
    allDist = tf.pow(tf.reduce_sum(tf.pow(tf.abs(allPairwiseDiff), power), 2),1/power)

    dataY=tf.expand_dims(dataY,0)

    allSquaredDistInv=1./(allDist+1)

    weightedValue=tf.mul(dataY, allSquaredDistInv)
    value=tf.reduce_sum(weightedValue,1)
    return value


dataX,dataY=wineSet1(200)
dataXTest,dataYTest=wineSet1(5)

dataYInfer =step2(dataX, dataY, dataXTest)

pr("dataYInfer", dataYInfer)
print("dataYTest",dataYTest)



# dataXTest,dataYTest_=wineSet1(10)
# for x in dataXTest:





def step3(dataX, dataY, X):
    power=2.

    """conversion en tenseur"""
    dataX = tf.constant(dataX)
    dataY = tf.constant(dataY)
    X = tf.constant(X)

    allPairwiseDiff = tf.sub(tf.expand_dims(dataX, 0), tf.expand_dims(X, 1))
    allDist = tf.pow(tf.reduce_sum(tf.pow(tf.abs(allPairwiseDiff), power), 2),1/power)

    pr("allDist",allDist)

    dataY=tf.expand_dims(dataY,0)
    pr("dataY",dataY)

    allSquaredDistInv=1./allDist

    weightedValue=tf.mul(dataY, allSquaredDistInv)
    pr('weightedValue',weightedValue)
    value=tf.reduce_sum(weightedValue,1)
    pr("value",value)
    return value



# dat=tf.constant([3.,4,2,1,-4])
# top=tf.nn.top_k(dat,k=2)
# print("aaaa",sess.run(top.values))









