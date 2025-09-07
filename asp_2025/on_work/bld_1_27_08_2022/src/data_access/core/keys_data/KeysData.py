


from basic.Basic import Basic
from data_access.core.keys_data.app.data.MarketGlobalKeys import MarketGlobalKeys
from data_access.core.keys_data.app.data.MarketLocalKeys import MarketLocalKeys
from data_access.core.keys_data.app.data.ProfessionKeys import ProfessionKeys
from data_access.core.keys_data.app.data.BuildingKeys import BuildingKeys
from data_access.core.keys_data.app.data.RecipesKeys import RecipesKeys
from data_access.core.keys_data.app.data.ResourcesKeys import ResourcesKeys

class KeysData:

    def __init__(self):
        return

    def getMarketGlobalKeysMap(self):
        array = MarketGlobalKeys().INNER
        return Basic().convertArrayToMap(array)

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

    def getResourcesTypeMap(self):
        array = ResourcesKeys().inner
        return Basic().convertArrayToMap(array)
