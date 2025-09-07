


from data_access.core.building_data.BuildingEntity import BuildingEntity

class PublicWaterBLD(BuildingEntity):

    def __init__(self):
        super().__init__()
        self.type = "public_water"
        self.timeToBuild = 3
        self.health = 100
        self.addRequirement("global", "soft_board", 2)
        self.addRecipe("bottle_water")
        return
