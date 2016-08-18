
from TP1_firstStepWithPython.X_correction import *
from AAA_common.helper import *

point1=Point(0, 0.0001)
point2=Point(0,0)

trajet1=[point1, Point(1., 1.), Point(1., 0.)]
trajet2=[Point(-1, -1), Point(0., 0.0002), Point(1, 1), Point(1, 0), Point(2, 2)]


bilan=Bilan()
bilan.assertTrue(point1.hashString()==point2.hashString())
bilan.assertTrue(len(commonPoints(trajet1, trajet2))==3)
bilan.assertTrue(len(commonSegment(trajet1, trajet2))==2)

""" la liste des tests devra s'alonger à chaque fois que vous écrivez un bout de code """
print (bilan)
