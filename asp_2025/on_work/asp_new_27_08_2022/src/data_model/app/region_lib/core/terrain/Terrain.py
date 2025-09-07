

from data_model.app.market_lib.core.job_offert.JobOffert import JobOffert

class Terrain:

    def __init__(self):
        self.indexX = 0
        self.indexY = 0
        self.code = 0
        self.buildingProduct = None
        self.typeResource = "none"
        self.quantityResource = 0
        self.personAssignedHere = []

    def addPersonCode(self, personCode):
        self.personAssignedHere.append(personCode)

    def deletePersonCode(self, personCode):
        for i in range(self.personAssignedHere):
            if(self.personAssignedHere[i] == personCode):
                del self.personAssignedHere[i]
            break
