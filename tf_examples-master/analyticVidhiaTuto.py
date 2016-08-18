import pandas as pd
import numpy as np
import matplotlib as plt


# df = pd.read_csv('data/titanic_train.csv')
# print(df.head(10))
# #print(df.describe())
# print(df['Sex'].value_counts())
# print(df['Age'].hist(bins=5))


ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
print(ts.plot())




