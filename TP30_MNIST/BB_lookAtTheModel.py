import tensorflow as tf


x=tf.constant([[1.,2,3],[-1,-1,-1],[0,0,0]])
W=tf.constant([[1.,0],[1,0],[1,0]])
b=tf.Variable(tf.zeros([2.]))

mu=tf.matmul(x,W)+b
y= tf.nn.softmax(mu)

y_=tf.constant([[1.,0],[0,1],[1,0]])

cross_entropy=-tf.reduce_sum(y_*tf.log(y))

sess=tf.Session()
sess.run(tf.initialize_all_variables())

print(sess.run(tf.shape(x)))
print(sess.run(tf.shape(W)))
print(sess.run(tf.shape(b)))
print("mu\n",sess.run(mu))
print("y\n",sess.run(y))
print("y_\n",sess.run(y_))
print("crossEntropy\n",sess.run(cross_entropy))



