



class ResourcePack:

    def __init__(self):
        self._keyname = ""
        self._recipesEnabledArray = []
        self._goodsCostArray = []
        self._servicesCostArray = []
        self._materialKey = ""
        self._useQuantityMaximum = 0
        self._useQuantityMinimum = 0
        self._grouthTime = 0
        self._grouthQuantity = 0
        self._resourceClass = ""

    def setKeyname(self, vstring):
        self._keyName = vstring

    def getKeyname(self):
        return self._keyName

    def addRecipeKeyEnabled(self, vstring):
        self._recipesEnabledArray.append(vstring)

    def addGoodsKeyCost(self, vstring):
        self._goodsCostArray.append(vstring)

    def addServiceKeyCost(self, vstring):
        self._servicesCostArray.append(string)

    def setMaterialKey(self, vstring):
        self._materialKey = vstring

    def getMaterialKey(self):
        return self._materialKey

    def setUseQuantityMaximum(self, vint):
        self._useQuantityMaximum = vint

    def getUseQuantityMaximum(self):
        return self._useQuantityMaximum

    def setUseQuantityMinimum(self, vint):
        self._useQuantityMinimum = vint

    def getUseQuantityMinimum(self):
        return self._useQuantityMinimum

    def setGrouthTime(self, vint):
        self._grouthTime = vint

    def getGrouthTime(self):
        return self._grouthTime

    def setResourceClass(self, vstring):
        self.resourceClass = vstring

    def getResourceClass(self):
        return self.resourceClass

    def getGrouthQuantity(self):
        return self._grouthQuantity

    def setGrouthQuantity(self, vint):
        self._grouthQuantity = vint
