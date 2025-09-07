


from data_access.core.resources_collection.Resource import Resource

class ForestHouseRES(Resource):

    def __init__(self):
        super().__init__()
        self.type = self.setResourceType("structure")
        self.key = "forest_house"
        self.supportedSoilArray = []
        self.supportedTemperatureMaximum = 0
        self.supportedTemperatureMinimum = 0
        self.humidityRequired = 0
        self.nutrientRequired = 0
        self.quantityMinimum = 10
        self.quantityMaximum = 100
        self.PHMaximum = 0
        self.PHMinimum = 0
        self.itIsMigrant = False
        self.deadImageName = "none"
        self.basicImageName = "region/resource/forest_house"
        self.winterImageName = "none"
        self.fallImageName = "none"
        self.stringImageName = "none"
        self.summerImageName = "none"
        self.nightImageName = "none"
        self.dayImageName = "none"
        self.feedingPosition = 0
        self.addRequirement("global", "soft_trunk", 0)
        self.addRecipe("cut_down_tree")
        return
