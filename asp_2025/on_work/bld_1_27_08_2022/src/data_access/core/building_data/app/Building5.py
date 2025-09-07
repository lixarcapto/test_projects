


from data_access.core.building_data.BuildingEntity import BuildingEntity

class Building5(BuildingEntity):

    def __init__(self):
        super().__init__()
        self.type = "mine"
        self.timeToBuild = 3
        self.health = 100
        self.addRequirement("global", "board-bunch", 2)
        self.addRequirement("global", "tool", 1)
        self.recipeTypeInt = BuildingEntity.RECIPES_KEYS["magmatic-deposit"]
        return
