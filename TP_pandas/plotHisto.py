import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import numpy as np
import random

''' http://pandas.pydata.org/pandas-docs/stable/visualization.html '''

def exo1():
    nb=1000
    ts = pd.Series(np.random.randn(nb), index=pd.date_range('1/1/2000', periods=1000))
    ts = ts.cumsum()
    ts.plot()
    plt.show()
    return


def exo1bis():
    nb=1000
    y=[]
    y.append(0)
    for i in range(1,nb):
        y.append(random.normalvariate(0,1)+y[i-1])

    plt.plot(range(nb),y)
    plt.show()
    return


def exo2():
    nb = 1000
    ts = pd.Series(np.random.randn(nb), index=pd.date_range('1/1/2000', periods=1000))
    df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
    df=df.cumsum()
    df.plot()
    plt.show()
    return


def exo3():
    df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
    #df2.plot.bar()
    df2.plot.bar(stacked=True)
    plt.show()
    return


def exo4():
    df4 = pd.DataFrame({
    'a': np.random.randn(1000) + 2,
    'b': np.random.randn(1000)})
    df4.plot.hist(alpha=0.5,bins=20)
    #df4.plot.hist(alpha=0.5,bins=20,stacked=True)
    plt.show()
    return


exo4()





