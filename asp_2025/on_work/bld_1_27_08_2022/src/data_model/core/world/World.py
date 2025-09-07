



from data_model.core.region.Region import Region
from data_model.core.market.Market import Market

class World:

    worldSizeX = 30
    worldSizeY = 15

    def __init__(self):
        self.messagesOnHold = ""
        self.market = Market()
        self.regionMatrix = []
        return

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
        region = self.getRegionByCode(regionCode)
        self.market = region.build(self.market, type, locationY, locationX, recipe)
        self.messagesOnHold += region.obtainMessagesOnHold()
        self.setRegion(region)

    def writeRegionByCode(self, code):
        region = self.getRegionByCode(code)
        return region.writeMap()

    def createNewMap(self):
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
                region.createNewMap()
                matrix[y].append(region)
                n += 1
        self.regionMatrix = matrix

    def advanceTime(self):
        for y in range(World.worldSizeY):
            for x in range(World.worldSizeX):
                region = self.regionMatrix[y][x]
                self.market = region.advanceTime(self.market)
                self.regionMatrix[y][x] = region
