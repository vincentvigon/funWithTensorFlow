import tensorflow as tf
import random
import matplotlib.pyplot as plt



def generateData(nb:int):
    x_data=[]
    y_data=[]
    for i in range(nb):
        x=[random.random(),random.random()]
        x_data.append(x)
        if x[0]<x[1]+random.gauss(0,0.1): y_data.append([0.,1.])
        else: y_data.append([1.,0.])
    return x_data,y_data


def plotData(_x, _y):

    zerosX=[]
    zerosY=[]
    onesX=[]
    onesY=[]
    for i in range(len(_x)):
        if _y[i]==0:
            zerosX.append(_x[i][0])
            zerosY.append(_x[i][1])
        else :
            onesX.append(_x[i][0])
            onesY.append(_x[i][1])
    plt.plot(zerosX,zerosY,'ro')
    plt.plot(onesX,onesY,'g^')

    plt.show()



x=tf.placeholder("float",[None,2])
W=tf.Variable(tf.zeros([2,2]))
b=tf.Variable(tf.zeros([2]))



y= tf.nn.softmax(tf.matmul(x,W)+b)
y_ = tf.placeholder("float", [None, 2])


#cross_entropy=tf.reduce_sum(y_*(1-y))
cross_entropy=-tf.reduce_sum(y_*tf.log(y))


train_step=tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

sess=tf.Session()
sess.run((tf.initialize_all_variables()))

for i in range(100):
    batch_xs,batch_ys=generateData(30)
    sess.run(train_step,feed_dict={x:batch_xs,y_:batch_ys})

    xs_test, ys_test = generateData(30)
    correct_prediction=tf.equal(tf.arg_max(y,1),tf.arg_max(y_,1))
    accuracy=tf.reduce_mean(tf.cast(correct_prediction,"float"))
    print(sess.run(accuracy,feed_dict={x:xs_test,y_:ys_test }))





#plotData(x,y)

