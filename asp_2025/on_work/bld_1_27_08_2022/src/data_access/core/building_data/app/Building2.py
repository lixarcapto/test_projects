


from data_access.core.building_data.BuildingEntity import BuildingEntity

class Building2(BuildingEntity):

    def __init__(self):
        super().__init__()
        self.type = "flax-farm"
        self.timeToBuild = 3
        self.health = 100
        self.addRequirement("global", "board-bunch", 2)
        self.recipeTypeInt = BuildingEntity.RECIPES_KEYS["trunk"]
        return
