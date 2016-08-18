import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


''' voici mes tests tiré de cette page web :   http://pandas.pydata.org/pandas-docs/stable/10min.html#histogramming'''

def exo1():
    s = pd.Series([1,3,5,np.nan,6,8])

    df2 = pd.DataFrame({
    'A' : 1.,
    'B' : pd.date_range('20130101', periods=4,freq='5H'),
    'C' : pd.Series(1,index=list(range(4))),
    'D' : [2,3,4,5],
    'E' : pd.Categorical(["test","train","test","train"]),
    'F' : 'foo' })


    print(df2)
    #print(df2.head(2))
    #print(df2.describe())
    #print(df2['D'])
    return


def exo2():
    #Creating a DataFrame by passing a numpy array, with a datetime index and labeled columns:
    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    print(df,"\n\n\n")

    '''selection par label et colonne'''
    #print(df.loc[dates[0]])
    #print(df.loc[ [dates[0],dates[2]], ['A', 'B']])
    #print(df.loc[ :, ['A', 'B']])
    '''selection par colonne'''
    #print(df.A)
    #print(df['A'])
    '''selection par valeur'''
    #print(df.A>0)
    #print(df[df.A>0])

    ''' opérations sur les données '''
    #print(df.mean())
    #print (df.mean(1))
    print(df.apply(np.cumsum))
    return


# def exo3():
#     dates = pd.date_range('20130101', periods=6)
#     df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
#     s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates)#.shift(2)
#     df.sub(s, axis='index')
#     print (s)
#     print(df,"\n\n\n")
#
#     return


exo2()




