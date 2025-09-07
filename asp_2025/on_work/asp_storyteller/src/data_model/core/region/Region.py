


from data_model.core.region.app.RegionPack import RegionPack
from data_model.core.resource_collection.ResourceCollection import ResourceCollection
from data_model.core.resource_structure.ResourceStructure import ResourceStructure
from data_model.core.recipe_collection.RecipeCollection import RecipeCollection
from data_model.core.society.Society import Society
from basic.Basic import Basic
import random

class Region:

    def __init__(self):
        self.inner = RegionPack()
        return

    def createResourceStructure(self, keyname):
        resourceCollection = ResourceCollection()
        resourceStructure = None
        resourceStructure = ResourceStructure()
        resourceData = resourceCollection.inner[keyname]
        resourceStructure.keyname = resourceData.inner.getKeyname()
        resourceStructure.producctionTime = resourceData.inner.getGrouthTime()
        randomInt = random.randint(resourceData.inner.getUseQuantityMinimum(),
        resourceData.inner.getUseQuantityMaximum())
        resourceStructure.remainingUse = randomInt
        return resourceStructure

    def randomizeRegion(self):
        resourceStructure = None
        resourceArray = [
            "forest_oak",
            "stone_massif",
            "hydrocarbons_deposit"
        ]
        resourceKey = ""
        for e in range(50):
            resourceKey = Basic().randomizeElementFromArray(resourceArray)
            resourceStructure = self.createResourceStructure(resourceKey)
            self.inner.resourcesArray.append(resourceStructure)
        # randomizar ciudadanos
        self.inner.society.createRandomSociety(self.inner.culture, 10)

    def writeResources(self):
        text = ""
        for resource in self.inner.resourcesArray:
            text += resource.keyname + " "
            text += str(resource.remainingUse) + "kms, "
        return text

    def performProductionProcesses(self, market):
        resourceCollection = ResourceCollection()
        resourceData = None
        keyname = ""
        maximumUsesReached = None
        recipe = None
        n = 0
        for resource in self.inner.resourcesArray:
            keyname = resource.keyname
            resourceData = resourceCollection.inner[keyname]
            if(resourceData.inner.getResourceClass() == "vegetable"
            or resourceData.inner.getResourceClass() == "animal"):
                # condiciones para el crecimiento
                maximumUsesReached = resource.remainingUse
                maximumUsesReached += resourceData.inner.getGrouthQuantity()
                if(resource.producctionTime <= 0
                and  maximumUsesReached <= resourceData.inner.getUseQuantityMaximum()):
                    resource.remainingUse += resourceData.inner.getGrouthQuantity()
                    resource.producctionTime = resourceData.inner.getGrouthTime()
                if(resource.producctionTime <= 0
                and  maximumUsesReached > resourceData.inner.getUseQuantityMaximum()):
                    resource.remainingUse = resourceData.inner.getUseQuantityMaximum()
                    resource.producctionTime = resourceData.inner.getGrouthTime()
                # avansar el tiempo de produccion
                if(resource.producctionTime > 0):
                    resource.producctionTime -= 1
            # hacer receta
            market = self.doitRecipe(n, resource, resourceData, market)
            n += 1
        return market

    def advanceOneDay(self, market, dateWrited):
        market = self.performProductionProcesses(market)
        market = self.inner.society.advanceOneDay(market,
        dateWrited)
        return market

    # no funciona  XXX
    def doitRecipe(self, indexResourceArray, resource, resourceData, market):
        # hacer receta
        hasResource = False
        if(resourceData.inner.getResourceClass() == "building"):
            if(resource.remainingUse > 0):
                resource.remainingUse -= 1
            # busca el recurso a explotar en la receta
            recipe = RecipeCollection().inner[resource.recipe]
            for e in recipe.inner.extractedResources:
                # busca si tiene el recurso indicado y lo modifica
                for i in range(len(self.inner.resourcesArray)):
                    if(e["key"] == self.inner.resourcesArray[i].keyname):
                        self.inner.resourcesArray[i].remainingUse -= e["value"]
                        hasResource = True
                        break
            if(hasResource):
                for goodsProduced in recipe.inner.goodsProducedArray:
                    market.productMap[goodsProduced["key"]] += goodsProduced["value"]
        return market

    def createBuilding(self, keyname, recipeKey):
        resourceCollection = ResourceCollection()
        resourceStructure = self.createResourceStructure(keyname)
        resourceStructure.recipe = recipeKey
        self.inner.resourcesArray.append(resourceStructure)

    def writeSocietyInformation(self):
        text = ""
        text += self.inner.society.writeCitizenInformation()
        return text
