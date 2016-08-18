import tensorflow as tf


'''créer un tenseur. Accéder à ses éléments'''
def ex0():
    tensor1=tf.constant([[1,2,1],[3,4,3]])
    init = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init)
    print(sess.run(tensor1))
    print(tf.shape(tensor1))
    print(sess.run(tensor1[0,1]))
    print(sess.run(tensor1[0,:]))
    return




"""opération élémentaire sur un tenseur"""
def ex1():
    tensor1= tf.constant(1, shape=[3, 2])
    tensor2= tf.transpose(tensor1)
    tensor3= tf.reduce_sum(tensor1,1)
    tensor4= tf.mul(tensor1,3)
    tensor5=tensor1+tensor1

    init = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init)
    print('tensor1\n',sess.run(tensor1))
    print('tensor2\n',sess.run(tensor2))
    print('tensor3\n',sess.run(tensor3))
    print('tensor4\n',sess.run(tensor4))
    print('tensor5\n',sess.run(tensor5))

    """vérifions que toutes ces opération n'ont pas affecté le tensor1"""
    print('tensor1\n',sess.run(tensor1))


    return


"""comment utiliser des dimensions supplémentaires pour éviter des boucles (et ainsi rendre possible la parallélisation)"""
def ex2():
    size=3
    data=[]
    for i in range(size):
        data.append(i)

    tensor1=tf.constant(data)
    tensor2=tf.constant(data)
    tensor1Exp=tf.expand_dims(tensor1,0)
    tensor2Exp=tf.expand_dims(tensor2,1)
    """la fonction add va adapter les tailles, en répétant les données, pour permettre une addition"""
    tensor3=tf.add(tensor1Exp,tensor2Exp)


    init = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init)
    print('tensor1\n', sess.run(tensor1))
    print('tensor2\n', sess.run(tensor2))
    print('tensor1Exp\n', sess.run(tensor1Exp))
    print('tensor2Exp\n', sess.run(tensor2Exp))
    print('tensor1 shape\n',sess.run(tf.shape(tensor1)))
    print('tensor1Exp shape\n',sess.run(tf.shape(tensor1Exp)))
    print('tensor3\n', sess.run(tensor3))
    return

"""question : pour tensorFlow, y a-t-il une différence entre un vecteur ligne de taille n et une matrice de taille 1*n ? """



"""extraction des coefficients diagonaux d'une matrice"""
def ex3():
    """pour évider d'avoir à numéroter nos tenseurs à la main, on créer une liste de tenseurs"""
    tensors=[]

    """ on crée une liste d'indices"""
    tensors.append(tf.range(0,6))#tensor0
    tensors.append(tf.range(0,6))#tensor1
    tensors.append(tf.pack([tensors[0],tensors[1]]))#tensor2
    tensors.append(tf.transpose(tensors[2]))#tensor3
    """la grosse matrice dont on veut extraire les élément"""
    tensors.append(tf.reshape(tf.range(36),[6,6]))#tensor4
    """l'extraction: argument 1, la matrice, argument 2, les indices"""
    tensors.append(tf.gather_nd(tensors[4],tensors[3]))#tensor5


    init = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init)
    i=0
    for tensor in tensors:
        print("tensor"+str(i)+"\n",sess.run(tensor))
        i+=1

    return


"""récupère toutes les valeurs <=1 dans un tenseur,puis en fait la moyenne
le résultat (=0) vous surprendra peut-être. Changez le tenseur0 en modifiant le  5 en 5.0. Quel se passe-t-il maintenant ? Expliquez"""
def ex4():
    tensors = []

    tensors.append(tf.constant([[5,0,1],[1,0,3]]))  # 0
    """on met des true là où il faut"""
    tensors.append(tf.less_equal(tensors[0],1))  # 1
    """on récupère les indices où il y a des true"""
    tensors.append(tf.where(tensors[1])) #2
    tensors.append(tf.gather_nd(tensors[0],tensors[2])) #3
    tensors.append(tf.reduce_mean(tensors[3],0))#4

    init = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init)
    i = 0
    for tensor in tensors:
        print("tensor" + str(i) + "\n", sess.run(tensor))
        i += 1

    return

"""quel est le point commun entre toutes les méthodes qui commencent par reduce_ ? """


"""extractions de sous-tenseurs et concaténation"""
def ex5():
    tensors = []

    """ concaténations de tenseurs """
    tensors.append(tf.constant([[1,2,3],[4,5,6]]))  # 0
    tensors.append(tf.constant([[7,8,9],[10,11,12]]))  # 1
    tensors.append(tf.concat(0,[tensors[0],tensors[1]])) #2
    tensors.append(tf.concat(1,[tensors[0],tensors[1]])) #3
    """quel est le role du premier paramètre dans concat ? """

    """ extractions de sous matrices. Le second argument est le point de départ, le troisième la taille du bloc extrait """
    tensors.append(tf.slice(tensors[2],[0,0],[1,2]))  # 4
    tensors.append(tf.slice(tensors[2],[1,0],[1,2]))  # 5
    tensors.append(tf.slice(tensors[2],[1,0],[1,-1]))  # 6
    tensors.append(tf.slice(tensors[2],[1,0],[-1,-1]))  # 7
    """quel est l'effet du -1 ?"""



    """concaténons uns liste de tenseurs"""
    list=[]
    for i in range(3):
        list.append(tf.mul(tf.ones([1,2]),i))
    tensors.append(tf.concat(0,list)) #8
    tensors.append(tf.concat(1,list)) #9


    init = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init)
    i = 0
    for tensor in tensors:
        print("tensor" + str(i) + "\n", sess.run(tensor))
        i += 1

    return



"""extractions de sous-tenseurs et concaténation, suite"""
def ex6():
    tensors = []

    """ concaténations de tenseurs """
    tensors.append(tf.constant([[1,2,3],[4,5,6]]))  # 0
    tensors.append(tf.constant([[7,8,9],[10,11,12]]))  # 1
    tensors.append(tf.concat(0,[tensors[0],tensors[1]])) #2

    """extractions de lignes"""
    tensors.append(tf.gather(tensors[2],1))#3
    tensors.append(tf.gather(tensors[2],[1,2]))#4


    init = tf.initialize_all_variables()
    sess = tf.Session()
    sess.run(init)
    i = 0
    for tensor in tensors:
        print("tensor" + str(i) + "\n", sess.run(tensor))
        i += 1

    return


''' placehoder: une place mémoire préparée pour entrer les données  '''
def ex7():
    x=tf.placeholder("float",[None,2])
    '''attention aux erreurs de types: remplacez 1. par A dans la matrice ci-dessous pour en voir une. Lisez le message d'erreur'''
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

    return


"""et voici l'exécution. Changez le numéro"""
ex7()