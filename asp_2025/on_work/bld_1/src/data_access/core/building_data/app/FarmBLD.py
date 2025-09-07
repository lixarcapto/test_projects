


from data_access.core.building_data.BuildingEntity import BuildingEntity

class FarmBLD(BuildingEntity):

    def __init__(self):
        super().__init__()
        self.type = "farm"
        self.timeToBuild = 3
        self.health = 100
        self.addRequirement("global", "soft_board", 0)
        self.addRecipe("grow_flax")
        self.addRecipe("grow_wheat_farm")
        return
