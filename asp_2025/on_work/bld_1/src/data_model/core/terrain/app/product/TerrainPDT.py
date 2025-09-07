



class TerrainPDT:

    def __init__(self):
        self.code = 0
        self.districtCode = 0
        self.locationY = 0
        self.locationX = 0
        self.soilTypeInt = 0
        self.buildTypeInt = 0
        self.resourceTypeInt = 0
        self.resourceQuantityInt = 0
        self.recipeCodeInt = 0
        return

    def getCode(self):
        return self.code

    def setCode(self, vint):
        self.code = vint

    def getSoilTypeInt(self):
        return self.soilTypeInt

    def setSoilTypeInt(self, vint):
        self.soilTypeInt = vint

    def getBuildTypeInt(self):
        return self.buildTypeInt

    def setBuildTypeInt(self, vint):
        self.buildTypeInt = vint

    def getResourceTypeInt(self):
        return self.resourceTypeInt

    def setResourceTypeInt(self, vint):
        self.resourceTypeInt = vint

    def getResourceQuantityInt(self):
        return self.resourceQuantityInt

    def setResourceQuantityInt(self, vint):
        self.resourceQuantityInt = vint

    def getRecipeCodeInt(self):
        return self.recipeCodeInt

    def setRecipeCodeInt(self, vint):
        self.recipeCodeInt = vint
