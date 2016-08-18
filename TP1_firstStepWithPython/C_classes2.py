
from typing import List

""" Une classe avec une méthode récursive  """

class Animal:
    def __init__(self,name:str):
        self.children=[] # type: List[Animal]
        self.name=name #type: str
        self.firstName="jean" #un prénom par défaut
        return

    def getMyCompleteName(self)->str:
        return self.name+self.firstName


    """ Voici une méthode récursive, prenez le temps de la comprendre.

      Dans l'idéal il faudrait rajouter à cette méthode le type de return : ->List[Animal],
      mais chez moi cela cré un warning injustifié. Cependant, l'inférence de type fait que l'IDE devine le type de retour (cf plus bas)"""
    def meAndMyDescendant(self):
        res=[self] # type: List[Animal]
        for child in self.children:
            res.extend(child.meAndMyDescendant())
        return res


    def __repr__(self):
        return self.name




"""PROGRAMME PRINCIPAL"""

tom=Animal("tom")
paul=Animal("paul")


mum=Animal("Clair")
mum.children=[tom, paul]



grandMother=Animal("gertrude")
grandMother.children.append(mum)

print (mum)
grandMotherDescendant=grandMother.meAndMyDescendant()
print (grandMotherDescendant)
"""comme indiqué plus haut, l'IDE arrive à inférer (=deviner) les type. Ainsi, voici erreur de type:"""
#grandMotherDescendant.append('toto')



"""pour l'instant on ne sait pas repérer l'égalité sémantique"""
tom2=Animal("tom")
paul2=Animal("paul")
mum2=Animal("Clair")
mum2.children=[tom2, paul2]
print ("deux type d'égalités",mum2==mum,mum2 is mum)

"""une fois que vous aurez implémentez la méthode Animal.__eq__, le résultat de (mum2==mum) et (mum2 is mum)  devraient être (true) et (false)"""

