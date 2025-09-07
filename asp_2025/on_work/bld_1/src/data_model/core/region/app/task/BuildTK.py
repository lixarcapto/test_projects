

from data_access.DataAccess import DataAccess
from basic.Basic import Basic

class BuildTK:
    """
        Realiza la tarea de construir edificios en las regiones,
        comprobar si tiene los requisitos y configurar el edificio.
    """

    def __init__(self):
        self.recipesCollection = DataAccess().obtainRecipesCollection()
        self.resourceCollection = DataAccess().getResourceCollection()
        self.recipesKeysMap = self.recipesCollection.getRecipeKeysMap()
        self.resourceKeysMap = self.resourceCollection.getResourceKeysMap()

    def build(self, mapResult, buildingKey, locationY, locationX, recipe):
        terrain = None
        recipeCode = 0
        resource = None
        resource = self.resourceCollection.getResource(buildingKey)
        market = resource.buildIt(mapResult["market"])
        terrain = mapResult["regionPDT"].mapMatrix[locationY][locationX]
        terrain.inner.setResourceTypeInt(self.resourceKeysMap[buildingKey])
        terrain.inner.setResourceQuantityInt(100)
        recipeCode = self.recipesKeysMap[recipe]
        terrain.inner.setRecipeCodeInt(recipeCode)
        mapResult["regionPDT"].mapMatrix[locationY][locationX] = terrain
        return mapResult

    def checkErrors(self, mapResult, buildingKey, locationY,
    locationX, recipe):
        resource = None
        if(not Basic().hasTheKey(self.resourceKeysMap, buildingKey)):
            mapResult["regionPDT"].mailbox.addError("building doesnt exist",
            buildingKey)
            return mapResult
        if(not Basic().hasTheKey(self.recipesKeysMap, recipe)):
            mapResult["regionPDT"].mailbox.addError("recipe key doesnt exist",
            recipe)
            return mapResult
        resource = self.resourceCollection.getResource(buildingKey)
        if(not resource.hasRecipe(resource.getRecipe(recipe))):
            mapResult["regionPDT"].mailbox.addError("build cant do this recipe",
            recipe)
            return mapResult
        if(not resource.canBeBuilt(mapResult["market"])):
            mapResult["regionPDT"].mailbox.addError("cant build it", buildingKey)
            return mapResult
        return self.build(mapResult, buildingKey, locationY,
        locationX, recipe)

    def convertCodes(self, regionPDT, market, buildingKey, locationY,
    locationX, recipe):
        mapResult = dict()
        mapResult["market"] = market
        mapResult["regionPDT"] = regionPDT
        mapResult["regionPDT"].mailbox.start("build")
        if(Basic().areAllThoseNumbers(buildingKey)):
            print(buildingKey)
            buildingKey = Basic().obtainKey(self.resourceKeysMap,
            int(buildingKey))
        if(Basic().areAllThoseNumbers(recipe)):
            recipe = Basic().obtainKey(self.recipesKeysMap, int(recipe))
        return self.checkErrors(mapResult, buildingKey, locationY,
        locationX, recipe)

    def inner(self, regionPDT, market, buildingKey, locationY,
    locationX, recipe):
        return self.convertCodes(regionPDT, market, buildingKey, locationY,
        locationX, recipe)
