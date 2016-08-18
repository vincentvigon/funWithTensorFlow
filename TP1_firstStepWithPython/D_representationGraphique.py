
import matplotlib.pyplot as plt
import numpy as np
from typing import List
from typing import Tuple


def generatePoints(numPoint:int)->List[Tuple[float, float]]:
    res=[]
    for i in range(numPoint):
        res.append((np.random.normal(0,1),np.random.normal(0,1)))
    return res


data=generatePoints(5)


x_data=[v[0] for v in data]
y_data=[v[1] for v in data]


plt.plot(x_data,y_data,'ro')
plt.plot(x_data,y_data)
plt.show()

