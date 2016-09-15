import tensorflow as tf
import matplotlib.pyplot as plt
import random
import math


random.seed(51)

sess=tf.Session()
def pr(st,ob): print(st+"\n",sess.run(ob))

def createDataWithSquare(nbData:int):
    x_data=[]
    for i in range(nbData):
        x_data.append(i/nbData)



    y_data=[]
    for i in range(nbData):
        y_data.append(x_data[i]*0.1+ math.sin(3*x_data[i])*0.8  +0.3+random.normalvariate(0,0.2) )

    return x_data,y_data


def step1():

    maxPower=2

    W = tf.Variable([1., 0.5])
    b = tf.Variable(1.)

    x_data, y_data = [0., 1, 2, 0], [0., 0, 0, 0]


    xi=[]
    for i in range(1,maxPower+1):
        xi.append(tf.pow(x_data,i))

    x=tf.pack(xi,1)


    #y_i = sum_j W_j* x_ij + b
    y= tf.reduce_sum(tf.mul(W,x) ,1)+b
    loss = tf.reduce_mean(tf.square(y - y_data))

    sess.run(tf.initialize_all_variables())
    pr("x",x)
    # pr("W",W)
    pr("y",y)
    pr("loss",loss)

    return

""" données pour faire apparaître le sur apprentissage
stdVar=0.2, maxPower=4, nbData=7
"""
def step2():

    maxPower=4

    W = tf.Variable(tf.random_uniform([maxPower], -0.1, 0.1))
    b = tf.Variable(tf.zeros([1]))

    x_data,y_data=createDataWithSquare(7)

    xi=[]
    for i in range(1,maxPower+1):
        xi.append(tf.pow(x_data,i))

    x=tf.pack(xi,1)


    #y_i = sum_j W_j* x_ij + b
    y= tf.reduce_sum(tf.mul(W,x),1)+b
    loss = tf.reduce_mean(tf.square(y - y_data))

    train = tf.train.AdamOptimizer(0.1).minimize(loss)

    sess.run(tf.initialize_all_variables())

    oldLoss =1
    for step in range(401):
        sess.run(train)
        if step % 20 == 0:
            lossNow=sess.run(loss)
            print(step,sess.run(W), sess.run(b),round(lossNow/oldLoss,2),lossNow)
            oldLoss=lossNow

    plt.plot(x_data, y_data, 'ro')
    plt.plot(x_data, sess.run(y))
    plt.show()

    return


step2()