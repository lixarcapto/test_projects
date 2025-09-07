


from data_access.DataAccess import DataAccess

class Market:

    def __init__(self):
        self.MARKET_GLOBAL_KEYS = DataAccess().getKeysData().getMarketGlobalKeysMap()
        self.productMatrix = [0] * len(self.MARKET_GLOBAL_KEYS)
        return

    def hasResource(self, code, quantity):
        if(self.productMatrix[code] >= quantity):
            return True
        return False

    def consumeResource(self, code, quantity):
        self.productMatrix[code] -= quantity

    def sumMarket(self, market):
        for i in range(len(self.productMatrix)):
            self.productMatrix[i] = market.productMatrix[i] + self.productMatrix[i]

    def sumResource(self, code, value):
        self.productMatrix[code] = self.productMatrix[code] + value

    def haveTheProducts(self, productMatrix):
        for e in productMatrix:
            print(str(e[1]) + " / " + str(e[2]))
            if(not self.hasResource(e[1], e[2])):
                return False
        return True

    def consumeProductMatrix(self, productMatrix):
        for e in productMatrix:
            self.consumeResource(e[1], e[2])

    def sumProductMatrix(self, productMatrix):
        for e in productMatrix:
            self.sumResource(e[1], e[2])

    def writeMarketValues(self):
        text = "market: \n"
        code = 0
        columnSize = 0
        limitColumnSize = 4
        spaceInterColumn = 6
        spaceToFillColumn = 0
        idealSpaceColumn = 20
        spaces = ""
        for e in self.MARKET_GLOBAL_KEYS.keys():
            spaceToFillColumn = idealSpaceColumn - len(e)
            spaces = " " * spaceToFillColumn
            text += " > " + e
            code = self.MARKET_GLOBAL_KEYS[e]
            text += spaces
            text += ": " + str(self.productMatrix[code]) + " " * spaceInterColumn
            columnSize += 1
            if(columnSize == limitColumnSize):
                columnSize = 0
                text += "\n"
        return text
