


import random
from data_access.DataAccess import DataAccess
from data_model.core.world.World import World
from basic.Basic import Basic

class DataModel:

    def __init__(self):
        self.actualRegionSelected = 0
        self.actualNationSelected = 0
        self.actualDistrictSelected = 0
        self.directionImage = "/Users/luisd/OneDrive/Escritorio/"
        self.directionImage += "py_proyects/bld_1/res/image/"
        self.formatImage = ".png"
        self.world = World()
        return

    def advanceTime(self):
        self.world.advanceTime()

    def createNewMap(self):
        self.world.createNewMap()

    def calculeHappyPeople(self):
        return self.world.calculeHappyPeople()

    def writeMap(self):
        return self.world.writeRegionByCode(self.actualRegionSelected,
        self.actualDistrictSelected)

    def writeMarketValues(self, marketTabKey):
        return self.world.writeMarketValues(marketTabKey, self.directionImage,
        self.formatImage)

    def writePersonData(self):
        return self.world.writePersonDataByCode(self.actualRegionSelected)

    def obtainMessagesOnHold(self):
        return self.world.obtainMessagesOnHold()

    def build(self, type, locationY, locationX, recipe):
        self.world.buildInRegion(self.actualRegionSelected,
        type, locationY, locationX, recipe)

    def writeArmyData(self):
        return self.world.writeArmyData(self.actualRegionSelected)

    def recruitPersonInRegionByCode(self, codePerson):
        self.world.recruitPersonInRegionByCode(self.actualRegionSelected,
        codePerson)

    def writeWorldMap(self):
        return self.world.writeWorldMap()

    def writeNationData(self):
        return self.world.writeNationData()

    def writeBuildInformation(self):
        recipesCollection = DataAccess().obtainRecipesCollection()
        keysData = DataAccess().getKeysData()
        recipesKeysMap = recipesCollection.getRecipeKeysMap()
        resourceCollection = DataAccess().getResourceCollection()
        resourceKeysMap = resourceCollection.getResourceKeysMap()
        recipeCode = 0
        text = ""
        symbolTitle = "*" * 6
        resource = None
        key = ""
        index = 0
        for e in resourceCollection.inner.keys():
            resource = resourceCollection.getResource(e)
            text += symbolTitle + str(Basic().indexFromMap(resourceKeysMap, e))
            text += " " + resource.key + symbolTitle + "\n"
            text += "requeriments:  \n"
            for f in resource.resourceList.INNER:
                key = keysData.getMarketGlobalKey(f[1])
                text += " >> " + key + " = " + str(f[2]) + "\n"
            text += "recipes:  \n"
            for i in range(len(resource.recipesCodesArray)):
                recipeCode = resource.recipesCodesArray[i]
                print("recipeCode " + str(recipeCode))
                key = recipesCollection.getRecipeKey(recipeCode)
                index = recipesCollection.getRecipeIndex(key)
                text += " >> " + key + "(" + str(index) + ")\n"
            text += "\n"
        return text
