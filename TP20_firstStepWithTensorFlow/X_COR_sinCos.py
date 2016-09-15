import tensorflow as tf
import math

sess = tf.Session()
def pr(leg,a):
    print(leg+"\n",sess.run(a))



nbFreq=2
nbStep=4
epsilon=1./nbStep

x=tf.lin_space(0.,1.,nbStep)
y=x*x-x+1

xSinCosList=[x*1/math.sqrt(2)]
for i in range(1,nbFreq+1):
    xSinCosList.append(tf.sin(i*2*math.pi*x))
    xSinCosList.append(tf.cos(i*2*math.pi*x))

sinCos=tf.pack(xSinCosList)







pr("x",x)
pr("sinCos",sinCos)