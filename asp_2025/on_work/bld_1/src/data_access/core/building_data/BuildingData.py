


from data_access.core.building_data.BuildingEntity import BuildingEntity
from data_access.core.keys_data.KeysData import KeysData
from basic.Basic import Basic

from data_access.core.building_data.app.PublicWaterBLD import PublicWaterBLD
from data_access.core.building_data.app.CraftWorkshopBLD import CraftWorkshopBLD
from data_access.core.building_data.app.FarmBLD import FarmBLD
from data_access.core.building_data.app.ForestHouseBLD import ForestHouseBLD
from data_access.core.building_data.app.MineBLD import MineBLD
from data_access.core.building_data.app.NoneBLD import NoneBLD
from data_access.core.building_data.app.PotteryWorkshopBLD import PotteryWorkshopBLD
from data_access.core.building_data.app.RanchBLD import RanchBLD
from data_access.core.building_data.app.SawmillBLD import SawmillBLD
from data_access.core.building_data.app.WindmillBLD import WindmillBLD
from data_access.core.building_data.app.SlaughterhouseBLD import SlaughterhouseBLD

class BuildingData:

    BUILDING_KEYS = KeysData().getBuildingKeysMap()

    def __init__(self):
        self.buildingCollection = dict()
        self.addBuilding(PublicWaterBLD())
        self.addBuilding(CraftWorkshopBLD())
        self.addBuilding(FarmBLD())
        self.addBuilding(ForestHouseBLD())
        self.addBuilding(MineBLD())
        self.addBuilding(NoneBLD())
        self.addBuilding(PotteryWorkshopBLD())
        self.addBuilding(RanchBLD())
        self.addBuilding(SawmillBLD())
        self.addBuilding(WindmillBLD())
        self.addBuilding(SlaughterhouseBLD())
        return

    def addBuilding(self, building):
        self.buildingCollection[building.type] = building

    def getBuildingKeysMap(self):
        array = []
        for e in self.buildingCollection.keys():
            array.append(e)
        map = Basic().convertArrayToMap(array)
        return map

    def getBuildingKey(self, index):
        map = self.getBuildingKeysMap()
        return Basic().obtainKey(map, index)

    def getBuildingIndex(self, key):
        map = self.getBuildingKeysMap()
        return Basic().indexFromArray(map, key)

    def getQuantityBuildingKeys(self):
        return len(self.inner)
