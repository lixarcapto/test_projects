


class Biome:

    def __init__(self):
        self.key = ""
        self.resourceList = []
        self.soilTypeList = []
        self.baseSoilType = ""
        return

    def setKey(self, vstring):
        self.key = vstring

    def getKey(self):
        return self.key

    def addResource(self, resourceKey, quantity):
        map = dict()
        map.append(resourceKey)
        map.append(quantity)
        self.resourceList.append(array)

    def addSoilType(self, soilTypeKey, quantity):
        map = dict()
        map.append(soilTypeKey)
        map.append(quantity)
        self.soilTypeList.append(array)

    def setBaseSoilType(self, vstring):
        self.baseSoilType = vstring

    def getBaseSoilType(self, vstring):
        return self.baseSoilType
