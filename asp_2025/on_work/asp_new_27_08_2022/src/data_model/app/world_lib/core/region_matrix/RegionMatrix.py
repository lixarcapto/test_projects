

from data_model.app.region_lib.Region import Region
from data_access.DataAccess import DataAccess
import random

class RegionMatrix:

    SIZE_Y = 36
    SIZE_X = 36

    def __init__(self):
        self.total = 0
        self.regionMatrix = None
        return

    def getRegionByCode(self, code):
        for y in range(RegionMatrix.SIZE_Y):
            for x in range(RegionMatrix.SIZE_X):
                if(self.regionMatrix[y][x].code == code):
                    return self.regionMatrix[y][x]
        return None

    def advanceOneDayToEachRegion(self, worldProduct):
        region = None
        for y in range(RegionMatrix.SIZE_Y):
            for x in range(RegionMatrix.SIZE_X):
                    region = self.regionMatrix[y][x]
                    if(region.isItInhabited):
                        region.advanceOneDay(worldProduct)
                    self.regionMatrix[y][x] = region

    def endDayForAllWorld(self):
        for y in range(RegionMatrix.SIZE_Y):
            for x in range(RegionMatrix.SIZE_X):
                    if(self.regionMatrix[y][x].isItInhabited):
                        self.regionMatrix[y][x].endDayForRegion()

    def getRegion(self, locationX, locationY):
        return self.regionMatrix[locationX][locationY]

    def createMatrix(self):
        n = 0
        self.regionMatrix = [None] * RegionMatrix.SIZE_Y
        for i in range(RegionMatrix.SIZE_Y):
            self.regionMatrix[i] = [None] * RegionMatrix.SIZE_X
        for y in range(RegionMatrix.SIZE_Y):
            for x in range(RegionMatrix.SIZE_X):
                self.regionMatrix[y][x] = Region()
                self.regionMatrix[y][x].code = n
                self.regionMatrix[y][x].locationX = x
                self.regionMatrix[y][x].locationY = y
                self.regionMatrix[y][x].randomize()
                n += 1

    def haveNumberInArray(self, intArray, number):
        for e in intArray:
            if(e == number):
                return True
        return False

    def generateRandomArrayWithoutRepeat(self, quantityInt, maxSizeInt):
        randomizedIntArray = [None] * quantityInt
        randomInt = 0
        for i in range(quantityInt):
            while(True):
                randomInt = random.randint(0, maxSizeInt)
                if(self.haveNumberInArray(randomizedIntArray, randomInt) == False):
                    randomizedIntArray[i] = randomInt
                    print("random Number without repeat: " + str(randomInt))
                    break
        return randomizedIntArray

    def getAllCodesOfLivePersonInWorld(self):
        personLiveArray = []
        temporalArray = []
        for y in range(RegionMatrix.SIZE_Y):
            for x in range(RegionMatrix.SIZE_X):
                if(self.regionMatrix[y][x].isItInhabited):
                    temporalArray = self.regionMatrix[y][x].personList.getPersonLiveCodesArray()
                    for e in temporalArray:
                        personLiveArray.append(e)
        return personLiveArray

    def generateRandomCultures(self, quantity):
        cultureKeyData = DataAccess().getCultureKeyData()
        cultureArray = self.generateRandomArrayWithoutRepeat(quantity,
        cultureKeyData.LIMIT)
        return cultureArray

    def createFirstSettlement(self, quantitySettlement):
        randomIntArray = []
        randomNumber = 0
        for i in range(quantitySettlement):
            randomNumber = random.randint(0, RegionMatrix.SIZE_X * RegionMatrix.SIZE_Y)
            randomIntArray.append(randomNumber)
            print("randomNumber: " + str(randomNumber))
        cultureCodeArray = self.generateRandomCultures(quantitySettlement)
        for y in range(RegionMatrix.SIZE_Y):
            for x in range(RegionMatrix.SIZE_X):
                for i in range(len(randomIntArray)):
                    if(self.regionMatrix[y][x].code == randomIntArray[i]):
                        self.regionMatrix[y][x].createFirstPerson(cultureCodeArray[i])
                        print("codigo region: " + str(self.regionMatrix[y][x].code))

    def getPersonInWorld(self, code):
        person = None
        for y in range(RegionMatrix.SIZE_Y):
            for x in range(RegionMatrix.SIZE_X):
                if(self.regionMatrix[y][x].isItInhabited):
                    person = self.regionMatrix[y][x].personList.getPerson(code)
                    if(person != None):
                        return person
        return person

    def updatePersonInWorld(self, person):
        result = 0
        for y in range(RegionMatrix.SIZE_Y):
            for x in range(RegionMatrix.SIZE_X):
                if(self.regionMatrix[y][x].isItInhabited):
                    result = self.regionMatrix[y][x].personList.updatePerson(person)
                    if(result != -1):
                        return 0
        return -1

    def calculeData(self):
        region = None
        latitudeCounter = 90
        longitudeCounter = 0
        for y in range(RegionMatrix.SIZE_Y):
            for x in range(RegionMatrix.SIZE_X):
                region = self.regionMatrix[y][x]
                region.latitude = latitudeCounter
                region.longitude = longitudeCounter
                self.regionMatrix[y][x] = region
                longitudeCounter += 2.5
            longitudeCounter = 0
            latitudeCounter -= 2.5

    def writeInformation(self):
        text = " information about all world: \n"
        for y in range(RegionMatrix.SIZE_Y):
            for x in range(RegionMatrix.SIZE_X):
                text += self.regionMatrix[y][x].writeInformation()
        return text
