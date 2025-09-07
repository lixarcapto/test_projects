

from components.data_model.app.building.app.product.BuildingStatsProduct import BuildingStatsProduct

class BuildingLoggin(BuildingStatsProduct):

    def __init__(self):
        self.type = 1
        self.jobOffertType = BuildingStatsProduct.WORK.FORESTRY
        self.jobOffertQuantity = 1
        self.life = 100
        self.cost = 0
        self.timeToBuild = 0
        self.haveTemperatureRequirement = False
        self.temperatureMax = 0
        self.temperatureMin = 0
        self.resourceYieldTypeArray = []
        self.resourceRequiereTypeArray = []
