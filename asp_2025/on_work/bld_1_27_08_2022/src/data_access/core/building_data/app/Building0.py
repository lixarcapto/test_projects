


from data_access.core.building_data.BuildingEntity import BuildingEntity

class Building0(BuildingEntity):

    def __init__(self):
        super().__init__()
        self.typeCode = BuildingEntity.BUILDING_KEYS["quarry"]
        self.timeToBuild = 3
        self.health = 100
        self.addRequirement("global", "trunk-bunch", 2)
        return
