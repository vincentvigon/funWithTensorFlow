

import tensorflow as tf
import TP25_winePrice.E_wineHelper as wine


sess = tf.Session()
def pr(leg,a):
    print(leg+"\n",sess.run(a))



# def step10():
#
#     k=tf.Variable(100.)
#
#     dataX=tf.placeholder("float",shape=[None,2])
#     dataY=tf.placeholder("float",shape=[None])
#     X=tf.placeholder("float",shape=[None,2])
#     Y=tf.placeholder("float",shape=[None])
#
#
#     allPairwiseDiff = tf.sub(tf.expand_dims(dataX, 0), tf.expand_dims(X, 1))
#     allDist = tf.reduce_sum(tf.square(allPairwiseDiff), 2)
#     weights = tf.exp(-tf.square(allDist / k))
#     totalWeight = 1 / tf.reduce_sum(weights, 1)
#     weightedDataY = tf.mul(weights, tf.expand_dims(dataY, 0))
#     weightedDataYNor = tf.mul(weightedDataY, tf.expand_dims(totalWeight, 1))
#     meanPrice = tf.reduce_sum(weightedDataYNor, 1)
#
#     error = tf.reduce_mean(tf.abs(tf.sub(meanPrice, Y)))
#     optimizer=tf.train.GradientDescentOptimizer(5)
#     train=optimizer.minimize(error)
#
#
#     sess.run(tf.initialize_all_variables())
#
#
#     for i in range(5):
#         dataXbatch,dataYbatch=wine.createWineData(15)
#         Xbatch,Ybatch=wine.createWineData(20)
#
#         sess.run(error,feed_dict={dataX:dataXbatch,dataY:dataYbatch,X:Xbatch,Y:Ybatch})
#         sess.run(train)
#
#
#
#     return


# def step10():
#
#
#     dataX=tf.placeholder("float",shape=[None,2])
#     #dataY=tf.placeholder("float",shape=[None])
#
#     y=tf.square(dataX)
#
#
#     sess.run(tf.initialize_all_variables())
#
#
#     dataXBatch,dataYBatch=wine.createWineData(15)
#
#     print(dataXBatch)
#
#     sess.run(y,feed_dict={dataX:dataXBatch})
#
#
#
#     return






def step10():

    k=tf.Variable(500.)

    dataX=tf.placeholder("float",shape=[None,2])
    dataY=tf.placeholder("float",shape=[None])
    X=tf.placeholder("float",shape=[None,2])
    Y=tf.placeholder("float",shape=[None])


    allPairwiseDiff = tf.sub(tf.expand_dims(dataX, 0), tf.expand_dims(X, 1))
    allDist = tf.reduce_sum(tf.square(allPairwiseDiff), 2)
    weights = tf.exp(-tf.square(allDist / k))
    totalWeight = 1 / tf.reduce_sum(weights, 1)
    weightedDataY = tf.mul(weights, tf.expand_dims(dataY, 0))
    weightedDataYNor = tf.mul(weightedDataY, tf.expand_dims(totalWeight, 1))
    meanPrice = tf.reduce_sum(weightedDataYNor, 1)

    error = tf.reduce_mean(tf.square(tf.sub(meanPrice, Y)))

    optimizer=tf.train.GradientDescentOptimizer(10.)
    train=optimizer.minimize(error)


    sess.run(tf.initialize_all_variables())

    for i in range(60):
        dataXbatch,dataYbatch=wine.createWineData(15)
        Xbatch,Ybatch=wine.createWineData(20)
        print('error',sess.run(error,feed_dict={dataX:dataXbatch,dataY:dataYbatch,X:Xbatch,Y:Ybatch}))
        sess.run(train,feed_dict={dataX:dataXbatch,dataY:dataYbatch,X:Xbatch,Y:Ybatch})
        print('k',sess.run(k,feed_dict={dataX:dataXbatch,dataY:dataYbatch,X:Xbatch,Y:Ybatch}))


    return




def step11():

    k=tf.Variable(500.)

    dataX=tf.placeholder("float",shape=[None,2])
    dataY=tf.placeholder("float",shape=[None])
    X=tf.placeholder("float",shape=[None,2])
    Y=tf.placeholder("float",shape=[None])




    error = winePrediction(dataX,dataY,X,Y,k)

    optimizer=tf.train.GradientDescentOptimizer(10.)
    train=optimizer.minimize(error)


    sess.run(tf.initialize_all_variables())

    for i in range(60):
        dataXbatch,dataYbatch=wine.createWineData(15)
        Xbatch,Ybatch=wine.createWineData(20)
        print('error',sess.run(error,feed_dict={dataX:dataXbatch,dataY:dataYbatch,X:Xbatch,Y:Ybatch}))
        sess.run(train,feed_dict={dataX:dataXbatch,dataY:dataYbatch,X:Xbatch,Y:Ybatch})
        print('k',sess.run(k,feed_dict={dataX:dataXbatch,dataY:dataYbatch,X:Xbatch,Y:Ybatch}))

    return

step11()
