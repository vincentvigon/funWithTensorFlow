import tensorflow as tf
from typing import List


"""===============================================================================================
étape 1: on cherche à assigner à chaque point son plus proche centroid
"""

""" astuce: le fait mettre un programme principal dans une fonction permet d'enfermer toutes les variables
 il n'y aura donc pas de variables globales avec des interactions potentiellement néfastes
"""
def step1():

    points = tf.constant([0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.])
    centroids = tf.Variable([7., 9.])

    pointsExp = tf.expand_dims(points, 0)
    centroidExp = tf.expand_dims(centroids, 1)
    allPairwiseDiff = tf.sub(pointsExp, centroidExp)
    allPairwiseDiffSquared = tf.square(allPairwiseDiff)
    """pour chacune des colonnes, on cherche l'indice de la plus petite valeur"""
    assignments=tf.argmin(allPairwiseDiffSquared, 0)

    init = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init)

    print('pointsExp\n',sess.run(pointsExp))
    print('centroidExp\n',sess.run(centroidExp))
    print('allPairwiseDiff\n',sess.run(allPairwiseDiff))
    print('allPairwiseDiffSquared\n',sess.run(allPairwiseDiffSquared))
    print('assignments\n',sess.run(assignments))

    return



"""===============================================================================================
étape 2:
On transforme l'étape 1 en une fonction.
Maintenant  regroupe les points selon leur centroid choisi dans l'étape 1, cela forme des clusters,
pour chaque cluster on calcul sa moyenne.
"""

def step2():


    def findClosestCentroid(_points, _centroids):
        pointsExp = tf.expand_dims(_points, 0)
        centroidExp = tf.expand_dims(_centroids, 1)
        allPairwiseDiff = tf.sub(pointsExp, centroidExp)
        allPairwiseDiffSquared = tf.square(allPairwiseDiff)
        return tf.argmin(allPairwiseDiffSquared, 0)

    points = tf.constant([0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 100.])
    centroids = tf.Variable([5., 9.])
    assignments=findClosestCentroid(points, centroids)

    """travaillons sur un cluster donné, mettons le 1 """
    c=1
    equalC=tf.equal(assignments, c)
    """on récupère la liste des indices où il y a des true """
    where = tf.where(equalC)
    """nous voulons simplement un tenseur d'ordre 1, donc on reshape
    jeter un coup d'oeil dans la doc (très bien faite) pour la fonction reshape"""
    whereFlatten=tf.reshape(where,[-1])

    oneCluster=tf.gather(points,whereFlatten)
    mean=tf.reduce_mean(oneCluster,0)



    init = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init)

    print('assignments\n', sess.run(assignments))
    print('equalC\n', sess.run(equalC))
    print('where\n', sess.run(where))
    print('whereFlatten\n', sess.run(whereFlatten))
    print('oneCluster\n', sess.run(oneCluster))
    print('mean\n', sess.run(mean))


    return



"""===============================================================================================
étape finale, il n'y a plus qu'à regrouper toutes ces moyennes en un vecteur,
on met tout cela dans une fonction
"""

def improveCentroid(points, centroids,nbCluster:int):


    def findClosestCentroid(_points, _centroids):
        pointsExp = tf.expand_dims(_points, 0)
        centroidExp = tf.expand_dims(_centroids, 1)
        allPairwiseDiff = tf.sub(pointsExp, centroidExp)
        allPairwiseDiffSquared = tf.square(allPairwiseDiff)
        return tf.argmin(allPairwiseDiffSquared, 0)


    assignments=findClosestCentroid(points, centroids)

    means=[] #type:List[float]
    for c in range(nbCluster):
        equalC = tf.equal(assignments, c)
        where = tf.where(equalC)
        whereFlatten = tf.reshape(where, [-1])
        oneCluster = tf.gather(points, whereFlatten)
        """tf.reduce_mean(oneCluster, 0) est un tenseur d'odre 0 (de  forme[]). On l'augment en un petit vecteur (de forme [1]), pour pouvoir ensuite faire une concaténation"""
        mean = tf.expand_dims(tf.reduce_mean(oneCluster, 0),0)
        means.append(mean)

    """maintenant collons tous nos tenseurs [1] et renvoyons le résultat"""
    return tf.concat(0,means)




def testFinal():
    points = tf.constant([0., 1., 2., 3., 4., 5., 6., 7., 8., 9., 10.])
    centroids = tf.Variable([7., 9.])
    nbCluster=2

    init = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init)

    centroids = improveCentroid(points, centroids,nbCluster)
    print(sess.run(centroids))

    centroids = improveCentroid(points, centroids,nbCluster)
    print(sess.run(centroids))

    centroids = improveCentroid(points, centroids,nbCluster)
    print(sess.run(centroids))

    centroids = improveCentroid(points, centroids,nbCluster)
    print(sess.run(centroids))
    return



testFinal()
#step2()