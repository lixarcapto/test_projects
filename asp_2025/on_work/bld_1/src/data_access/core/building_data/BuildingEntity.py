


from data_access.core.keys_data.KeysData import KeysData
from data_access.core.resource_list.ResourceList import ResourceList
from basic.Basic import Basic
from data_access.core.recipes_collection.RecipesCollection import RecipesCollection

class BuildingEntity:

    RECIPES_KEYS = RecipesCollection().getRecipeKeysMap()

    def __init__(self):
        self.type = ""
        self.timeToBuild = 3
        self.health = 100
        self.resourceList = ResourceList()
        self.recipeTypeInt = 0
        self.recipesCodesArray = []
        return

    def getRecipe(self, index):
        return Basic().indexFromMap(BuildingEntity.RECIPES_KEYS, index)

    def addRecipe(self, key):
        self.recipesCodesArray.append(BuildingEntity.RECIPES_KEYS[key])

    def hasRecipe(self, vint):
        return Basic().arrayHasInt(self.recipesCodesArray, vint)

    def addRequirement(self, location, keyResource, quantity):
        self.resourceList.addResource(location, keyResource, quantity)

    def canBeBuilt(self, market):
        return market.haveTheProducts(self.resourceList.INNER)

    def buildIt(self, market):
        market.consumeProductMatrix(self.resourceList.INNER)
        return market
