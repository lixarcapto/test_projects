



from data_access.core.keys_data.KeysData import KeysData
from data_access.core.building_data.BuildingData import BuildingData
from data_access.core.translation.Translation import Translation

class DataAccess:

    def getKeysData(self):
        return KeysData()

    def getTranslation(self):
        return Translation()

    def getBuildingData(self):
        return BuildingData()
