


from data_model.core.general.General import General
from data_model.core.body.Body import Body
from data_model.core.mind.Mind import Mind

class PersonPDT:

    def __init__(self):
        self._body = Body()
        self._mind = Mind()
        self._coordinate = General().createCoordinate()
        return

#*** MODIFIER ***********************************************************************

#*** ACCESSORS **********************************************************************

    def getCoordinate(self):
        return self._coordinate

    def setCoordinate(self, coordinate):
        self._coordinate = coordinate

    def getBody(self):
        return self._body

    def setBody(self, body):
        self._body = body

    def getMind(self):
        return self._mind

    def setMind(self, mind):
        self._mind = mind

    def setCodeInt(self, vint):
        self._mind.inner.setCodeInt(vint)

    def getCodeInt(self):
        return self._mind.inner.getCodeInt()

    def getDesitionCode(self):
        return self._mind.inner.getDesitionCode()

    def setDesitionCode(self, vint):
        self._mind.inner.setDesitionCode(vint)

    def getDesitionGoal(self):
        return self._mind.inner.getDesitionGoal()

    def setDesitionGoal(self, vint):
        self._mind.inner.setDesitionGoal(vint)

    def getIsDeath(self):
        return self._body.inner.getIsDeath()

#***********************************************************************************
