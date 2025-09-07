


from data_model.core.complementary_product.ComplementaryProduct import ComplementaryProduct

class CitizenTrigger:

    def __init__(self):
        self._keyName = ""
        self.complementaryProductConditionArray = []
        self.productEffectArray = []
        self.attributeEffectsArray = []
        self.maximumAttributeConditionArray = []
        self.minimumAttributeConditionArray = []
        self._satisfactionKey = ""
        self._dissatisfactionKey = ""
        self._triggerKeyEffectsArray = []
        self._category = ""
        return

    def setKeyName(self, vstring):
        self._keyName = vstring

    def getKeyName(self):
        return self._keyName

    def addTriggerKey(self, key):
        self._triggerKeyEffectsArray.append(key)

    def addMinimumAttributeCondition(self, key, valueInt):
        map = dict()
        map["key"] = key
        map["value"] = valueInt
        self.minimumAttributeConditionArray.append(map)

    def addMaximumAttributeCondition(self, key, valueInt):
        map = dict()
        map["key"] = key
        map["value"] = valueInt
        self.maximumAttributeConditionArray.append(map)

    def createComplementaryProduct(self, keyName):
        complementaryProduct = ComplementaryProduct()
        complementaryProduct.keyName = keyName
        return complementaryProduct

    """ añade un map a complementaryProductArray con el array
    de bienes y de servicios consumibles y sus valores modificables"""
    def addComplementaryProduct(self, complementaryProduct):
        self.complementaryProductConditionArray.append(complementaryProduct)

    def addProductEffect(self, key, value):
        map = dict()
        map["key"] = key
        map["value"] = value
        self.productEffectArray.append(value)

    def addAttributeEffect(self, key, value, duration):
        map = dict()
        map["key"] = key
        map["value"] = value
        map["duration"] = duration
        self.attributeEffectsArray.append(map)

    def setCategory(self, vstring):
        self._category = vstring

    def getCategory(self):
        return self._category
