
from typing import List
from typing import Dict
import time


"""====================================================== QUELQUES ERREURS CLASSIQUE ============================================================"""

def step1():
    """ attention, contrairement au dictionnaire, dans un tableau, il faut avoir créer un élément avant de l'appeler """
    tab=[]
    '''une erreur qui n'en aurait pas été une si tab était un dictionnaire  '''
    #tab[0]='AE'
    ''' l'utilisatino classique des liste est'''
    tab.append('toto')
    tab.append('tata')
    tab.append('tutu')
    for i in range(len(tab)): print(tab[i])



    '''si on veut créer un tableau vide de taille donnée on peut l'inialiser comme ceci'''
    tabSize4=[None for i in range(4)]
    tabSize4[3]='AES'
    tabSize4[0]='BONBON'
    print(tab)

    '''créons par exemple un tableau de tableau '''
    tabOfTabSize5= [[] for j in range(5)]
    tabOfTabSize5[3].append(5)
    tabOfTabSize5[3].append(2)
    tabOfTabSize5[1].append(6)

    print("tabOfTabSize5",tabOfTabSize5)


    '''attention à l'ordre de vos instruction. Dans de nombreux langages de "script", les fonctions/classes doivent être définie avant leur utilisation.
     Ci-dessous, une erreur'''
    # a=bou()
    # def bou():
    #     return 1
    return





'''  voici 4 bouts de code qui font la même chose: ils suppriment des éléments dans une liste
 Le troisième ne fonctionne pas comme on le souhaiterait.
  Cela illustre ce qui est pour moi une des grandes difficulté de l'informatique à savoir : le passage d'argument par adresse '''


def step2():


    '''voici une méthode directe et efficace pour supprimer plusieurs éléments d'un coup dans un tableau :
    l'idée, c'est qu'on crée un nouveau tableau
    '''
    array=['a','b','c','d']
    indices=[1,3]
    res=[]
    for i in range(len(array)):
        if i not in indices: res.append(array[i])
    array=res
    print('sans appel de fonction',array)



    '''on peut faire la même chose dans fonction'''
    def arrayMinusIndices(array:List,indices:List[int])->List:
        res=[]
        for i in range(len(array)):
            if i not in indices: res.append(array[i])
        return res
    array=['a','b','c','d']
    indices=[1,3]
    array=arrayMinusIndices(array,indices)
    print('arrayMinusIndices',array)


    '''Une technique informatique  est dite "InPlace" lorsqu'elle ne créer pas de copie d'objet (pas de res=[]).
       Par exemple, si vous voulez changer 1 élément dans un tableau de taille 1000, il vaut mieux utiliser une technique InPlace.
       Par contre si vous voulez supprimer 50% des éléments d'un tableau, il vaut mieux créer un nouveau tableau comme nous avons fait précédemment.

       Voici une fausse fonction "InPlace". Elle ne marche pas, comprenez pourquoi (utilisez ce que nous avons fait avant) '''
    def arrayMinusIndicesInPlace(array:List, indices:List[int])->None:
        res = []
        for i in range(len(array)):
            if i not in indices: res.append(array[i])
        array=res
        return
    array=['a','b','c','d']
    indices=[1,3]
    arrayMinusIndicesInPlace(array,indices)
    print('arrayMinusIndicesInPlace',array)



    '''Voici maintenant une fonction qui fait quasiment la même chose que la précédente.
    Mais au lieu de passer en argument un tableau, on passe un argument un objet qui contient un tableau (un wrapper = objet englobant).
    Cette fois cela marche ! Analyser pourquoi'''
    class Wrapper:
        def __init__(self,array):
            self.array=array
            self.autreChose=3

    def suppressIndicesOfAnArrayWrapped(wrapper:Wrapper,indices:List[int])-> None:
        res = []
        for i in range(len(wrapper.array)):
            if i not in indices: res.append(wrapper.array[i])
        wrapper.array=res
        return

    array=['a','b','c','d']
    wrapper=Wrapper(array)
    indices=[1,3]
    suppressIndicesOfAnArrayWrapped(wrapper,indices)
    print('suppressIndicesOfAnArrayWrapped',wrapper.array)





    '''fonction "InPlace" qui est bien 'in place' mais qui donne des résultat incompréhensible.'''
    def deleteIndicesInPlace(_array: List, indices: List[int]) -> None:
        for i in range(len(indices)): del _array[i]
        return

    array = ['a', 'b', 'c', 'd']
    indices = [1, 2]
    deleteIndicesInPlace(array, indices)
    print('deleteIndicesInPlace', array)

    array = ['a', 'b', 'c', 'd']
    indices = [1,1]
    deleteIndicesInPlace(array, indices)
    print('deleteIndicesInPlace', array)

    """ Pourquoi c'est incompréhensible : car quand on supprime un élément, la numérotation du tableau change. """




    return





''' Voici maintenant différentes fonctions qui supprime des éléments d'un tableau par valeur (et non plus par indice).
 Nous faisons également un test de performance qui vous montrera la puissance des dictionnaires (grâce aux tables de hachage qu'il y a derrière) '''

def step3():

    def deleteValuesInPlace0(array: List, valuesToSuppress: List) -> None:
        for elem in valuesToSuppress: array.remove(elem)
        return


    def deleteValuesInPlace1(array:List, valuesToSuppress:List)->None:
        for elem in valuesToSuppress:
            if elem in array: array.remove(elem)
        return

    def deleteValuesInPlace2(array:List, valuesToSuppress:List)->None:
        for elem in valuesToSuppress:
            try:
                array.remove(elem)
            except ValueError:
                pass
        return

    """pourquoi deleteValuesInPlace1 est deux fois plus longue que deleteValuesInPlace2 ?
    pourquoi deleteValuesInPlace0 plante ? """

    def deleteValues3(array:List, valuesToSuppress:List)->List:
        dico={}
        for elem in valuesToSuppress:
            dico[elem]=True
        res=[]
        for elem in array:
            if  dico.get(elem) is None: res.append(elem)
        return res


    import numpy as np


    def createData(size:int):
        data = []
        for a in range(size):
            data.append(str(a))

        perm=np.random.permutation(size)
        perm=perm[0:int(size/2)]
        dataToSuppress=[data[i] for i in perm]
        '''on rajoute une valeur à supprimer qui n'est pas  dans les data'''
        dataToSuppress.append('-1')
        return data,dataToSuppress


    # perm=np.random.permutation(6)
    # print(perm[1:4])
    # print(createData(6))



    size=20000

    data,dataToDelete=createData(size)
    t=time.time()
    deleteValuesInPlace1(data,dataToDelete)
    print('deleteValuesInPlace1:',time.time()-t)


    data,dataToDelete=createData(size)
    t=time.time()
    deleteValuesInPlace2(data,dataToDelete)
    print('deleteValuesInPlace2:',time.time()-t)

    data,dataToDelete=createData(size)
    t=time.time()
    deleteValues3(data,dataToDelete)
    print('deleteValues3:',time.time()-t)


    print("deleteValuesInPlace 1 et 2  : en plus d'être lente, elles ne marchent pas vraiment comme il faudrait ")
    data=['1','1','1','2']
    deleteValuesInPlace1(data,['1'])
    print(data)

    data=['1','1','1','2']
    deleteValuesInPlace2(data,['1'])
    print(data)

    print('deleteValues3 est parfaite en plus d être 1000 fois plus rapide')
    data=['1','1','1','2']
    data=deleteValues3(data,['1'])
    print(data)

    return

step3()

