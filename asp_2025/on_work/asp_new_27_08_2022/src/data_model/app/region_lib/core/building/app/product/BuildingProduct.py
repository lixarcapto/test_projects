
from components.data_model.firm.data.WorkData import WorkData
from components.data_model.firm.BuildingStatsCollectionData import BuildingStatsCollectionData

class Building:

    def createBuildingType(self, typeInt):
        buildingCollection = BuildingStatsCollectionData()
        e = buildingCollection[typeInt]
        self.buildingType = e.buildingType
        self.buildingJobOffert = e.buildingJobOffert
        self.buildingLife = e.buildingLife

    def __init__(self):
        self.buildingType = 0
        self.buildingJobOffert = 0
        self.buildingLife = 100
