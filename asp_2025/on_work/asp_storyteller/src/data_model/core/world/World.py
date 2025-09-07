


from data_model.core.region.Region import Region
from data_model.core.market.Market import Market
from data_model.core.date.Date import Date

class World:

    def __init__(self):
        self.actualRegionX = 0
        self.actualRegionY = 0
        self.regionMatrix = []
        self.sizeX = 0
        self.sizeY = 0
        self.market = Market()
        self.date = Date()
        return

    def createNewWorld(self, sizeY, sizeX):
        self.createVoidWorld(sizeY, sizeX)
        self.randomizeWorld()

    def createVoidWorld(self, sizeY, sizeX):
        self.sizeX = sizeX
        self.sizeY = sizeY
        matrix = []
        array = None
        region = Region()
        for y in range(sizeY):
            array = []
            for x in range(sizeX):
                region = Region()
                array.append(region)
            matrix.append(array)
        self.regionMatrix = matrix

    def randomizeWorld(self):
        for y in range(self.sizeY):
            for x in range(self.sizeX):
                self.regionMatrix[y][x].randomizeRegion()

    def createBuilding(self, buildingKey, recipeKey):
        self.regionMatrix[self.actualRegionY][self.actualRegionX].createBuilding(
        buildingKey, recipeKey)

    def writeRegionInformation(self):
        text = ""
        text += self.regionMatrix[self.actualRegionY][self.actualRegionX].writeResources()
        return text

    def writeMarketInformation(self):
        text = ""
        text = self.market.writeMarketInformation()
        return text

    def advanceOneDay(self):
        self.date.advanceOneDay()
        for y in range(self.sizeY):
            for x in range(self.sizeX):
                self.market = self.regionMatrix[y][x].advanceOneDay(self.market,
                self.date.writeDate())

    def writeSocietyInformation(self):
        text = ""
        text += self.regionMatrix[self.actualRegionY][self.actualRegionX].writeSocietyInformation()
        return text
