


from data_access.core.building_data.BuildingEntity import BuildingEntity

class RanchBLD(BuildingEntity):

    def __init__(self):
        super().__init__()
        self.type = "ranch"
        self.timeToBuild = 3
        self.health = 100
        self.addRequirement("global", "soft_board", 2)
        self.addRequirement("global", "basic_tool", 1)
        self.addRequirement("global", "straw", 2)
        self.addRecipe("raise_cows")
        return
