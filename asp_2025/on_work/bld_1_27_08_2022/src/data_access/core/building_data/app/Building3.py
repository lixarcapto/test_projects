


from data_access.core.building_data.BuildingEntity import BuildingEntity

class Building3(BuildingEntity):

    def __init__(self):
        super().__init__()
        self.type = "forest-house"
        self.timeToBuild = 3
        self.health = 100
        self.addRequirement("global", "board-bunch", 0)
        self.recipeTypeInt = BuildingEntity.RECIPES_KEYS["trunk"]
        return
