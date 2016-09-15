import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf



num_vectors = 1000
num_clusters = 3
num_steps = 100
vector_values = []


"""des points aléatoires. C'est un tenseur constant"""
vectors = tf.random_normal([num_vectors,2])


"""tirage aléatoire de num_clusters  vectors """
vectorsShuffle=tf.random_shuffle(vectors)
"""on extrait un sous-tenseur commençant aux indices [0,0] et de taille [num_clusters,-1] (le -1 signifiant : on va jusqu'au bord) """
subVectorsShuffle=tf.slice(vectorsShuffle, [0,0],[num_clusters,-1])
"""on défini une variable initialisée sur le tenseur ci-dessus
on le déclare comme variables car on va le faire évoluer par la suite"""
centroids = tf.Variable(subVectorsShuffle)


"""rajout de dimensions"""
expanded_vectors = tf.expand_dims(vectors, 0)
expanded_centroids = tf.expand_dims(centroids, 1)

print(expanded_vectors.get_shape())
print(expanded_centroids.get_shape())








#
# distances = tf.reduce_sum(
#   tf.square(tf.sub(expanded_vectors, expanded_centroids)), 2)
# assignments = tf.argmin(distances, 0)
#
#
# means = tf.concat(0, [
#   tf.reduce_mean(
#       tf.gather(vectors,
#                 tf.reshape(
#                   tf.where(
#                     tf.equal(assignments, c)
#                   ),[1,-1])
#                ),reduction_indices=[1])
#   for c in range(num_clusters)])
#
# update_centroids = tf.assign(centroids, means)
# init_op = tf.initialize_all_variables()
#
# #with tf.Session('local') as sess:
# sess = tf.Session()
# sess.run(init_op)
#
# for step in range(num_steps):
#    _, centroid_values, assignment_values = sess.run([update_centroids,
#                                                     centroids,
#                                                     assignments])
# print("centroids")
# print(centroid_values)
#








#
# data = {"x": [], "y": [], "cluster": []}
# for i in range(len(assignment_values)):
#   data["x"].append(vector_values[i][0])
#   data["y"].append(vector_values[i][1])
#   data["cluster"].append(assignment_values[i])
# df = pd.DataFrame(data)
# sns.lmplot("x", "y", data=df,
#            fit_reg=False, size=7,
#            hue="cluster", legend=False)
# plt.show()
