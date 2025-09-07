



from data_model.core.region.Region import Region
from data_model.core.market.Market import Market
from data_access.DataAccess import DataAccess
from data_model.core.nation.Nation import Nation
from basic.Basic import Basic
import random

class World:

    worldSizeX = 20
    worldSizeY = 15

    def __init__(self):
        self.playerIndexNation = 0
        self.nationArray = []
        self.nationQuantity = 6
        self.districtSize = 8
        self.districtQuantity = 8
        self.regionPerimeter = self.districtSize * self.districtQuantity
        self.terrainQuantity = self.regionPerimeter * self.regionPerimeter
        self.camRegionLocationX = 0
        self.camRegionLocationY = 0
        self.camSizeX = 8
        self.camSizeY = 6
        self.camLocationX = 0
        self.camLocationY = 0
        self.messagesOnHold = ""
        self.startPersonQuantity = 6
        self.regionMatrix = []
        return

    #XXX
    def giveMeCoordinatesOfSection(self, sectionCode, sizeMatrix, sectionSize):
        coordinatesArray = []
        array = None
        locationY = 0
        locationX = 0
        quantityCamCuts = int(self.regionPerimeter / self.districtSize-1)
        quantityCamCuts = int(quantityCamCuts / 2 )
        print("quantityCamCuts" + str(quantityCamCuts))
        for y in range(quantityCamCuts):
            for x in range(quantityCamCuts):
                array = [0] * 2
                array[0] = locationY
                array[1] = locationY
                coordinatesArray.append(array)
                print("cor: " + str(locationY) + "/" + str(locationX))
                locationX += self.districtSize
            locationX = 0
            locationY += self.districtSize
        coordinates = [0] * 2
        coordinates[0] = coordinatesArray[sectionCode][0]
        coordinates[1] = coordinatesArray[sectionCode][1]
        return coordinates

    def obtainIndexRegionHabitable(self):
        indexArray = []
        for y in range(World.worldSizeY):
            for x in range(World.worldSizeX):
                if(self.regionMatrix[y][x].inner.getIsItHabitable()):
                    indexArray.append(self.regionMatrix[y][x].inner.getCode())
        return indexArray

    def createNationArray(self):
        self.nationArray = []
        for i in range(self.nationQuantity):
            self.nationArray.append(Nation())

    def setOwnerStartRegion(self):
        region = None
        code = 0
        for i in range(len(self.nationArray)):
            code = self.nationArray[i].inner.getOwnedRegionCodesArray()[0]
            region = self.getRegionByCode(code)
            region.inner.ownerCode = i
            region.createInitialPerson(self.startPersonQuantity)
            self.setRegion(region)

    def writeNationData(self):
        return self.nationArray[self.playerIndexNation].writeNationData()

    def establishSettlements(self):
        indexHabitableRegion = self.obtainIndexRegionHabitable()
        randomIndexArray = Basic().generateRandomArrayWithoutRepeat(self.nationQuantity,
        len(indexHabitableRegion))
        randomizedCodesRegionArray = []
        for e in randomIndexArray:
            randomizedCodesRegionArray.append(indexHabitableRegion[e])
        for i in range(self.nationQuantity):
            self.nationArray[i].inner.addOwnedRegionCodes(randomIndexArray[i])
        self.setOwnerStartRegion()

    def obtainMessagesOnHold(self):
        message = self.messagesOnHold
        self.messagesOnHold = ""
        return message

    def getRegionByCode(self, code):
        region = None
        for y in range(World.worldSizeY):
            for x in range(World.worldSizeX):
                region = self.regionMatrix[y][x]
                if(region.inner.getCode() == code):
                    return region

    def setRegion(self, regionUpdate):
        for y in range(World.worldSizeY):
            for x in range(World.worldSizeX):
                region = self.regionMatrix[y][x]
                if(region.inner.getCode() == regionUpdate.inner.getCode()):
                    self.regionMatrix[y][x] = regionUpdate
                    return

    def buildInRegion(self, regionCode, type, locationY, locationX, recipe):
        market = self.nationArray[self.playerIndexNation].inner.marketGlobal
        region = self.getRegionByCode(regionCode)
        market = region.build(market, type, locationY, locationX, recipe)
        self.messagesOnHold += region.obtainMessagesOnHold()
        self.setRegion(region)
        self.nationArray[self.playerIndexNation].inner.marketGlobal = market

    def writeRegionByCode(self, code, districtLocation):
        coordinates = self.giveMeCoordinatesOfSection(districtLocation,
        self.regionPerimeter, self.districtSize)
        self.camRegionLocationY = coordinates[0]
        self.camRegionLocationX = coordinates[1]
        region = self.getRegionByCode(code)
        text = region.writeMap(self.camRegionLocationY,
        self.camRegionLocationX, self.districtSize, districtLocation)
        return text

    def writePersonDataByCode(self, code):
        region = self.getRegionByCode(code)
        return region.writePersonData()

    def writeAllPersonData(self):
        text = ""
        for y in range(len(self.regionMatrix)):
            for x in range(len(self.regionMatrix[y])):
                text += self.regionMatrix[y][x].writePersonData()
        return text

    def writePersonDataByCode(self, code):
        region = self.getRegionByCode(code)
        return region.writePersonData()

    def recruitPersonInRegionByCode(self, codeRegion, codePerson):
        region = self.getRegionByCode(codeRegion)
        region.recruitPersonInRegionByCode(codePerson)
        self.setRegion(region)

    def writeArmyData(self, code):
        region = self.getRegionByCode(code)
        return region.writeArmyData()

    def becomeWorldMapToStringMatrix(self, regionMatrix):
        number = 0
        keyImage = ""
        reliefKeysMap = DataAccess().getKeysData().getReliefKeysMap()
        matrix = Basic().matrix([len(regionMatrix),
        len(regionMatrix[0])])
        array = None
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                array = [""] * 5
                reliefKey = Basic().obtainKey(reliefKeysMap,
                regionMatrix[y][x].inner.reliefCode)
                array[0] = reliefKey
                array[1] = str(regionMatrix[y][x].inner.getCode())
                array[2] = "name"
                array[3] = "biome"
                array[4] = "owner"
                matrix[y][x] = array
        return matrix

    def cutCamInWorldMap(self, matrix):
        matrixResult = Basic().cutMatrix3D(matrix, self.camLocationX,
        self.camLocationY, self.camSizeY, self.camSizeX)
        return matrixResult

    def writeWorldMap(self):
        matrixCutted = self.cutCamInWorldMap(self.regionMatrix)
        matrix = self.becomeWorldMapToStringMatrix(matrixCutted)
        text = Basic().writeMatrixOfStringArray(matrix)
        return text

    def writeMarketValues(self, marketTabCode,  directionImage, format):
        i = self.playerIndexNation
        return self.nationArray[i].inner.marketGlobal.writeMarketValues(marketTabCode,
        directionImage, format)

    def createNewMap(self):
        self.createNationArray()
        self.regionMatrix = []
        matrix = []
        array = None
        region = None
        n = 0
        for y in range(World.worldSizeY):
            array = []
            matrix.append(array)
            for x in range(World.worldSizeX):
                region = Region()
                region.inner.setCode(n)
                region.createNewMap(self.districtSize,
                self.regionPerimeter)
                region.inner.reliefCode = random.randint(0, 6)
                matrix[y].append(region)
                n += 1
        self.regionMatrix = matrix
        self.establishSettlements()

    def calculeHappyPeople(self):
        number = 0
        for y in range(World.worldSizeY):
            for x in range(World.worldSizeX):
                number += self.regionMatrix[y][x].calculeHappyPeople()
        return number

    #inicia todos los procesos del inicio de turno
    def initTimeToNationArray(self):
        for i in range(len(self.nationArray)):
            nation = self.nationArray[i]
            nation.inner.marketGlobalPast.copyMarket(nation.inner.marketGlobal)
            self.nationArray[i] = nation

    #termina todos los procesos al fin del turno
    def endTimeToNationArray(self):
        for i in range(len(self.nationArray)):
            nation = self.nationArray[i]
            nation.inner.marketGlobal.calculeDiferenceValue(nation.inner.marketGlobalPast)
            self.nationArray[i] = nation

    #realiza todos los procesos de cada turno
    def advanceTime(self):
        region = None
        nation = None
        self.initTimeToNationArray()
        for y in range(World.worldSizeY):
            for x in range(World.worldSizeX):
                region = self.regionMatrix[y][x]
                nation = self.nationArray[region.inner.ownerCode]
                nation.inner.marketGlobal = region.advanceTime(nation.inner.marketGlobal)
                self.nationArray[region.inner.ownerCode] = nation
                self.regionMatrix[y][x] = region
        self.endTimeToNationArray()
