

from data_access.DataAccess import DataAccess
from data_access.core.resources_collection.ResourceCollection import ResourceCollection
from basic.Basic import Basic
import random

class RandomizeRegionTK:

    def inner(self, regionPDT, districtSize):
        terrain = None
        keysData = DataAccess().getKeysData()
        resourceTypeMap = DataAccess().getKeysData().getResourcesTypeMap()
        n = 0
        terrainsCounter = 0
        districtCounter = 0
        resource = None
        key = ""
        resourceCollection = ResourceCollection()
        for y in range(regionPDT.getSizeY()):
            for x in range(regionPDT.getSizeX()):
                terrain = regionPDT.mapMatrix[y][x]
                terrain.inner.setCode(n)
                terrain.inner.locationX = x
                terrain.inner.locationY = y
                randomNum = random.randint(0, keysData.getQuantitySoilTypeKeys() -1)
                terrain.inner.setSoilTypeInt(randomNum)
                #randomiza recurso
                randomNum = Basic().randomIndex(len(resourceCollection.inner))
                key = Basic().obtainKey(resourceCollection.inner, randomNum)
                resource = resourceCollection.inner[key]
                terrain.inner.setResourceTypeInt(randomNum)
                #randomiza cantidad de recurso
                resourceQuantity = random.randint(resource.quantityMinimum,
                resource.quantityMaximum)
                terrain.inner.setResourceQuantityInt(resourceQuantity)
                #
                terrain.inner.districtCode = districtCounter
                regionPDT.mapMatrix[y][x] = terrain
                if(terrainsCounter == districtSize):
                    districtCounter += 1
                    terrainsCounter = 0
                else:
                    terrainsCounter += 1
                n += 1
        return regionPDT
