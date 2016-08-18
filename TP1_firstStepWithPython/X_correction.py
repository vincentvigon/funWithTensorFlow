import math


#
# def roundWithGivenPrecision(value, nbDecimal):
#     value *= math.pow(10, nbDecimal)
#     value = rou(value)
#     value /= math.pow(10, nbDecimal)
#     return value



class Point:

    def __init__(self,x,y):
        self.x=float(x)
        self.y=float(y)
        return

    nbDigit=3


    def hashStringWithPrecision(self,nbDigit):
        return '('+str(round(self.x,nbDigit))+','+str(round(self.y,nbDigit))+')'

    def __repr__(self):
        return self.hashStringWithPrecision(1)

    def hashString(self):
        return self.hashStringWithPrecision(Point.nbDigit)




class Segment:

    def __init__(self,point1:Point,point2:Point):
        self.point1=point1
        self.point2=point2
        return

    def hashStringForUndirected(self):
        if self.point1.hashString()<self.point2.hashString():
            return '['+self.point1.hashString()+','+self.point2.hashString()+']'
        else:
            return '['+self.point2.hashString()+','+self.point1.hashString()+']'

    def __repr__(self):
        return '[' + self.point1.hashString() + ',' + self.point2.hashString() + ']'




def commonPoints(trajet1,trajet2):
    dico={}
    for point in trajet1:
        dico[point.hashString()]=True
    res=[]
    for point in trajet2:
        if  not dico.get(point.hashString()) is None:  res.append(point)
    return res

def commonSegment(trajet1,trajet2):
    dico={}
    for pointIndex in range(len(trajet1)-1):
        segment=Segment(trajet1[pointIndex],trajet1[pointIndex+1])
        dico[segment.hashStringForUndirected()]=True
    res=[]
    for pointIndex in range(len(trajet2) - 1):
        segment=Segment(trajet2[pointIndex],trajet2[pointIndex+1])
        if  not dico.get(segment.hashStringForUndirected()) is None:  res.append(segment)
    return res



def test():

    trajet1=[Point(0, 0.0001), Point(1., 1.), Point(1., 0.)]
    trajet2=[Point(-1, -1), Point(0., 0.0002), Point(1, 1), Point(1, 0), Point(2, 2)]

    print(commonPoints(trajet1, trajet2))
    print(commonSegment(trajet1, trajet2))
    return