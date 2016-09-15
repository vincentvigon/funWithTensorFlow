import tensorflow as tf

'''  le graphe de tensor flow'''
def step0():
    x=5
    y=5*x
    z=x*x
    res=y+z
    """ programmation classique: les opérations sont effectuées au fur et à mesure"""
    print("résultat avec calcul classique",res)

    """refaisons la même chose en tensorflow"""
    x=tf.constant(5)
    """comme x est un tenseur, y,z,et res seront aussi des tenseurs"""
    y=5*x
    z = x * x
    res = y + z
    """jusqu'ici il ne c'est rien passé.
    tensorflow va analyser les calculs à faire, dresser un arbre,  et les faire en parallèle.
    (x=5)
       |    \
    (y=5*x,z=x*x)
       |    /
    (res = y + z)
    Ex: les calculs (y=5*x,z=x*x) peuvent être parallélisé
    """
    sess = tf.Session()
    print("résultat avec calcul en arbre",sess.run(res))

    return


"""nous définissons une session pour toute la suite, créons une fonction qui évalue et affiche un tenseur de tensorFlow"""
sess = tf.Session()
def pr(nom,var):
    print(nom,"\n",sess.run(var))




'''créer un tenseur. Accéder à ses éléments. Connaître sa forme (shape)'''
def step1():
    tensor1=tf.constant([[1,2,1],[3,4,3]])
    grosTenseur=tf.constant([[[1,2,0],[3,4,0]],[[5,6,0],[7,8,0]]])


    pr("tensor1",tensor1)
    pr("tf.shape(tensor1)",tf.shape(tensor1))
    pr("tensor1[0,1]",tensor1[0,1])
    pr("tensor1[0,:]",tensor1[0,:])
    pr("grosTenseur",grosTenseur)
    pr("grosTenseur",tf.shape(grosTenseur))

    '''apprenez très vite à repérer les indices 0,1,2... dans les sorties consoles.
    Exemple1: l'indice 0 balaye les lignes, l'indice 1 balaye les colonnes
    tensor1
    [[1 2 1]
    [3 4 3]]

    Exemple2:
    grosTenseur
    [[[1 2 0]
     [3 4 0]]

    [[5 6 0]
      [7 8 0]]]

    voici comment sont les indices
    [i=0: [ j=0:[ k=0:1 k=1:2 k=2:0]
            j=1:[ k=0:3 k=1:4 k=2:0]]

    [i=1: [5 6 0]
          [7 8 0]]]

    '''

    return


step1()




''' Les types (float32, int32 ).
si on print un tenseur sans faire appel à sess.run, on a pas sa valeur, mais sa forme  et son type  '''
def step2():
    x=tf.constant([5,5])
    y=tf.constant([5.,5])
    print('x',x,'y',y)
    pr ('x',x)
    pr('y',y)

    '''attention aux erreurs de types: ci-dessous une erreur que vous ferez souvent : essayer de combiner (ici additionner) deux tenseurs de types différents.
    Lisez le message d'erreur. il est très explicite  '''
    #z=tf.add(x,y)
    #pr('z',z)



    return








"""opération élémentaire sur un tenseur"""
def step3():
    tensor1= tf.constant(1, shape=[3, 2])
    tensor2= tf.transpose(tensor1)
    tensor3= tf.reduce_sum(tensor1,1)
    tensor4= tf.mul(tensor1,3)
    tensor5=tensor1+tensor1

    pr("tensor1",tensor1)
    pr("tensor2",tensor2 )
    pr("tensor3",tensor3 )
    pr("tensor4",tensor4 )
    pr("tensor5",tensor5 )
    pr("tensor1",tensor1 )

    """vérifions que toutes ces opération n'ont pas affecté le tensor1"""
    pr('tensor1 pour la seconde fois',tensor1)
    """les opérations entre tenseur "tf.constant" implique systématiquement une copie  """

    return





"""comment utiliser des dimensions supplémentaires pour éviter des boucles (et ainsi rendre possible l'optimisation)
Attention: l'extension de dimension est difficile au début. Conseil : toujours écrire les indices comme ci-dessous
"""
def step4():
    size=3
    data=[]
    for i in range(size):
        data.append(i)

    """deux vecteurs 'lignes' """
    tensor1=tf.constant(data)
    tensor2=tf.constant(data)
    """tensor1Exp_ij=tensor1_j """
    tensor1Exp=tf.expand_dims(tensor1,0)
    """tensor2Exp_ij=tensor2_i """
    tensor2Exp=tf.expand_dims(tensor2,1)
    """
    tensor3_ij= tensor1Exp_ij + tensor2Exp_ij
              = tensor1_j + tensor2_i
    la fonction tf.add adapte les tailles, pour permettre une addition: C'est tous à fait naturel: nous le faisons aussi
    """
    tensor3=tf.add(tensor1Exp,tensor2Exp)

    """on peut additionner,multiplier, soustraire,  des tenseurs de dimensions différentes. Par défaut tf fait des expand_dims(,0). """
    tensor4=tf.constant([[1.,2,3],[4,5,6]])
    tensor5=tf.constant([10.,10,10])
    tensor6=tf.constant(100.)
    tensor7=tf.add(tensor4,tensor5)
    tensor8=tf.add(tensor6,tensor7)
    '''Cette convention est naturelle. On l'utilise par exemple lorsqu'on écrit  Sum_i (a_i - b )^2   '''



    pr("tensor1",tensor1 )
    pr("tensor2",tensor2 )
    pr("tensor1Exp",tensor1Exp )
    pr("tensor2Exp",tensor2Exp )
    pr("tf.shape(tensor1)",tf.shape(tensor1) )
    pr("tf.shape(tensor1Exp)",tf.shape(tensor1Exp) )
    pr("tensor3",tensor3 )
    pr("tensor7",tensor7)
    pr("tensor8",tensor8)


    return


"""question : pour tensorFlow, y a-t-il une différence entre un vecteur ligne de taille n et une matrice de taille 1*n ? """



"""extraction des coefficients diagonaux d'une matrice"""
def step5():

    """ on crée une liste d'indices"""
    tensor0=tf.range(0,6)
    tensor1 =tf.range(0,6)
    """on colle 2 tenseur selon l'axe 0"""
    tensor2 =tf.pack([tensor0,tensor1],0)
    tensor2bis = tf.pack([tensor0, tensor1], 1)

    tensor3 =tf.transpose(tensor2)
    """la grosse matrice dont on veut extraire les élément"""
    tensor4 =tf.reshape(tf.range(36),[6,6])
    """l'extraction: argument 1, la matrice, argument 2, les indices"""
    tensor5 =tf.gather_nd(tensor4,tensor3)

    pr("tensor0",tensor0 )
    pr("tensor1",tensor1 )
    pr("tensor2",tensor2 )
    pr("tensor2bis",tensor2bis )
    pr("tensor3",tensor3 )
    pr("tensor4",tensor4 )
    pr("tensor5",tensor5 )

    return




"""récupère toutes les valeurs <=1 dans un tenseur,puis en fait la moyenne
le résultat (=0) vous surprendra peut-être. Changez le tenseur0 en modifiant le  5 en 5.0. Quel se passe-t-il maintenant ? Expliquez"""
def step6():
    tensor0=tf.constant([[5,0,1],[1,0,3]])
    """on met des true là où il faut"""
    tensor1 =tf.less_equal(tensor0,1)
    """on récupère les indices où il y a des true"""
    tensor2 =tf.where(tensor1)
    tensor3 =tf.gather_nd(tensor0,tensor2)
    tensor4 =tf.reduce_mean(tensor3,0)

    pr("tensor0",tensor0 )
    pr("tensor1",tensor1 )
    pr("tensor2",tensor2 )
    pr("tensor3",tensor3 )
    pr("tensor4",tensor4 )

    return

"""quel est le point commun entre toutes les méthodes qui commencent par reduce_ ? """



"""extractions de sous-tenseurs et concaténation (comparez concat et pack)"""
def step7():

    """ concaténations de tenseurs """
    tensor0=tf.constant([[1,2,3],[4,5,6]])
    tensor1 =tf.constant([[7,8,9],[10,11,12]])
    tensor2 =tf.concat(0,[tensor0,tensor1])
    tensor3 =tf.concat(1,[tensor0,tensor1])
    """quel est le role du premier paramètre dans concat ? """

    """ extractions de sous matrices. Le second argument est le point de départ, le troisième la taille du bloc extrait """
    tensor4 =tf.slice(tensor2,[0,0],[1,2])
    tensor5 =tf.slice(tensor2,[1,0],[1,2])
    tensor6 =tf.slice(tensor2,[1,0],[1,-1])
    tensor7 =tf.slice(tensor2,[1,0],[-1,-1])
    """quel est l'effet du -1 ?"""



    """concaténons uns liste de tenseurs"""
    list=[]
    for i in range(3):
        list.append(tf.mul(tf.ones([1,2]),i))

    tensor8 =tf.concat(0,list)
    tensor9 =tf.concat(1,list)

    pr("tensor0",tensor0)
    pr("tensor1", tensor1)
    pr("tensor2", tensor2)
    pr("tensor3", tensor3)
    pr("tensor4", tensor4)
    pr("tensor5", tensor5)
    pr("tensor6", tensor6)
    pr("tensor7", tensor7)
    pr("tensor8", tensor8)
    pr("tensor9", tensor9)

    return



"""extractions de sous-tenseurs et concaténation, suite"""
def step8():

    """ concaténations de tenseurs """
    tensor0=tf.constant([[1,2,3],[4,5,6]])
    tensor1 =tf.constant([[7,8,9],[10,11,12]])
    tensor2 =tf.concat(0,[tensor0,tensor1])

    """extractions de lignes"""
    tensor3 =tf.gather(tensor2,1)
    tensor4 =tf.gather(tensor2,[1,2])

    pr("tensor0", tensor0)
    pr("tensor1", tensor1)
    pr("tensor2", tensor2)
    pr("tensor3", tensor3)
    pr("tensor4", tensor4)

    return



