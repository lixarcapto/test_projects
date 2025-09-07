


from data_access.core.building_data.BuildingEntity import BuildingEntity

class NoneBLD(BuildingEntity):

    def __init__(self):
        super().__init__()
        self.typeCode = "none"
        self.timeToBuild = 3
        self.health = 100
        self.addRequirement("global", "soft_board", 2)
        self.addRecipe("craft_basic_tool")
        return
