



from data_model.core.region.Region import Region
from data_model.core.general.core.coordinate.Coordinate import Coordinate
from basic.Basic import Basic
from data_access.DataAccess import DataAccess
from data_model.core.general.core.date.Date import Date
import random

class World:

    def __init__(self):
        self._sizeX = 36
        self._sizeY = 36
        self._quantityStartedRegion = 10
        self._quantityStartedPerson = 6
        self._date = Date()
        self.regionMatrix = None
        return

#*** ACCESSORS ******************************************************************

    def getSizeX(self):
        return self._sizeX

    def setSizeX(self, vint):
        self._sizeX = vint

    def getSizeY(self):
        return self._sizeY

    def setSizeY(self, vint):
        self._sizeY = vint

    def getQuantityStartedRegion(self):
        return self._quantityStartedRegion

    def setQuantityStartedRegion(self, vInt):
        self._quantityStartedRegion = vInt

    def getQuantityStartedPerson(self):
        return self._quantityStartedPerson

    def setQuantityStartedPerson(self, vInt):
        self._quantityStartedPerson = vInt

#*** MUTTATORS ******************************************************************

    def getPersonInWorld(self, codeInt):
        person = None
        for y in range(self.getSizeY()):
            for x in range(self.getSizeX()):
                person = self.regionMatrix[y][x].inner._personList.getPerson(codeInt)
                if(person != None):
                    return person
        return None

    def updatePersonInWorld(self, person):
        result = 0
        for y in range(self.getSizeY()):
            for x in range(self.getSizeX()):
                if(self.regionMatrix[y][x].inner.getIsInhabited()):
                    result = self.regionMatrix[y][x].inner._personList.updatePerson(person)
                    if(result != -1):
                        return 0
        return -1

    def calculeData(self):
        region = None
        latitudeCounter = 90
        longitudeCounter = 0
        for y in range(self.getSizeY()):
            for x in range(self.getSizeX()):
                region = self.regionMatrix[y][x]
                region.latitude = latitudeCounter
                region.longitude = longitudeCounter
                self.regionMatrix[y][x] = region
                longitudeCounter += 2.5
            longitudeCounter = 0
            latitudeCounter -= 2.5

    def writeGlobalDescription(self):
        text = "GLOBAL DESCRIPTION"
        region = None
        for y in range(self.getSizeY()):
            for x in range(self.getSizeX()):
                region = self.regionMatrix[y][x]
                text += region.writeRegionDescription()
        return text

    def randomizeInitialCultures(self, quantityNations):
        cultureLimit = DataAccess().createValuesSupplier().getCulturesLimit() -1
        culturesCodesArray = Basic().generateRandomArrayWithoutRepeat(quantityNations,
        cultureLimit)
        return culturesCodesArray

    def generateRandomCultures(self, quantity):
        None
        return []

    def colonizeInitialRegion(self):
        quantityStartedRegion = self.getQuantityStartedRegion()
        quantityRegionCodes = self.getSizeX() * self.getSizeY()
        coordinatesMatrix = Basic().randomizeCoordinates(quantityStartedRegion,
        self.getSizeY() -1, self.getSizeX() -1)
        culturesCodesArray = self.randomizeInitialCultures(quantityStartedRegion)
        x = 0
        y = 0
        cultureCode = 0
        for i in range(quantityStartedRegion):
            y = coordinatesMatrix[i][0]
            x = coordinatesMatrix[i][1]
            self.regionMatrix[y][x].inner.setCulture(culturesCodesArray[i])
            self.regionMatrix[y][x].inner.setIsInhabited(True)
            self.regionMatrix[y][x].createInitialPerson(self.getQuantityStartedPerson())
            print("_isInhabited : " + str(y) + "/ " + str(x))

    def createVoidMap(self):
        self.regionMatrix = [None] * self.getSizeY()
        for i in range(self.getSizeY()):
            self.regionMatrix[i] = [None] * self.getSizeX()
        region = None
        n = 0
        coordinate = 0
        for y in range(self.getSizeY()):
            for x in range(self.getSizeX()):
                region = Region()
                region.inner.setCodeInt(n)
                coordinate = region.inner.getCoordinate()
                coordinate.setX(x)
                coordinate.setY(y)
                region.inner.setCoordinate(coordinate)
                self.regionMatrix[y][x] = region
                n += 1

    def randomizeDate(self):
        yearMinimum = 900
        yearMaximum = 1400
        regionKeys = DataAccess().getRegionKeys()
        year = random.randint(yearMinimum, yearMaximum)
        day = random.randint(0, len(regionKeys.getDaysMap()) -1)
        month = random.randint(0, len(regionKeys.getMonthsMap()) -1)
        self._date.setYear(year)
        self._date.setDay(day)
        self._date.setMonth(month)

    def createNewMap(self):
        self.createVoidMap()
        self.calculeData()
        self.colonizeInitialRegion()
        self.randomizeDate()

    def advanceOneDayToEachRegion(self, worldProduct):
        region = None
        for y in range(self.getSizeY()):
            for x in range(self.getSizeX()):
                    region = self.regionMatrix[y][x]
                    if(region.inner.getIsInhabited()):
                        region.advanceOneDay(worldProduct)
                    self.regionMatrix[y][x] = region

    def getAllCodesOfLivePersonInWorld(self):
        personLiveArray = []
        temporalArray = []
        personList = None
        for y in range(self.getSizeY()):
            for x in range(self.getSizeX()):
                if(self.regionMatrix[y][x].inner.getIsInhabited()):
                    personList = self.regionMatrix[y][x].inner.getPersonList()
                    temporalArray = personList.getPersonLiveCodesArray()
                    for e in temporalArray:
                        personLiveArray.append(e)
        return personLiveArray

    def getRegionByCoordinate(self, coordinate):
        return self.regionMatrix[coordinate.getY()][coordinate.getX()]

    def setRegion(self, region):
        coordiante = region.getCoordinate()
        self.regionMatrix[coordinate.getY()][coordinate.getX()] = region

#--- PERSON DESITIONS -----------------------------------------------------------------

    def makeDesitions(self):
        makeDesitions = MakeDesitionTk()
        self.inner = makeDesitions.inner(self.inner)

    def advanceTime(self):
        self.advanceOneDayToEachRegion()
