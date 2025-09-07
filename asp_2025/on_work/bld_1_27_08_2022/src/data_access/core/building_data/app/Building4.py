


from data_access.core.building_data.BuildingEntity import BuildingEntity

class Building4(BuildingEntity):

    def __init__(self):
        super().__init__()
        self.type = "lumberjack-house"
        self.timeToBuild = 3
        self.health = 100
        self.addRequirement("global", "board-bunch", 2)
        self.recipeTypeInt = BuildingEntity.RECIPES_KEYS["trunk"]
        return
