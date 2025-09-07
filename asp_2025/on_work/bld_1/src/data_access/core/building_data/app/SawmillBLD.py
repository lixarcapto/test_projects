


from data_access.core.building_data.BuildingEntity import BuildingEntity

class SawmillBLD(BuildingEntity):

    def __init__(self):
        super().__init__()
        self.type = "sawmill"
        self.timeToBuild = 3
        self.health = 100
        self.addRequirement("global", "soft_trunk", 2)
        self.addRequirement("global", "basic_tool", 1)
        self.addRecipe("carve_trunk_for_board")
        
        return
