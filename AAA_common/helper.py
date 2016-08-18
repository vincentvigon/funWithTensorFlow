import time


class Bilan:

    def __init__(self):
        self._millisDep=time.time()
        self._millisDuration = 0
        self._nbTested = 0
        self._nbOK = 0
        return

    def _computeTime(self):
        return time.time()-self._millisDep

    """ on peut créer plusieurs bilans et les additionner dans un 'bilan global' """
    def add(self,bilan):
        self._nbTested += bilan.nbTested
        self._nbOK += bilan.nbOK
        self._millisDuration += bilan.millisDuration
        return

    def assertTrue(self,ok:bool):
        self._nbTested+=1
        if ok: self._nbOK+=1
        else:raise RuntimeError('Un test ne fonctionne pas')
        return
    def __repr__(self):
        return 'nbTest:'+str(self._nbTested) + ', nbOK:' + str(self._nbOK) + ', millisDuration:' + str(round(self._millisDuration, 2))





def testBilan():
    bilan=Bilan()
    bilan.assertTrue(True)
    bilan.assertTrue(False)
    bilan.assertTrue(False)


