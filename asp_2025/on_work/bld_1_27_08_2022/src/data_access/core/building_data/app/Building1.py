


from data_access.core.building_data.BuildingEntity import BuildingEntity

class Building1(BuildingEntity):

    def __init__(self):
        super().__init__()
        self.type = "craft-workshop"
        self.timeToBuild = 3
        self.health = 100
        self.addRequirement("global", "trunk-bunch", 2)
        self.recipeTypeInt = BuildingEntity.RECIPES_KEYS["tool-wood"]
        return
