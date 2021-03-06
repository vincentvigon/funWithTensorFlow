import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets("../MNIST_data/", one_hot=True)



def weightVariable(shape):
    initial=tf.truncated_normal(shape,stddev=0.1)
    return tf.Variable(initial)

def biasVariable(shape):
    initial=tf.constant(0.1,shape=shape)
    return tf.Variable(initial)



def conv2d(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')

def max_pool_2x2(x):
    return tf.nn.max_pool(x,ksize=[1,2,2,1],padding='SAME',strides=[1,2,2,1])


x=tf.placeholder("float",shape=[None,784])
y_=tf.placeholder("float",shape=[None,10])
x_image=tf.reshape(x,[-1,28,28,1])


W_conv1=weightVariable([5,5,1,32])
b_conv1=biasVariable([32])

h_conv1=tf.nn.relu(conv2d(x_image,W_conv1)+b_conv1)
h_pool1=max_pool_2x2(h_conv1)


W_conv2=weightVariable([5,5,32,64])
b_conv2=biasVariable([64])

h_conv2=tf.nn.relu(conv2d(h_pool1,W_conv2) + b_conv2)
h_pool2= max_pool_2x2(h_conv2)


''' fc=fully connected.   '''
W_fc1=weightVariable([7*7*64,1024])
b_fc1=biasVariable([1024])

h_pool2_flat=tf.reshape(h_pool2,[-1,7*7*64])
h_fc1=tf.nn.relu(tf.matmul(h_pool2_flat,W_fc1)+b_fc1)

keep_prob=tf.placeholder("float")
h_fc_drop=tf.nn.dropout(h_fc1,keep_prob)

W_fc2=weightVariable([1024,10])
b_fc2=biasVariable([10])

y_conv=tf.nn.softmax(tf.matmul(h_fc_drop,W_fc2)+b_fc2)




