


from data_access.core.building_data.BuildingEntity import BuildingEntity

class ForestHouseBLD(BuildingEntity):

    def __init__(self):
        super().__init__()
        self.type = "forest_house"
        self.timeToBuild = 3
        self.health = 100
        self.addRequirement("global", "soft_trunk", 0)
        self.addRecipe("cut_down_tree")
        return
