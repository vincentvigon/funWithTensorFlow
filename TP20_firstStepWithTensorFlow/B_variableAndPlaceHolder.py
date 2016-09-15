import tensorflow as tf


sess = tf.Session()
def pr(leg,a):
    print(leg+"\n",sess.run(a))


""" Les variables : leur valeur peut changer au cours de l'exécution, et toutes les fonctions qui dépendent d'elles changent aussi."""
def step0():
    W = tf.Variable(0)
    """y est une fonction d'une variable (elle varie donc aussi)"""
    y = tf.square(W)

    """les variables doivent être initialisée initialisation"""
    sess.run(tf.initialize_all_variables())
    for i in range(1,4):
        assignation=W.assign(i)
        sess.run(assignation)
        pr("W",W)
        pr("y=W^2",y)
    return


""" remarquez que tensorFlow est une sorte de langage de calcul formel. Il mémorise les liens entre les tenseurs.
 Dans un langage  classique (ex: python), que donnerait ? :
 W=0
 y=W*W
 for i in range(1,4):
        W=i
        pr("W",W)
        pr("y=W^2",y)
    return
 """



""" Rappelons que les constantes ne changent pas !"""
def step0bis():

    W=tf.constant(0)
    y=tf.square(W)

    for i in range(1,4):
        W=tf.constant(i) #on créé ici une nouvelle constante qui n'a rien à voir avec le W précédent, donc rien à voir avec y
        pr("W",W)
        pr("y=W^2",y)
    return




''' placehoder: une place mémoire préparée pour  les entrées de données. On n'est pas obligé de les initialiser, ni même de les
  dimensionner précisément'''
def step8():
    x=tf.placeholder("float",[None,2])
    x2 = tf.mul(x, 2)
    W = tf.constant([[1., 2], [3, 4]])
    y = tf.matmul(x2, W)

    init = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init)


    x_data = [[0., 1],[2,4],[0,0]]
    print(sess.run(y, feed_dict={x: x_data}))
    x_data = [[0., 1], [2, 4]]
    print(sess.run(y, feed_dict={x: x_data}))
    """ attention, x est le place holder, et x_data est la liste qui remplie cette place. Ne pas leur donner le même nom ! """

    """ Contrairement aux variable, la session ne mémorise jamais la valeur d'un placeholder, à chaque sess.run, il faut
      re-rentrer un dico via feed_dict= dico. Par exemple ci-dessous, c'est une erreur (lisez le message) """
    #print(sess.run(x2))


    return

