


from basic.Basic import Basic
from data_model.core.resource_collection.ResourceCollection import ResourceCollection
from data_model.core.market.Market import Market
from data_model.core.society.Society import Society

class RegionPack:

    def __init__(self):
        self.name = ""
        self.culture = "nordic"
        self.temperatureRegime = 0
        self.windRegime = 0
        self.humidityRegime = 0
        self.clime = 0
        self.temperature = 0
        self.humidity = 0
        self.soilType = 0
        self.nutrients = 0
        self.resourcesArray = []
        self.marketLocal = Market()
        self.society = Society()
        return

    def createResource(self, keyName):
        resourceCollection = ResourceCollection()
        return resourceCollection.inner[keyName]

    def addResource(self, resource):
        self.addResourceArray.append(resource)
