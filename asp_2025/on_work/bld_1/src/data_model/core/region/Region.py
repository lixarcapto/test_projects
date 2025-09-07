

from colorama import init, Fore, Back, Style
from data_model.core.region.app.product.RegionPDT import RegionPDT
#TASK-----------------------------------------------------------------
from data_model.core.region.app.task.WriteMapTK import WriteMapTK
from data_model.core.region.app.task.BuildTK import BuildTK
from data_model.core.region.app.task.DoitRecipeTK import DoitRecipeTK
from data_model.core.region.app.task.RandomizeRegionTK import RandomizeRegionTK
from data_model.core.region.app.task.ConvertTerrainMatrixToImageNamesMatrixTK import ConvertTerrainMatrixToImageNamesMatrixTK
from data_model.core.region.app.task.HasNearbyResourceTK import HasNearbyResourceTK
from data_model.core.region.app.task.ExtractNearbyResourceTK import ExtractNearbyResourceTK
#--------------------------------------------------------------------------
from data_model.core.terrain.Terrain import Terrain
from data_access.DataAccess import DataAccess
from basic.Basic import Basic
from basic.core.image_popup.ImagePopup import ImagePopup
from data_access.core.resources_collection.ResourceCollection import ResourceCollection
import random

class Region:

    def __init__(self):
        self.inner = RegionPDT()
        return

    def obtainMessagesOnHold(self):
        message = self.inner.mailbox.obtainMessage()
        return message

    def isLimitX(self, coordinateArray):
        coordinateY = coordinateArray[0]
        coordinateX = coordinateArray[1]
        if(coordinateY < self.RegionPDT.SIZE_Y):
            return True
        return False

    def isLimitY(self, coordinateArray):
        coordinateY = coordinateArray[0]
        coordinateX = coordinateArray[1]
        if(coordinateX < self.RegionPDT.SIZE_X):
            return True
        return False

    def isInitX(self, coordinateArray):
        coordinateY = coordinateArray[0]
        coordinateX = coordinateArray[1]
        if(0 > coordinateX):
            return True
        return False

    def isInitY(self, coordinateArray):
        coordinateY = coordinateArray[0]
        coordinateX = coordinateArray[1]
        if(0 > coordinateY):
            return True
        return False

    def extractNearbyResource(self, coordinateArray, resourceCode, quantity):
        self.inner = ExtractNearbyResourceTK().inner(self.inner, coordinateArray,
        resourceCode, quantity)

    def hasNearbyResource(self, coordinateArray, resourceCode, quantity):
        return HasNearbyResourceTK().inner(self.inner, coordinateArray,
        resourceCode, quantity)

    def recruitPersonInRegionByCode(self, code):
        person = self.inner.personList.extractPerson(code)
        self.inner.battle.armyGarrison.personList.setPerson(person)

    def createInitialPerson(self, quantity):
        self.inner.setIsItPopulated(True)
        self.inner.personList.createInitialPerson(quantity)

    def createVoidMapMatrix(self, perimeterRegion):
        matrix = []
        self.inner.setSizeX(perimeterRegion)
        self.inner.setSizeY(perimeterRegion)
        for y in range(self.inner.getSizeY()):
            array = []
            matrix.append(array)
            for x in range(self.inner.getSizeX()):
                matrix[y].append(Terrain())
        self.inner.mapMatrix = matrix

    def doitRecipe(self, locationY, locationX, market):
        map = DoitRecipeTK().inner(regionPDT, locationY, locationX, market)
        self.inner = map["regionPDT"]
        return map["market"]

    def advanceTime(self, market):
        if(self.inner.getIsItPopulated()):
            market = self.inner.personList.advanceTime(market)
        #terrain matrix
        for y in range(self.inner.getSizeY()):
            for x in range(self.inner.getSizeX()):
                market = self.doitRecipe(y, x, market)
        self.inner.battle.advanceTime()
        return market

    def writeMap(self, camLocationY, camLocationX, sizeDistrict,
    actualDistrictSelected):
        text = self.convertTerrainMatrixToImageNameMatrix(camLocationY,
        camLocationX, sizeDistrict, actualDistrictSelected)
        return text

    def convertTerrainMatrixToImageNameMatrix(self, camLocationY,
    camLocationX, sizeDistrict, actualDistrictSelected):
        return ConvertTerrainMatrixToImageNamesMatrixTK().inner(self.inner,
        camLocationY, camLocationX, sizeDistrict, actualDistrictSelected)

    def calculeHappyPeople(self):
        number = 0
        if(self.inner.getIsItPopulated()):
            number = self.inner.personList.calculeHappyPeople()
        return number

    def randomizeMap(self, districtSize):
        self.inner = RandomizeRegionTK().inner(self.inner, districtSize)

    def build(self, market, buildingKey, locationY, locationX, recipe):
        mapResult = BuildTK().inner(self.inner, market, buildingKey,
        locationY, locationX, recipe)
        market = mapResult["market"]
        self.inner = mapResult["regionPDT"]
        return market

    def writeMarketValues(self, directionImage, format):
        return self.market.writeMarketValues()

    def createNewMap(self, districtSize, perimeterRegion):
        self.createVoidMapMatrix(perimeterRegion)
        self.randomizeMap(districtSize)
        self.inner.personList.createInitialPerson(10)

    def writePersonData(self):
        text = "is not populated"
        if(self.inner.getIsItPopulated()):
            text = self.inner.personList.writePersonData()
        return text

    def writeArmyData(self):
        text = ""
        if(self.inner.battle.armyGarrison != None):
            text = self.inner.battle.armyGarrison.personList.writePersonData()
        return text
