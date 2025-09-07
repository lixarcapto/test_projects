

from data_access.core.keys_data.KeysData import KeysData
from data_access.core.resource_list.ResourceList import ResourceList
from data_access.core.recipes_collection.RecipesCollection import RecipesCollection

from basic.Basic import Basic

class Resource:

    RECIPES_KEYS = RecipesCollection().getRecipeKeysMap()

    FEEDING_POSITION = [
        "carnivorous",
        "herbivorous",
        "large carnivore",
        "great herbivore"
        ]

    TYPE_RESOURCE = [
        "deposit",
        "vegetable",
        "animal",
        "structure"
        ]

    def __init__(self):
        self.type = 0
        self.key = ""
        self.timeToBuild = 0
        self.resourceList = ResourceList() #requerimientos para construir
        self.recipesCodesArray = [] #recetas habilitadas para este edificio
        self.supportedSoilArray = []
        self.supportedTemperatureMaximum = 0
        self.supportedTemperatureMinimum = 0
        self.humidityRequired = 0
        self.nutrientRequired = 0
        self.quantityMinimum = 0
        self.quantityMaximum = 0
        self.PHMaximum = 0
        self.PHMinimum = 0
        self.itIsMigrant = False
        self.deadImageName = "none"
        self.basicImageName = "none"
        self.winterImageName = "none"
        self.fallImageName = "none"
        self.stringImageName = "none"
        self.summerImageName = "none"
        self.nightImageName = "none"
        self.dayImageName = "none"
        self.feedingPosition = 0
        return

    #STRUCTURE METHODS------------------------------------------------------

    def getRecipe(self, index):
        return Basic().indexFromMap(Resource.RECIPES_KEYS, index)

    def addRecipe(self, key):
        self.recipesCodesArray.append(Resource.RECIPES_KEYS[key])

    def hasRecipe(self, vint):
        return Basic().arrayHasInt(self.recipesCodesArray, vint)

    def addRequirement(self, location, keyResource, quantity):
        self.resourceList.addResource(location, keyResource, quantity)

    def canBeBuilt(self, market):
        return market.haveTheProducts(self.resourceList.INNER)

    def buildIt(self, market):
        market.consumeProductMatrix(self.resourceList.INNER)
        return market

    #--------------------------------------------------------------------------

    def setFeedingPosition(self, feedingPosition):
        self.feedingPosition = Basic().indexFromArray(Resource.FEEDING_POSITION,
        feedingPosition)

    def setResourceType(self, vstring):
        self.type = Basic().indexFromArray(Resource.TYPE_RESOURCE, vstring)
