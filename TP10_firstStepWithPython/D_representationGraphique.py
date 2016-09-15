
import matplotlib.pyplot as plt
import numpy as np


def simplePlot():
    data=np.random.normal(size=(2,10))

    x_data=data[0,:]
    y_data=data[1,:]

    plt.plot(x_data,y_data,'ro')
    plt.plot(x_data,y_data)
    plt.show()
    return




def scatterPlot():
    import numpy as np
    import matplotlib.pyplot as plt

    N = 10
    data = np.random.random((N, 4))
    labels = ['point{0}'.format(i) for i in range(N)]
    plt.subplots_adjust(bottom=0.1)
    plt.scatter(
        data[:, 0], #x
        data[:, 1], #y
        marker='o', #forme en o
        c=data[:, 2], #couleur
        s=data[:, 3] * 1500, #rayon
        cmap=plt.get_cmap('Spectral')) #mapping des couleurs

    for label, x, y in zip(labels, data[:, 0], data[:, 1]):
        plt.annotate(
            label,
            xy=(x, y), #position du texte
            xytext=(-20, 20), #decalage du texte
            textcoords='offset points',#la position du texte dépend des points
            ha='right', va='bottom', #alignement
            bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5), #encadrement
            arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0')) # flèche

    plt.show()
    return

scatterPlot()