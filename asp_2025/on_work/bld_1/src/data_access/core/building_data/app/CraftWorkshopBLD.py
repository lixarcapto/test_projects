


from data_access.core.building_data.BuildingEntity import BuildingEntity

class CraftWorkshopBLD(BuildingEntity):

    def __init__(self):
        super().__init__()
        self.type = "craft_workshop"
        self.timeToBuild = 3
        self.health = 100
        self.addRequirement("global", "soft_trunk", 2)
        self.addRecipe("craft_basic_tool")
        return
