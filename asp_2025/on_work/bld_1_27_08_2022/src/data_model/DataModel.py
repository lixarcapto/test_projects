


import random
from data_access.DataAccess import DataAccess
from data_model.core.world.World import World
from basic.Basic import Basic

class DataModel:

    def __init__(self):
        self.actualRegionSelected = 0
        self.actualNationSelected = 0
        self.world = World()
        return

    def advanceTime(self):
        self.world.advanceTime()

    def createNewMap(self):
        self.world.createNewMap()

    def writeMap(self):
        return self.world.writeRegionByCode(self.actualRegionSelected)

    def writeMarketValues(self):
        return self.world.market.writeMarketValues()

    def writePersonData(self):
        return ""

    def obtainMessagesOnHold(self):
        return self.world.obtainMessagesOnHold()

    def build(self, type, locationY, locationX, recipe):
        self.world.buildInRegion(self.actualRegionSelected,
        type, locationY, locationX, recipe)

    def writeBuildInformation(self):
        marketGlobalKeysMap = DataAccess().getKeysData().getMarketGlobalKeysMap()
        buildingCollection = DataAccess().getBuildingData().buildingCollection
        text = ""
        build = None
        key = ""
        for e in buildingCollection:
            build = buildingCollection[e]
            text += build.type + " require: \n"
            for f in build.resourceList.INNER:
                key = Basic().obtainKey(marketGlobalKeysMap, f[1])
                text += " >> " + key + " = " + str(f[2]) + "\n"
            text += "\n"
        return text
