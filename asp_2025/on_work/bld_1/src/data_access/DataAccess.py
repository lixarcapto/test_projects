



from data_access.core.keys_data.KeysData import KeysData
from data_access.core.building_data.BuildingData import BuildingData
from data_access.core.translation.Translation import Translation
from data_access.core.recipes_collection.RecipesCollection import RecipesCollection
from data_access.core.resources_collection.ResourceCollection import ResourceCollection

class DataAccess:

    def getKeysData(self):
        return KeysData()

    def getTranslation(self):
        return Translation()

    def getBuildingData(self):
        return BuildingData()

    def obtainRecipesCollection(self):
        return RecipesCollection()

    def getResourceCollection(self):
        return ResourceCollection()
