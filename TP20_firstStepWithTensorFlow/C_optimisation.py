import tensorflow as tf


sess = tf.Session()
def pr(leg,a):
    print(leg+"\n",sess.run(a))


"""l'algo de descente du gradient est l'algo d'optimisation le plus populaire.
 Un dessin suffit à le comprendre (réclamez un dessin si j'oublie).
 """
def step1():
    W=tf.Variable(100.)
    y=tf.square(W)

    '''l'oject optimizer représente l'algo de descente de gradient, avec un pas donné (essayez avec 0.1,0.2,0.5,1,2)'''
    optimizer = tf.train.GradientDescentOptimizer(0.1)
    """l'objet train doit minimise la fonction loss"""
    minimizer = optimizer.minimize(y)

    sess.run(tf.initialize_all_variables())

    pr("W",W)
    print("on commence l'optimisation\n")

    for k in range(5):
        sess.run(minimizer)
        pr("W",W)

"""
QUESTION: que se passe-t-il si on prend un learning_rate de 1 ou 2 ou 100 dans tf.train.GradientDescentOptimizer(learning_rate) ?
Expliquez le phénomène dans votre rapport, avec, par exemple, un schéma.
Remplacez tf.train.GradientDescentOptimizer par tf.train.AdamOptimizer et remarquez combien l'algo converge pour une plus grande plage de learning_rate
"""

"""faisons la même chose à la main"""
def step1bis():
    W=tf.Variable(100.)
    y=tf.square(W)

    sess.run(tf.initialize_all_variables())

    for k in range(5):
        gradient = tf.gradients(y, W)[0]
        pr('gradient', gradient)

        sess.run(W.assign(W-gradient*0.1))
        pr('W',W)

''' Puisque tensor flow connaît toutes les opérations formellement, il est capable de calculer des gradients de manière formelles.
Ainsi les valeurs du gradient sont "exactes" (à la précision des float prêt).  '''


"""descente du gradient en dimension 2"""
def step2():
    W = tf.Variable([100.,100])
    y = tf.reduce_sum(tf.square(W))

    '''l'oject optimizer représente l'algo de descente de gradient, avec un pas donné (essayez avec 0.1,0.2,0.5,1,2)'''
    optimizer = tf.train.GradientDescentOptimizer(0.2)
    """l'objet train doit minimise la fonction loss"""
    train = optimizer.minimize(y)
    """plus précisément train va approcher les arguments W et b qui minimisent la fonctionnelle (W,b) ---> (y_data - W*x_data+b )^2
     W0 et b0 sont initialisés arbitrairement (cf. au-dessus). W_n+1 et b_n+1 sont déduits de W_n et b_n en suivant la plus
     grande pente de la fonctionnelle"""

    sess.run(tf.initialize_all_variables())

    gradient = tf.gradients(y, W)

    pr("W", W)
    pr('gradient', gradient)
    print("on commence l'optimisation\n")

    for k in range(5):
        sess.run(train)
        pr("Wk", W)
        pr('gradient', gradient)



