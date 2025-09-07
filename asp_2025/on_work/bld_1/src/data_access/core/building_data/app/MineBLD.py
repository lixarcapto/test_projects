


from data_access.core.building_data.BuildingEntity import BuildingEntity

class MineBLD(BuildingEntity):

    def __init__(self):
        super().__init__()
        self.type = "mine"
        self.timeToBuild = 3
        self.health = 100
        self.addRequirement("global", "soft_board", 2)
        self.addRequirement("global", "basic_tool", 1)
        self.addRecipe("magmatic_deposit")
        self.addRecipe("mine_sedimentary_deposit")
        self.addRecipe("produce_adobe")
        return
