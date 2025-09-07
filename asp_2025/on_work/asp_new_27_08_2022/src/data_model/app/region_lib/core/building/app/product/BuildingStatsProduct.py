
from components.static_data.StaticData import StaticData

class BuildingStatsProduct:

    WORK = StaticData().getWorkData()

    def __init__(self):
        self.type = 0
        self.jobOffertType = 0
        self.jobOffertQuantity = 0
        self.life = 100
        self.cost = 0
        self.timeToBuild = 0
        self.haveTemperatureRequirement = False
        self.temperatureMax = 0
        self.temperatureMin = 0
        self.resourceYieldTypeArray = []
        self.resourceRequiereTypeArray = []
