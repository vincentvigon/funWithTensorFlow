import re

class Man:


    """le constructeur. Il sera lancé dès que l'on créera un objet de type Man
    Dedans, on défini les champs (=variables globales d' une classe).
    Certains peuvent être initialisé via les paramètre du constructeur"""
    def __init__(self,age:int,name:str)->None:
        self.age=age
        self.name=name
        self.conjoint=None# de type Man aussi
        self.nbChildren=0


        """champs privés (commencent par underscore) """
        self._nameListOfChildren= ""
        if not self._checkNameOK(name):raise RuntimeWarning("attention, le nom en entrée ne semble pas correcte")
        return


    """une méthode qui modifie un champs"""
    def becomeOlder(self)->None:
        self.age+=1
        return


    """un méthode qui donne accès en lecture seule à un champs privé"""
    def getNameListOfChildren(self):
        return self._nameListOfChildren


    """méthode privée. Pour usage interne
    elle vérifie que 'name' est acceptable"""
    def _checkNameOK(self,name:str)->bool:
        if re.match("^[A-Za-z0-9_-]*$", name):return True
        else: return False


    def addAChild(self,name)->None:
        if not self._checkNameOK(name):raise RuntimeWarning("attention, le nom en entrée ne semble pas correcte")
        self.nbChildren+=1
        self._nameListOfChildren+=","+name
        return

    """La méthode qui indique comment représenter notre objet en une chaîne de caractère.
    Préférez cette méthode à __str__ """
    def __repr__(self):
        return self.name

    """une fonction qui duplique (mal) un objet de type Man"""

    def duplicate(self):
        res = Man(self.age, self.name)
        res._nameListOfChildren=self._nameListOfChildren
        res.nbChildren=self.nbChildren
        res.conjoint=self.conjoint
        return res

    """ Une bonne habitude: Créer une méthode qui représente votre objet de manière "sémantique". Voir son utilisation plus loin"""
    def hashString(self):
        conjointName=""
        if self.conjoint is not None: conjointName=self.conjoint.name
        return '['+self.name+'+'+conjointName+'='+self._nameListOfChildren+']'




"""voici maintenant le programme principal"""
woman=Man(40,"Magali")
man0=Man(40, "Vincent")
man0.addAChild("Alix")
man0.addAChild("Joachim")
print("liste des enfants:",man0.getNameListOfChildren())
"""une méthode déjà faite qui résume l'object par un JSON"""
print(man0.__dict__)


man1=man0.duplicate()
man2=man0
""" quel sera le nombre d'enfant de man0 et man1 après cette opération ? """
man2.addAChild("toto")



"""vérification"""
print("man0",man0.__dict__)
print("man1",man1.__dict__)
print("man2",man2.__dict__)

""" remarquons que la méthode __dict__ utilise la méthode __repr__ """
man2.conjoint=woman
print("man2",man2.__dict__)


""" Utilisation de notre méthode hashString :  """

man3=man0.duplicate()


if man0.hashString()==man2.hashString(): print('ces deux objets sont sémantiquement égaux')

dico={}
dico[man0.hashString()]='man0'
dico[man1.hashString()]='man1'
dico[man2.hashString()]='man2'
dico[man3.hashString()]='man3'

print('dico:',dico)

""" J'espère que vous auriez pu prévoir la longueur de ce dictionnaire.
 Remarquons que nous avons fait en sorte que nos méthodes duplication et hashString soient 'compatibles'.

 En fait il y a des méthode __eq__ __hash__ qui permettent de créer le sens des égalités sémantiques, ensuite  l'opérateur == teste l'égalité sémantique,
 tandis que 'is' teste l'égalité parfaite.
  Mais c'est de la programmation plus avancé que je vous invite à découvrir vous même si vous en avez besoin.
 """











