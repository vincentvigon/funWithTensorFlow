import numpy as np
import tensorflow as tf

import TP25_winePrice.E_wineHelper as wine

sess = tf.InteractiveSession()
def pr(leg,a):
    print(leg+"\n",sess.run(a))




def step2():

    dataX = tf.constant([[1., 1], [4, 4], [1, 0], [5, 2]])
    dataY = tf.constant([10., 5, 11, 0])
    X = tf.constant([[2., 2],[10.,10]])

    ''' allPairwiseDiff_ijk= dataX_ijk - X_ik '''
    allPairwiseDiff = tf.sub(tf.expand_dims(dataX, 0), tf.expand_dims(X, 1))
    ''' allDist_ij=  Sum_k ( dataX_ijk - X_ik )^2 '''
    allDist = tf.reduce_sum(tf.square(allPairwiseDiff), 2)
    ''' weights_ij= exp -  Sum_k ( dataX_ijk - X_ik )^2 '''
    weights= tf.exp(-allDist/10) # alternative 1/(1+allDist)
    ''' totalWeight_i= 1/  Sum_j  exp -  Sum_k ( dataX_ijk - X_ik )^2 '''
    totalWeight=1/tf.reduce_sum(weights,1)
    '''weightedDataY_ij = weights_ij * dataY_j '''
    weightedDataY=tf.mul(weights,tf.expand_dims(dataY,0))
    '''weightedDataYNor_ij =  ( weights_ij * dataY_j ) / totalWeight_i '''
    weightedDataYNor=tf.mul(weightedDataY,tf.expand_dims(totalWeight,1))
    meanPrice=tf.reduce_sum(weightedDataYNor,1)


    pr("allPairwiseDiff", allPairwiseDiff)
    pr("allDist", allDist)
    pr("weight",weights)
    pr("totalWeight",totalWeight)
    pr("weightedDataY",weightedDataY)
    pr("weightedDataYNor",weightedDataYNor)
    pr("meanPrice",meanPrice)





def winePredictionWithGaussian(dataX, dataY, X, Y, k, squareError=True):
    ''' allPairwiseDiff_ijk= dataX_ijk - X_ik '''
    allPairwiseDiff = tf.sub(tf.expand_dims(dataX, 0), tf.expand_dims(X, 1))
    ''' allDist_ij=  Sum_k ( dataX_ijk - X_ik )^2 '''
    allDist = tf.reduce_sum(tf.square(allPairwiseDiff), 2)
    ''' weights_ij= exp -  Sum_k ( dataX_ijk - X_ik )^2 '''
    weights = tf.exp(-allDist / k)  # alternative 1/(1+allDist)
    ''' totalWeight_i= 1/  Sum_j  exp -  Sum_k ( dataX_ijk - X_ik )^2 '''
    totalWeight = 1 / tf.reduce_sum(weights, 1)
    '''weightedDataY_ij = weights_ij * dataY_j '''
    weightedDataY = tf.mul(weights, tf.expand_dims(dataY, 0))
    '''weightedDataYNor_ij =  ( weights_ij * dataY_j ) / totalWeight_i '''
    weightedDataYNor = tf.mul(weightedDataY, tf.expand_dims(totalWeight, 1))
    meanPrice = tf.reduce_sum(weightedDataYNor, 1)

    if squareError:
        error = tf.reduce_mean(tf.square(tf.sub(meanPrice, Y)))
    else:
        error = tf.reduce_mean(tf.abs(tf.sub(meanPrice, Y)))
    return error


def finalStep():
    nb=10
    ks=[10.,50.,80,100.,150,200,300]
    errors={}

    for j in range(nb):

        dataX,dataY =  wine.createWineData(15)
        X,Y = wine.createWineData(20)

        for k in ks:

            if errors.get(k) is None: errors[k]=np.zeros(nb)

            error=winePredictionWithGaussian(dataX, dataY, X, Y, k)
            errors[k][j]=sess.run(error)


    """ celui illustre la balance biais/erreur """
    for k in ks:
        print ("k:",k,"moy:",errors[k].mean(),"eq_type",errors[k].std())


finalStep()


'''
k: 10.0 moy: 2739.80944824 eq_type 1219.34665338
k: 50.0 moy: 2581.52525635 eq_type 1034.49004343
k: 80 moy: 2558.38039551 eq_type 974.352960779
k: 100.0 moy: 2570.73436279 eq_type 925.964899006
k: 150 moy: 2637.30675049 eq_type 808.996445039
k: 200 moy: 2723.55913086 eq_type 718.283356123
k: 300 moy: 2911.65800781 eq_type 609.523527845
'''


"""
Comparons avec kNN :
k: 1 moy: 2339.96381836 eq_type 1971.83498637
k: 2 moy: 2232.60392151 eq_type 1352.8925024
k: 3 moy: 2316.69503174 eq_type 1307.88034321
k: 5 moy: 2881.13510742 eq_type 1376.10734213
k: 8 moy: 3770.5866333 eq_type 1153.2223775
k: 10 moy: 4273.20219727 eq_type 1158.66602059
"""


"""
conclusion : on a fait mieux au niveau variance, moins bien au niveau biais.
"""