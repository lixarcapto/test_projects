



from basic.Basic import Basic
from data_access.core.keys_data.KeysData import KeysData
from data_access.core.recipes_collection.app.BottleWaterRCP import BottleWaterRCP
from data_access.core.recipes_collection.app.CraftBasicToolRCP import CraftBasicToolRCP
from data_access.core.recipes_collection.app.CutDownTreeRCP import CutDownTreeRCP
from data_access.core.recipes_collection.app.GrindWheatRCP import GrindWheatRCP
from data_access.core.recipes_collection.app.GrowFlaxRCP import GrowFlaxRCP
from data_access.core.recipes_collection.app.GrowWheatFarmRCP import GrowWheatFarmRCP
from data_access.core.recipes_collection.app.MagmaticDepositRCP import MagmaticDepositRCP
from data_access.core.recipes_collection.app.MineSedimentaryDepositRCP import MineSedimentaryDepositRCP
from data_access.core.recipes_collection.app.NoneRCP import NoneRCP
from data_access.core.recipes_collection.app.ProduceAdobeRCP import ProduceAdobeRCP
from data_access.core.recipes_collection.app.RaiseCowsRCP import RaiseCowsRCP
from data_access.core.recipes_collection.app.SlaughterCowRCP import SlaughterCowRCP
from data_access.core.recipes_collection.app.CarveTrunkForBoardRCP import CarveTrunkForBoardRCP

class RecipesCollection:

    recipesKeysMap = None

    def __init__(self):
        self.inner = dict()
        self.addRecipe(BottleWaterRCP())
        self.addRecipe(CraftBasicToolRCP())
        self.addRecipe(CutDownTreeRCP())
        self.addRecipe(GrindWheatRCP())
        self.addRecipe(GrowFlaxRCP())
        self.addRecipe(GrowWheatFarmRCP())
        self.addRecipe(MagmaticDepositRCP())
        self.addRecipe(MineSedimentaryDepositRCP())
        self.addRecipe(NoneRCP())
        self.addRecipe(ProduceAdobeRCP())
        self.addRecipe(RaiseCowsRCP())
        self.addRecipe(SlaughterCowRCP())
        self.addRecipe(CarveTrunkForBoardRCP())
        recipesKeysMap = self.getRecipeKeysMap()
        return

    def getRecipeKeysMap(self):
        array = []
        for e in self.inner.keys():
            array.append(e)
        map = Basic().convertArrayToMap(array)
        return map

    def getRecipeKey(self, index):
        map = self.getRecipeKeysMap()
        key = Basic().obtainKey(map, index)
        return key

    def getRecipeIndex(self, key):
        map = self.getRecipeKeysMap()
        index = Basic().indexFromMap(map, key)
        return index

    def getQuantityRecipesKeys(self):
        return len(self.inner)

    def existRecipe(self, key):
        return Basic().hasTheKey(recipesKeysMap, key)

    def getRecipeByKey(self, key):
        return self.inner[key]

    def getRecipeByCode(self, codeInt):
        n = 0
        for e in self.inner.keys():
            if(n == codeInt):
                return self.inner[e]
            n += 1

    def addRecipe(self, recipe):
        self.inner[recipe.key] = recipe
