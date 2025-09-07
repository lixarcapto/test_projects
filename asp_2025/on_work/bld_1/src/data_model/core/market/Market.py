


from data_access.DataAccess import DataAccess
from data_access.core.tab_map.TabMap import TabMap
from basic.Basic import Basic
from basic.core.image_popup.ImageOrder import ImageOrder

class Market:

    def __init__(self):
        self.keysData = DataAccess().getKeysData()
        self.productMatrix = [0] * self.keysData.getQuantityMarketGlobalKeys()
        self.previousValueDifferenceMatrix = [0] * self.keysData.getQuantityMarketGlobalKeys()
        self.everythingProducedSoFar = [0] * self.keysData.getQuantityMarketGlobalKeys()
        return

    def hasResource(self, code, quantity):
        if(self.productMatrix[code] >= quantity):
            return True
        return False

    def consumeResource(self, code, quantity):
        self.productMatrix[code] -= quantity

    def calculeDiferenceValue(self, market):
        beforeValue = 0
        actualValue = 0
        result = 0
        for i in range(len(self.productMatrix)):
            beforeValue = market.productMatrix[i]
            actualValue = self.productMatrix[i]
            result = actualValue - beforeValue
            self.previousValueDifferenceMatrix[i] = result

    def sumMarket(self, market):
        for i in range(len(self.productMatrix)):
            self.productMatrix[i] = market.productMatrix[i] + self.productMatrix[i]

    def copyMarket(self, market):
        for i in range(len(self.productMatrix)):
            self.productMatrix[i] = market.productMatrix[i]

    def convertMarketToIconListArray(self, directionImage, format):
        matrix = []
        array = None
        key = ""
        imageName = ""
        for i in range(len(self.productMatrix)):
            array = []
            key = self.keysData.getMarketGlobalKey(i)
            imageName = directionImage + key + format
            array.append(imageName)
            array.append(" = " + str(self.productMatrix[i]))
            matrix.append(array)
        return matrix

    def sumResource(self, code, value):
        self.productMatrix[code] = self.productMatrix[code] + value
        self.everythingProducedSoFar[code] += value

    def haveTheProducts(self, productMatrix):
        for e in productMatrix:
            if(not self.hasResource(e[1], e[2])):
                return False
        return True

    def consumeProductMatrix(self, productMatrix):
        for e in productMatrix:
            self.consumeResource(e[1], e[2])

    def sumProductMatrix(self, productMatrix):
        for e in productMatrix:
            self.sumResource(e[1], e[2])

    def getMarketTab(self, marketTabKey):
        return TabMap().inner[marketTabKey]

    def writeMarketValues(self, marketTabKey, directionImage, format):
        directionImage += "market/"
        return self.convertMarketToIconListArray(directionImage, format)
        """
        spaceTitle = "-" * 30
        text = spaceTitle + "market: " + marketTabKey + spaceTitle + "\n"
        code = 0
        columnSize = 0
        limitColumnSize = 3
        spaceInterColumn = 6
        spaceToFillColumn = 0
        idealSpaceColumn = 20
        minimumResourceToAdvise = 10
        mediumResourceToAdvise = 50
        spaces = ""
        key = ""
        marketTab = self.getMarketTab(marketTabKey)
        productIndex = 0
        for i in range(len(marketTab)):
            green = "\x1b[0;32m"
            red = "\x1b[0;31m"
            white = "\x1b[0;37m"
            productIndex = self.keysData.getMarketGlobalIndex(marketTab[i])
            basic = Basic()
            spaceToFillColumn = idealSpaceColumn - len(key)
            if(self.productMatrix[productIndex] <= minimumResourceToAdvise):
                text += red
            elif(self.productMatrix[productIndex] <= mediumResourceToAdvise):
                text += green
            text += " > " + marketTab[i]
            text += ": " + str(self.productMatrix[productIndex])
            differenceNumber = str(self.previousValueDifferenceMatrix[productIndex])
            differenceValue = ""
            if(self.previousValueDifferenceMatrix[productIndex] > 0):
                differenceValue = " +" + differenceNumber
            if(self.previousValueDifferenceMatrix[productIndex] < 0):
                differenceValue = " -" + differenceNumber
            text += differenceValue
            text += "(" + str(self.everythingProducedSoFar[productIndex]) + ")"
            text += " " * spaceInterColumn
            text += white
            columnSize += 1
            if(columnSize == limitColumnSize):
                columnSize = 0
                text += "\n"
            """
        return text
