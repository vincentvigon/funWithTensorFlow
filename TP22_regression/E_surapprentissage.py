import tensorflow as tf
import matplotlib.pyplot as plt
import random
import math


random.seed(51)

sess=tf.Session()
def pr(st,ob): print(st+"\n",sess.run(ob))

def createDataWithSquare(nbData:int):
    # x_data=[]
    # for i in range(nbData):
    #     x_data.append(i/nbData)
    x_data = []
    for i in range(nbData):
        x_data.append(random.random())

    x_data.sort()

    y_data=[]
    for i in range(nbData):
        y_data.append(x_data[i]*0.1+ math.sin(3*x_data[i])*0.8  +0.3+random.normalvariate(0,0.1) )

    return x_data,y_data


def step1():

    freqMax=2

    x_data = [0.,0.2,0.4,0.6,0.8,1]
    u_data = [0.,0,0,0,0,0]

    xi=[]
    xTensor=tf.constant(x_data)
    for i in range(1,freqMax+1):
        xi.append(tf.sin(2.*math.pi*i*xTensor))
        xi.append(tf.cos(2.*math.pi*xTensor))
    x=tf.pack(xi,1)

    W = tf.Variable(tf.ones([freqMax * 2]))
    b = tf.Variable(1.)

    #y_i = sum_j W_j* x_ij + b
    y= tf.reduce_sum(tf.mul(W,x) ,1)+b
    loss = tf.reduce_mean(tf.square(y - u_data))

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

    freqMax = 4


    x=tf.placeholder("float",[None])
    u=tf.placeholder("float",[None])


    xi = []
    for i in range(1, freqMax + 1):
        xi.append(tf.sin(2. * math.pi * i * x))
        xi.append(tf.cos(2. * math.pi * x))
    xSinCos = tf.pack(xi, 1)

    W = tf.Variable(tf.ones([freqMax * 2]))
    b = tf.Variable(1.)

    #y_i = sum_j W_j* x_ij + b
    y= tf.reduce_sum(tf.mul(W,xSinCos),1)+b
    loss = tf.reduce_mean(tf.square(y - u))

    train = tf.train.AdamOptimizer(0.1).minimize(loss)

    sess.run(tf.initialize_all_variables())

    x_train, u_train = createDataWithSquare(15)
    feedTrain={x:x_train,u:u_train}

    oldLoss =1
    for step in range(201):
        sess.run(train,feed_dict=feedTrain)
        if step % 20 == 0:
            lossNow=sess.run(loss,feed_dict=feedTrain)
            print(round(lossNow/oldLoss,2),"erreur d'ajustement",lossNow)
            oldLoss=lossNow

    f, windows = plt.subplots(2, sharex=True)

    windows[0].plot(x_train, u_train, 'ro')
    windows[0].plot(x_train, sess.run(y,feed_dict=feedTrain))
    windows[0].set_title('train')



    x_test,u_test=createDataWithSquare(100)
    feedTest={x:x_test,u:u_test}

    windows[1].plot(x_test, u_test, 'ro')
    windows[1].plot(x_test, sess.run(y, feed_dict=feedTest))
    windows[1].set_title('test')

    print( "erreur de prévision", sess.run(loss,feed_dict=feedTest))


    plt.show()

    return

"""
 15 données d'apprentissage
 100 données de test


 avec freqMax = 1
 erreur d'ajustement 0.0036944
 erreur de prévision 0.0175338

 avec freqMax = 2
 erreur d'ajustement 0.00243561
 erreur de prévision 0.0171062


 avec freqMax = 4
 erreur d'ajustement 0.00218764
 erreur de prévision 0.0170165



 avec freqMax = 6
 erreur d'ajustement 0.0011404
 erreur de prévision 0.0204454

 avec freqMax = 8
 erreur d'ajustement 0.00108702
 erreur de prévision 0.0209158


 avec freqMax = 8, il faut augmenter le nombre d'itération à 601
 erreur d'ajustement 0.000986137
 erreur de prévision 6.68978


 """


step2()