


from data_access.core.building_data.BuildingEntity import BuildingEntity
from data_access.core.keys_data.KeysData import KeysData

from data_access.core.building_data.app.Building0 import Building0
from data_access.core.building_data.app.Building1 import Building1
from data_access.core.building_data.app.Building2 import Building2
from data_access.core.building_data.app.Building3 import Building3
from data_access.core.building_data.app.Building4 import Building4
from data_access.core.building_data.app.Building5 import Building5
from data_access.core.building_data.app.Building6 import Building6
from data_access.core.building_data.app.Building7 import Building7
from data_access.core.building_data.app.Building8 import Building8
from data_access.core.building_data.app.Building9 import Building9
from data_access.core.building_data.app.Building10 import Building10
from data_access.core.building_data.app.Building11 import Building11
from data_access.core.building_data.app.Building12 import Building12
from data_access.core.building_data.app.Building13 import Building13
from data_access.core.building_data.app.Building14 import Building14

class BuildingData:

    BUILDING_KEYS = KeysData().getBuildingKeysMap()

    def __init__(self):
        self.buildingCollection = dict()
        self.addBuilding(Building0())
        self.addBuilding(Building1())
        self.addBuilding(Building2())
        self.addBuilding(Building3())
        self.addBuilding(Building4())
        self.addBuilding(Building5())
        self.addBuilding(Building6())
        self.addBuilding(Building7())
        self.addBuilding(Building8())
        self.addBuilding(Building9())
        self.addBuilding(Building10())
        self.addBuilding(Building11())
        self.addBuilding(Building12())
        self.addBuilding(Building13())
        self.addBuilding(Building14())
        return

    def addBuilding(self, building):
        self.buildingCollection[building.type] = building
