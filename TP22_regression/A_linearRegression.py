import tensorflow as tf
import matplotlib.pyplot as plt
import random

random.seed(100)



def createData(nbData:int):
    x_data=[]
    for i in range(nbData):
        x_data.append(random.random())

    '''ordonnons les données (uniquement pour l'affichage à la fin)'''
    x_data.sort()

    y_data=[]
    '''ordonnées aléatoires'''
    for i in range(nbData):
        y_data.append(x_data[i]*0.1 +0.3 + random.gauss(0,0.01))

    return x_data,y_data


"""maintenant on oublie que l'on connaît les coefficients 0.1 et 0.3.
on va les retrouver en minimisant une erreur quadratique"""


'''W est pris aléatoire dans [-1,1], b est pris égal à 0
 W et b sont des variables, càd qu'ils vont changer de valeur au cours du programme'''
W = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
b = tf.Variable(tf.zeros([1]))

x_data,y_data=createData(100)


'''Voici le modèle : y est une fonction affine de x_data'''
y= W*x_data + b


'''on définit la fonction de coup'''
loss = tf.reduce_mean(tf.square(y - y_data))
'''l'oject optimizer représente l'algo de descente de gradient, avec un pas de 0.5 (ni trop grand, ni trop petit)'''
optimizer = tf.train.GradientDescentOptimizer(0.5)
"""l'objet train doit minimise la fonction loss"""
train = optimizer.minimize(loss)
"""plus précisément train va approcher les arguments W et b qui minimisent la fonctionnelle (W,b) ---> (y_data - W*x_data+b )^2
 W0 et b0 sont initialisés arbitrairement (cf. au-dessus). W_n+1 et b_n+1 sont déduits de W_n et b_n en suivant la plus
 grande pente de la fonctionnelle"""


"""l'objet qui initialisera toutes les variables. A lancer en tout premier"""
init = tf.initialize_all_variables()
"""la session de calcul"""
sess = tf.Session()
"""cette session lance l'initialisation"""
sess.run(init)

"""cette session fait tourner le 'train'  toutes les 20 fois on affiche les variables"""
for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(W), sess.run(b))


plt.plot(x_data,y_data,'ro')
''' ne pas oublié "sess.run" pour avoir les valeurs de y '''
plt.plot(x_data,sess.run(y))
plt.show()


''' exercice 1: créez des donnée liée par un polynômes.
ex: y_data=2*x_data^2 -3*x_data + 4
oubliez les coefficients ici (2,-3,4) et retrouvez les.

exercice 2 : faite une régression linéaire de dimension supérieure. Par exemple, vos données auront la tête
y_data=  beta_0 + beta_1 * x1_data + beta_2 * x2_data
où les coef beta_i sont inconnus, et les x1_data et x2_data sont des variables 'explicatives' données.
  '''
