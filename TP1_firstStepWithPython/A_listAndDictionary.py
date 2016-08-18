
from typing import List
from typing import Dict

""" Liste (ou tableau) et dictionnaire sont les deux structures de données primordiales.
  Nous utilisons aussi le typage qui évite beaucoup d'erreur (uniquement a partir de python 3.5)"""


"""=================================================================================================================="""
"""créons des fonctions"""

def addition(a:float,b:float)->float:
    return a+b

def division(a:float,b:float)->float:
    if b==0: raise RuntimeError("second arg must be non zero")
    return a/b

def duplicateEachLetter(word:str)->str:
    res=""
    for letter in word:
        res+=letter+letter
    return res

print (addition(1,1)) #output 2
print (division(2,3)) #output 0.66666666666
print (duplicateEachLetter("toto"))
"""ci-dessous, une erreur que nous signalons nous même"""
# print (division(5,0)) would produce exception (=error message)


"""=================================================================================================================="""
""" création d'un dico et d'une liste avec expression littérale dite 'JSON' """
dictionnaire={'unEntier':3,'unStr':'aba'}
maListe=[1,2,3,4,5]


"""un dictionnaire est composé de clef et de valeurs. Les clefs sont des string, des entier (ou aussi des Tuplet).
Les valeurs peuvent être n'importe quel objet """
unEntier=3
unStr='aba'
dictionnaireBis={'unEntier':unEntier,'unStr':unStr}

"""création d'un dico élément par élément """
dico={}
dico['unEntier']=3
dico['unStr']='aba'
dico['unDico']=dictionnaire
dico['uneListe']=maListe

print(dico)

""" on accède aux valeur comme ceci"""
print(dico['unEntier'])#quand on est sur que la clef est présente
print(dico.get('toto'))#quand on n'est pas sur. Cela renvoie false quand la clef n'est pas présente


""" les dictionnaires  sont aussi utilisé pour représenter des ensembles (au sens mathématique) """
uneListe=[1,2,1,4,1,4,1,1,1,1]
unEnsemble={}
for i in uneListe:
    unEnsemble[i]=True
"""pour savoir si 0 est dans l'ensemble """
print(unEnsemble.get(0))






"""=================================================================================================================="""
"""création d'une liste et d'un dico avec des fonctions, vérification de typage"""

def createList(size)->List[int]:
    res=[]
    for i in range(size):
        res.append(i)
    return res


li=createList(4)
li.append(0)
li.append(-1)
li.extend([0,0,1,5])
"""ci-dessous, erreur de typage"""
#li.append('aze')
#li.append(3.5)

print (li)



def createDico()->Dict[int,str]:
    res={}
    alphabet='abcdefghijklmnopqrstuvwxyz'
    for i in range(26):
        res[i]=alphabet[i]
    return res

didi=createDico()
print(didi)
print("cinquième lettre:",didi[4])

"""ci-dessous, erreur de typage"""
#didi['toto']

''' Remarque: nous aurions pu tout autant faire une liste plutôt qu'un  Dict[int,str].'''
''' Mais a quel situation un  Dict[int,str] est mieux adapté qu'une simple liste ? '''



"""=================================================================================================================="""
""" attention, contrairement au dictionnaire, dans un tableau, il faut avoir créer un élément avant de l'appeler """
tab=[]
'''une erreur qui n'en aurait pas été une si tab était un dictionnaire  '''
#tab[0]='AE'

for i in range(4):
    tab.append('')

tab[3]='AES'
tab[0]='BON'
print(tab)


'''attention à l'ordre de vos instruction. Dans de nombreux langages de "script", les fonctions/classes doivent être définie avant leur utilisation.
 ci-dessous, une erreur'''
# a=bou()
# def bou():
#     return 1
