import tensorflow as tf


def conv2d(x,W):
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')


sess = tf.InteractiveSession()
def pr(leg,a):
    print(leg+"\n",sess.run(a))


'''une image x convoler par un noyau W'''
def exo1():

    size = 5
    aa = []
    for i in range(size * size):
        aa.append(i * 1.)

    a = tf.constant(aa)
    b = tf.reshape(a, [size, size])

    '''créons une image'''
    x = tf.reshape(b, [1, size, size, 1])
    pr('x shape',tf.shape(x))
    pr('x', x[0, :, :, 0])

    ''' créons un noyau'''
    W = tf.constant([[1., 1], [1, 1]])
    W = tf.reshape(W, [2, 2, 1, 1])
    pr('W shape',tf.shape(W))
    pr('W',W[:,:,0,0])

    conv=conv2d(x,W)
    pr ('conv shape',tf.shape(conv))
    pr('conv',conv[0,:,:,0])


'''une image à 2 channels convoler par un noyau à 2 in_channels -> une image à 1 channel'''
def exo2():

    size = 5
    aa = []
    for i in range(size * size):
        aa.append(i * 1.)

    a = tf.constant(aa)
    b = tf.reshape(a, [size, size])

    '''créons une image à 2 channels'''
    x0 = tf.reshape(b, [1, size, size, 1])
    x1 = tf.reshape(tf.mul(b,2), [1, size, size, 1])
    x = tf.concat(3,[x0,x1])
    pr('x shape',tf.shape(x))
    pr('x0', x[0, :, :, 0])
    pr('x1', x[0, :, :, 1])

    ''' créons un noyaux à deux in_channels'''
    W0 = tf.constant([[1., 1], [1, 1]])
    W0 = tf.reshape(W0, [2, 2, 1, 1])
    W1 = tf.mul(W0,0.5)
    W= tf.concat(2,[W0,W1])
    pr('W shape',tf.shape(W))
    pr('W0',W[:,:,0,0])
    pr('W1',W[:,:,1,0])

    conv=conv2d(x,W)
    pr ('conv shape',tf.shape(conv))
    pr('conv',conv[0,:,:,0])

    return


'''une image x à 1 channel convoler par un noyau W ayant 2 out_channels -> une image à 2 channels'''
def exo3():

    size = 5
    aa = []
    for i in range(size * size):
        aa.append(i * 1.)

    a = tf.constant(aa)
    b = tf.reshape(a, [size, size])

    '''créons une image'''
    x = tf.reshape(b, [1, size, size, 1])
    pr('x shape',tf.shape(x))
    pr('x', x[0, :, :, 0])

    ''' créons un noyau ayant 2 out_channels'''
    W = tf.constant([[1., 1], [1, 1]])
    W0 = tf.reshape(W, [2, 2, 1, 1])
    W1 = tf.reshape(tf.mul(W,2), [2, 2, 1, 1])
    W= tf.concat(3,[W0,W1])

    pr('W shape',tf.shape(W))
    pr('W_out0',W[:,:,0,0])
    pr('W_out1',W[:,:,0,1])


    conv=conv2d(x,W)
    pr ('conv shape',tf.shape(conv))
    pr('conv_out0',conv[0,:,:,0])
    pr('conv_out1',conv[0,:,:,1])


    return


exo3()

