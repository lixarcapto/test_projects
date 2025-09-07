


from basic.Basic import Basic
from data_access.core.keys_data.app.data.MarketGlobalKeys import MarketGlobalKeys
from data_access.core.keys_data.app.data.MarketLocalKeys import MarketLocalKeys
from data_access.core.keys_data.app.data.ProfessionKeys import ProfessionKeys
from data_access.core.keys_data.app.data.BuildingKeys import BuildingKeys
from data_access.core.keys_data.app.data.RecipesKeys import RecipesKeys
from data_access.core.keys_data.app.data.ResourcesKeys import ResourcesKeys
from data_access.core.keys_data.app.data.CultureKeys import CultureKeys
from data_access.core.keys_data.app.data.SoilTypeKeys import SoilTypeKeys

class KeysData:

    def __init__(self):
        return

    def getMarketGlobalKey(self, index):
        return MarketGlobalKeys().INNER[index]

    def getMarketGlobalIndex(self, key):
        return Basic().indexFromArray(MarketGlobalKeys().INNER, key)

    def getQuantityMarketGlobalKeys(self):
        return len(MarketGlobalKeys().INNER)

    def getCultureKey(self, index):
        return CultureKeys().inner[index]

    def getCultureIndex(self, key):
        return Basic().indexFromArray(CultureKeys().inner, key)

    def getQuantityCultureKeys(self):
        return len(CultureKeys().inner)

    def getMarketLocalKeysMap(self):
        array = MarketLocalKeys().INNER
        return Basic().convertArrayToMap(array)

    def getProfessionKeysMap(self):
        array = ProfessionKeys().INNER
        return Basic().convertArrayToMap(array)

    def getBuildingKeysMap(self):
        array = BuildingKeys().INNER
        return Basic().convertArrayToMap(array)

    def getRecipesKeysMap(self):
        array = RecipesKeys().inner
        return Basic().convertArrayToMap(array)

    def getSoilTypeKey(self, index):
        return SoilTypeKeys().inner[index]

    def getSoilTypeIndex(self, key):
        return Basic().indexFromArray(SoilTypeKeys().inner, key)

    def getQuantitySoilTypeKeys(self):
        return len(SoilTypeKeys().inner)

    def getSoilTypeMap(self):
        array = [
            "ground",
            "gravel",
            "sand",
            "peat",
            "salt",
            "limestone",
            "rock",
            "clay",
            "paved",
            "humus",
            "ash",
            "loamy"
        ]
        return Basic().convertArrayToMap(array)

    def getReliefKeysMap(self):
        array = [
            "deep-sea", #0
            "low-sea", #1
            "lowlands", #2
            "plain", #3
            "mountain", #4
            "plateau", #5
            "peak"  #6
        ]
        return Basic().convertArrayToMap(array)

    def getResourcesTypeMap(self):
        array = ResourcesKeys().inner
        return Basic().convertArrayToMap(array)
