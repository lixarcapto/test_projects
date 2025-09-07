

from data_model.core.person_list.PersonList import PersonList

class RegionPDT:

    SIZE_X = 14
    SIZE_Y = 8
    MINIMUM_RESOURCE = 200
    MAXIMUM_RESOURCE = 999

    def __init__(self):
        self.name = ""
        self.code = 0
        self.mapMatrix = []
        self.personList = PersonList()

    def setCode(self, vint):
        self.code = vint

    def getCode(self):
        return self.code

    def getSizeX(self):
        return RegionPDT.SIZE_X

    def setSizeX(self, vint):
        RegionPDT.SIZE_X = vint

    def getSizeY(self):
        return RegionPDT.SIZE_Y

    def setSizeY(self, vint):
        RegionPDT.SIZE_Y = vint

    def getMinimumResource(self):
        return RegionPDT.MINIMUM_RESOURCE

    def getMaximumResource(self):
        return RegionPDT.MAXIMUM_RESOURCE
