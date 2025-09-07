


from data_access.core.building_data.BuildingEntity import BuildingEntity

class PotteryWorkshopBLD(BuildingEntity):

    def __init__(self):
        super().__init__()
        self.type = "pottery_workshop"
        self.timeToBuild = 3
        self.health = 100
        self.addRequirement("global", "soft_board", 1)
        self.addRequirement("global", "adobe_brick", 2)
        self.addRequirement("global", "basic_tool", 1)
        return
