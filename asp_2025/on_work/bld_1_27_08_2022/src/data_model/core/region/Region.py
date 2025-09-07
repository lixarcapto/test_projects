

from data_model.core.region.app.product.RegionPDT import RegionPDT
from data_model.core.terrain.Terrain import Terrain
from data_access.DataAccess import DataAccess
from basic.Basic import Basic
import random

class Region:

    def __init__(self):
        self.messagesOnHold = ""
        self.inner = RegionPDT()
        return

    def obtainMessagesOnHold(self):
        message = self.messagesOnHold
        self.messagesOnHold = ""
        return message

    def createVoidMapMatrix(self):
        matrix = []
        for y in range(self.inner.getSizeY()):
            array = []
            matrix.append(array)
            for x in range(self.inner.getSizeX()):
                matrix[y].append(Terrain())
        self.inner.mapMatrix = matrix

    def advanceTime(self, market):
        for y in range(self.inner.getSizeY()):
            for x in range(self.inner.getSizeX()):
                market = self.inner.mapMatrix[y][x].advanceTime(market)
                market = self.inner.personList.advanceTime(market)
        return market

    def writeMap(self):
        text = "  "
        translation = DataAccess().getTranslation()
        code = 0
        for i in range(self.inner.getSizeY()):
            text +=  "    " + str(i) + "    "
        text += "\n\n\n"
        for y in range(self.inner.getSizeY()):
            text +=  str(y) + "  "
            for x in range(self.inner.getSizeX()):
                code = self.inner.mapMatrix[y][x].inner.getBuildTypeInt()
                text += "[" + translation.translateBuildingType(code) + "]"
            text += "\n   "
            for x in range(self.inner.getSizeX()):
                code = self.inner.mapMatrix[y][x].inner.getResourceTypeInt()
                text += "[" + translation.translateResourceType(code) + "]"
            text += "\n   "
            for x in range(self.inner.getSizeX()):
                text += "[" + str(self.inner.mapMatrix[y][x].inner.getResourceQuantityInt()) + "    ]"
            text += "\n   "
            for x in range(self.inner.getSizeX()):
                code = self.inner.mapMatrix[y][x].inner.getSoilTypeInt()
                text += "[" + translation.translateSoilType(code) + "]"
            text += "\n\n"
        return text

    def randomizeMap(self):
        terrain = None
        soilTypeMap = DataAccess().getKeysData().getSoilTypeMap()
        resourceTypeMap = DataAccess().getKeysData().getResourcesTypeMap()
        for y in range(self.inner.getSizeY()):
            for x in range(self.inner.getSizeX()):
                terrain = self.inner.mapMatrix[y][x]
                randomNum = random.randint(0, len(soilTypeMap) -1)
                terrain.inner.setSoilTypeInt(randomNum)
                resourceQuantity = random.randint(self.inner.getMinimumResource(),
                self.inner.getMaximumResource())
                terrain.inner.setResourceQuantityInt(resourceQuantity)
                randomNum = random.randint(0, len(resourceTypeMap) -1)
                terrain.inner.setResourceTypeInt(randomNum)
                self.inner.mapMatrix[y][x] = terrain

    def build(self, market, buildingKey, locationY, locationX, recipe):
        buildData = DataAccess().getBuildingData()
        recipesKeysMap = DataAccess().getKeysData().getRecipesKeysMap()
        buildingKeysMap = DataAccess().getKeysData().getBuildingKeysMap()
        if(not Basic().hasTheKey(buildingKeysMap, buildingKey)):
            self.messagesOnHold += "<!>error building doesnt exist: " + buildingKey + "."
            return market
        if(not Basic().hasTheKey(recipesKeysMap, recipe)):
            self.messagesOnHold += "<!>error key doesnt exist: " + recipe + "."
            return market
        building = buildData.buildingCollection[buildingKey]
        if(not building.canBeBuilt(market)):
            self.messagesOnHold += "<!>error cant build it."
            return market
        market = building.buildIt(market)
        buildingKeysMap = DataAccess().getKeysData().getBuildingKeysMap()
        self.inner.mapMatrix[locationY][locationX].inner.setBuildTypeInt(buildingKeysMap[buildingKey])
        self.inner.mapMatrix[locationY][locationX].inner.setRecipeCodeInt(recipesKeysMap[recipe])
        return market

    def writeMarketValues(self):
        return self.market.writeMarketValues()

    def createNewMap(self):
        self.createVoidMapMatrix()
        self.randomizeMap()
        self.inner.personList.createInitialPerson(10)

    def writePersonData(self):
        return self.inner.personList.writePersonData()
