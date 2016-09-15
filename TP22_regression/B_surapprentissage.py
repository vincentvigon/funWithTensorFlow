import tensorflow as tf
import matplotlib.pyplot as plt
import random


random.seed(51)

sess=tf.Session()
def pr(st,ob): print(st+"\n",sess.run(ob))

def createDataWithSquare(nbData:int):
    x_data=[]
    for i in range(nbData):
        x_data.append(random.random())

    x_data.sort()

    y_data=[]
    for i in range(nbData):
        y_data.append(x_data[i]*0.1+ x_data[i]*x_data[i]*0.8 +0.3 + random.gauss(0,0.01))

    return x_data,y_data



def step1():


    W = tf.Variable([1.,0.5])
    b = tf.Variable(1.)

    x_data,y_data=[0.,1,2,0],[0.,0,0,0]

    x1=tf.constant(x_data)
    x2=x1*x1
    x=tf.pack([x1,x2],1)


    """
    Pour mieux comprendre on peut rajouter
    W=tf.expand_dims(W,0)
    qui construit
    W_ij=W_j
    mais nous avons vu que l'extention en le premier indice est facultative
    """
    #y_i = sum_j W_j* x_ij + b
    y= tf.reduce_sum(tf.mul(W,x),1)+b# attention, ne  pas mettre le b à l'interieur du reduce_sum. Il sera compter plusieurs fois
    loss = tf.reduce_mean(tf.square(y - y_data))

    sess.run(tf.initialize_all_variables())
    pr("x1",x1)
    pr("x2",x2)
    pr("x",x)
    pr("W",W)
    pr("y",y)
    pr("loss",loss)
    return


def step2():



    W = tf.Variable(tf.random_uniform([2], -1.0, 1.0))
    b = tf.Variable(tf.zeros([1]))

    x_data, y_data = createDataWithSquare(100)

    x1 = tf.constant(x_data)
    x2 = x1 * x1
    x = tf.pack([x1, x2], 1)

    y = tf.reduce_sum(tf.mul(W, x), 1)+b
    loss = tf.reduce_mean(tf.square(y - y_data))
    train = tf.train.GradientDescentOptimizer(0.5).minimize(loss)


    sess.run(tf.initialize_all_variables())

    for step in range(401):
        sess.run(train)
        if step % 20 == 0:
            print(step, sess.run(W), sess.run(b),sess.run(loss))

    plt.plot(x_data,y_data,'ro')
    plt.plot(x_data,sess.run(y))
    plt.show()

    return



step2()




# loss = tf.reduce_mean(tf.square(y - y_data))
# train = tf.train.GradientDescentOptimizer(0.5).minimize(loss)
#
# init = tf.initialize_all_variables()
#
# with tf.Session() as sess:
#     sess.run(init)
#
#     for step in range(201):
#         sess.run(train)
#         if step % 20 == 0:
#             print(step, sess.run(W), sess.run(b))
#
#     plt.plot(x_data,y_data,'ro')
#     plt.plot(x_data,sess.run(y))
#     plt.show()
#
#

sess.close()