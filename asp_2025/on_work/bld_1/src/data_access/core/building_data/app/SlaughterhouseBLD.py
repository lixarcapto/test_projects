


from data_access.core.building_data.BuildingEntity import BuildingEntity

class SlaughterhouseBLD(BuildingEntity):

    def __init__(self):
        super().__init__()
        self.type = "slaughterhouse"
        self.timeToBuild = 3
        self.health = 100
        self.addRequirement("global", "soft_board", 2)
        self.addRecipe("slaughter_cow")
        return
