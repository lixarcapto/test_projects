


from data_access.core.building_data.BuildingEntity import BuildingEntity

class WindmillBLD(BuildingEntity):

    def __init__(self):
        super().__init__()
        self.type = "windmill"
        self.timeToBuild = 3
        self.health = 100
        self.addRequirement("global", "soft_board", 3)
        self.addRecipe("grind_wheat")
        return
