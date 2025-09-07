


from data_access.core.building_data.BuildingEntity import BuildingEntity

class Building14(BuildingEntity):

    def __init__(self):
        super().__init__()
        self.type = "14"
        self.timeToBuild = 3
        self.health = 100
        self.addRequirement("global", "trunk-bunch", 2)
        self.addRequirement("global", "tool", 1)
        self.recipeTypeInt = BuildingEntity.RECIPES_KEYS["board"]
        return
