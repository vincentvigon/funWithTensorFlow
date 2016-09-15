import numpy as np
import tensorflow as tf

import TP25_winePrice.E_wineHelper as wine

sess = tf.InteractiveSession()
def pr(leg,a):
    print(leg+"\n",sess.run(a))



''' plusieurs données, 1 point à évaluer'''
def step1():

    k=2

    dataX = tf.constant([[1., 1], [4, 4],[1,0],[5,2]])
    dataY = tf.constant([10., 5 ,11,0])
    X = tf.constant([2., 2])

    ''' allPairwiseDiff_jk= dataX_jk - X_k '''
    allPairwiseDiff = tf.sub(dataX, X)
    ''' allDist_j=  Sum_k ( dataX_jk - X_k )^2 '''
    allDist = tf.reduce_sum( tf.square(allPairwiseDiff),1)
    '''  bestIndices  = k-argmax_j allDist_j  ) '''
    bestIndices=tf.nn.top_k(allDist,k=k).indices
    ''' gather  = datY évalué en bestIndices  '''
    gather=tf.gather(dataY,bestIndices)
    ''' meanPrice = moyenne(gather) '''
    meanPrice=tf.reduce_mean(gather)


    pr("allPairwiseDiff", allPairwiseDiff)
    pr("allDist",allDist)
    pr("bestIndices",bestIndices)
    pr("gather",gather)
    pr("meanPrice",meanPrice)



''' plusieurs données, plusieurs points à évaluer'''
def step2():
    k = 2

    dataX = tf.constant([[1., 1], [4, 4], [1, 0], [5, 2]])
    dataY = tf.constant([10., 5, 11, 0])
    X = tf.constant([[2., 2],[10.,10]])

    ''' allPairwiseDiff_ijk= dataX_ijk - X_ik '''
    allPairwiseDiff = tf.sub(tf.expand_dims(dataX, 0), tf.expand_dims(X, 1))
    ''' allDist_ij=  Sum_k ( dataX_ijk - X_ik )^2
     est maintenant composé de plusieurs lignes, 1 ligne par point X à évaluer'''
    allDist = -tf.reduce_sum(tf.square(allPairwiseDiff), 2)
    bestIndices = tf.nn.top_k(allDist, k=k).indices
    gather = tf.gather(dataY, bestIndices)
    meanPrice = tf.reduce_mean(gather,1)

    pr("allPairwiseDiff", allPairwiseDiff)
    pr("allDist", allDist)
    pr("bestIndices", bestIndices)
    pr("gather", gather)
    pr("meanPrice", meanPrice)



'''transformons le travail précédent en une fonction qui prédit Y et calcule une erreur'''
def winePredictionWithKNN(dataX, dataY, X, Y, k, squareError=True):
    allPairwiseDiff = tf.sub(tf.expand_dims(dataX, 0), tf.expand_dims(X, 1))
    allDist = -tf.reduce_sum(tf.square(allPairwiseDiff), 2)

    bestIndices = tf.nn.top_k(allDist, k=k).indices
    gather = tf.gather(dataY, bestIndices)
    meanPrice = tf.reduce_mean(gather, 1)
    """ mathématiquement,  qu'est-ce que cela change d'utiliser le carré ou la valeur absolue des différences pour mesure les erreurs? """
    if squareError : error= tf.reduce_mean(tf.square(tf.sub(meanPrice, Y)))
    else : error = tf.reduce_mean(tf.abs(tf.sub(meanPrice, Y)))
    return error


'''essayons nos prédictions sur différents jeu de données simulées.'''
def finalStep():
    nbTrial=10
    ks=[1,2,3,5,8,10]
    errors={}

    for trial in range(nbTrial):

        dataX,dataY =  wine.createWineData(15)
        X,Y = wine.createWineData(10)

        for k in ks:
            if errors.get(k) is None: errors[k]=np.zeros(nbTrial)
            error=winePredictionWithKNN(dataX,dataY,X,Y,k)
            errors[k][trial]=sess.run(error)


    """ celui illustre la balance biais/erreur """
    for k in ks:
        print ("k:",k,"moy:",errors[k].mean(),"eq_type",errors[k].std())


finalStep()

"""
k: 1 moy: 2339.96381836 eq_type 1971.83498637
k: 2 moy: 2232.60392151 eq_type 1352.8925024
k: 3 moy: 2316.69503174 eq_type 1307.88034321
k: 5 moy: 2881.13510742 eq_type 1376.10734213
k: 8 moy: 3770.5866333 eq_type 1153.2223775
k: 10 moy: 4273.20219727 eq_type 1158.66602059
"""
