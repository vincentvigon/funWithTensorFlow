
import tensorflow as tf


def findClosestCentroid(_points, _centroids):
    pointsExp = tf.expand_dims(_points, 0)
    centroidExp = tf.expand_dims(_centroids, 1)
    allPairwiseDiff = tf.sub(pointsExp, centroidExp)
    allPairwiseDiffSquaredDist = tf.reduce_sum(tf.square(allPairwiseDiff),2)
    return tf.argmin(allPairwiseDiffSquaredDist, 0)


centroids = tf.Variable([[0,0], [4,4]])

pointsAsList=[]
for i in range(5):
    for j in range(5):
        pointsAsList.append([i,j])

points = tf.constant(pointsAsList)


assignments=findClosestCentroid(points,centroids)

c=1
"""les indices où sont les points associés au cluster 'c' """
where = tf.where(tf.equal(assignments, c))
"""il faut leur enlever une dimension superflue"""
where = tf.reshape(where,[1,-1])
oneFamily = tf.gather(points, where)

init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)

print('assignments',sess.run(assignments))
print('where',sess.run(where))
print('oneFamily',sess.run(oneFamily))