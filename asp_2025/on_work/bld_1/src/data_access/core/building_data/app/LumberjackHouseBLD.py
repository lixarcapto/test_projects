


from data_access.core.building_data.BuildingEntity import BuildingEntity

class LumberjackHouseBLD(BuildingEntity):

    def __init__(self):
        super().__init__()
        self.type = "lumberjack_house"
        self.timeToBuild = 3
        self.health = 100
        self.addRequirement("global", "soft_board", 2)
        self.addRecipe("cut_down_tree")
        return
