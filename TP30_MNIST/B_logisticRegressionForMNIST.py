import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("../MNIST_data/", one_hot=True)

x=tf.placeholder("float",[None,784])
W=tf.Variable(tf.zeros([784,10]))
b=tf.Variable(tf.zeros([10]))


y= tf.nn.softmax(tf.matmul(x,W)+b)
y_ = tf.placeholder("float", [None, 10])


cross_entropy=-tf.reduce_sum(y_*tf.log(y))
train_step=tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

sess=tf.Session()
sess.run((tf.initialize_all_variables()))

for i in range(1):
    batch_xs,batch_ys=mnist.train.next_batch(100)
    sess.run(train_step,feed_dict={x:batch_xs,y_:batch_ys})
    correct_prediction=tf.equal(tf.arg_max(y,1),tf.arg_max(y_,1))#renvoir des true/false
    a=tf.cast(correct_prediction,"float")
    #print(sess.run(tf.arg_max(y,1),feed_dict={x:mnist.test.images,y_:mnist.test.labels}))
    accuracy=tf.reduce_mean(tf.cast(correct_prediction,"float"))#que l'on transforme en 1/0
    print(sess.run(accuracy,feed_dict={x:mnist.test.images,y_:mnist.test.labels}))



