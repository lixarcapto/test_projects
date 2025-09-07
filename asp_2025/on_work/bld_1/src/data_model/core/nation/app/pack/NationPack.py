




from data_model.core.market.Market import Market

class NationPack:

    def __init__(self):
        self.cultureCode = 0
        self.marketGlobal = Market()
        self.marketGlobalPast = Market()
        self.marketLocal = None
        self.code = 0
        self.ownedRegionCodesArray = []

    def getCultureCode(self):
        return self.cultureCode

    def setCultureCode(self, vint):
        self.cultureCode = vint

    def getCode(self):
        return self.code

    def setCode(self, vint):
        self.code = vint

    def deleteOwnedRegionCodes(self, vint):
        for i in range(len(self.ownedRegionCodesArray)):
            if(self.ownedRegionCodesArray[i] == vint):
                del(self.ownedRegionCodesArray[i])
                break

    def addOwnedRegionCodes(self, vint):
        self.ownedRegionCodesArray.append(vint)

    def getOwnedRegionCodesArray(self):
        return self.ownedRegionCodesArray
