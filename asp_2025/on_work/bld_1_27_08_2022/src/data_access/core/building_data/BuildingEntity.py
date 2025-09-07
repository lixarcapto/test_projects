


from data_access.core.keys_data.KeysData import KeysData
from data_access.core.resource_list.ResourceList import ResourceList

class BuildingEntity:

    BUILDING_KEYS = KeysData().getBuildingKeysMap()
    RECIPES_KEYS = KeysData().getRecipesKeysMap()

    def __init__(self):
        self.type = ""
        self.timeToBuild = 3
        self.health = 100
        self.resourceList = ResourceList()
        self.recipeTypeInt = 0
        return

    def addRequirement(self, location, keyResource, quantity):
        self.resourceList.addResource(location, keyResource, quantity)

    def canBeBuilt(self, market):
        return market.haveTheProducts(self.resourceList.INNER)

    def buildIt(self, market):
        market.consumeProductMatrix(self.resourceList.INNER)
        return market
