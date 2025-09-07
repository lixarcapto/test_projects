

from data_model.core.person_list.PersonList import PersonList
from data_model.core.battle.Battle import Battle
from basic.Basic import Basic

class RegionPDT:

    SIZE_X = 7
    SIZE_Y = 7
    MINIMUM_RESOURCE = 200
    MAXIMUM_RESOURCE = 999

    def __init__(self):
        self.battle = Battle()
        self.isItPopulated = False
        self.isItHabitable = True
        self.mailbox = Basic().mailbox()
        self.name = ""
        self.messagesOnHold = ""
        self.code = 0
        self.reliefCode = 0
        self.ownerCode = 0
        self.mapMatrix = []
        self.personList = PersonList()

    def getIsItPopulated(self):
        return self.isItPopulated

    def setIsItPopulated(self, vboolean):
        self.isItPopulated = vboolean

    def setIsItHabitable(self, vboolean):
        self.isItHabitable = vboolean

    def getIsItHabitable(self):
        return self.isItHabitable

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
