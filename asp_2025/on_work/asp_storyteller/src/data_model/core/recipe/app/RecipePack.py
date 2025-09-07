



class RecipePack:

    def __init__(self):
        self.keyname = ""
        self.goodsRequiredArray = []
        self.servicesRequiredArray = []
        self.goodsProducedArray = []
        self.servicesProducedArray = []
        self.tecnologyConditionArray = []
        self.extractedResources = []
        return

    def setKeyname(self, vstring):
        self.keyname = vstring

    def getKeyname(self):
        return self.keyname

    def addGoodsKeyRequired(self, vstring, value):
        map = dict()
        map["key"] = vstring
        map["value"] = value
        self.goodsRequiredArray.append(map)

    def addServicesKeyRequired(self, vstring, value):
        map = dict()
        map["key"] = vstring
        map["value"] = value
        self.servicesRequiredArray.append(map)

    def addGoodsKeyProduced(self, vstring, value):
        map = dict()
        map["key"] = vstring
        map["value"] = value
        self.goodsProducedArray.append(map)

    def addServicesKeyProduced(self, vstring, value):
        map = dict()
        map["key"] = vstring
        map["value"] = value
        self.servicesProducedArray.append(map)

    def addTecnologyCondition(self, vstring, value):
        map = dict()
        map["key"] = vstring
        map["value"] = value
        self.tecnologyConditionArray.append(map)

    def addExtractedResources(self, vstring, value):
        map = dict()
        map["key"] = vstring
        map["value"] = value
        self.extractedResources.append(map)
