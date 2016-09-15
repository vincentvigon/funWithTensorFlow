import random
import math
import tensorflow as tf
import matplotlib.pyplot as plt

'''pour avoir toujours les mêmes sorties'''
random.seed(10)



def winePrice(rating, age):
    peakAge=rating-50
    price=rating/2
    if age>peakAge:
        price*=(5-(age-peakAge))
    else:
        price*=5*(age+1)/peakAge
    if price<0: price=5*random.random()
    return price


def createWineData(nbData):
    inputs=[]
    prices=[]

    for i in range(nbData):
        rating=random.random()*50+50
        age=random.random()*50

        price=winePrice(rating,age)
        price*=random.random()*0.4+0.8

        inputs.append([rating,age])
        prices.append(price)

    return inputs,prices






def plotWinePrices(dataX, dataY):
    x0=[v[0] for v in dataX]
    x1=[v[1] for v in dataX]

    labels = ['{0}'.format(int(i)) for i in dataY]
    plt.subplots_adjust(bottom = 0.1)
    plt.scatter(
        x0,
        x1,
        marker = 'o',
        cmap = plt.get_cmap('Spectral'))

    for label, x, y in zip(labels, x0,x1):
        plt.annotate(
            label,
            xy = (x, y),
            xytext = (-2, 2),
            textcoords = 'offset points', ha = 'right', va = 'bottom'
            )
    plt.xlabel("rating")
    plt.ylabel("age")

    plt.show()





def createWineData2(nbData):
    inputs=[]
    prices=[]

    for i in range(nbData):
        rating=random.random()*50+50
        age=random.random()*50

        aisle=float(random.randint(1,20))
        bottleSize=[375.,750.,1500.,3000.][random.randint(0,3)]

        price=winePrice(rating,age)
        price*=bottleSize/750
        price*=random.random()*0.2+0.9

        inputs.append([rating,age,aisle,bottleSize])
        prices.append(price)

    return inputs,prices

