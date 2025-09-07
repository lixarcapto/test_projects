


from basic.Basic import Basic
from data_access.core.resources_collection.app.entities.NoneRES import NoneRES
from data_access.core.resources_collection.app.entities.deposit.DepositSalineRES import DepositSalineRES
from data_access.core.resources_collection.app.entities.vegetable.ForestPineRES import ForestPineRES
from data_access.core.resources_collection.app.entities.deposit.DepositMagmaticRES import DepositMagmaticRES
from data_access.core.resources_collection.app.entities.structure.ForestHouseRES import ForestHouseRES
from data_access.core.resources_collection.app.entities.structure.CraftWorkshopRES import CraftWorkshopRES
from data_access.core.resources_collection.app.entities.structure.FarmRES import FarmRES
from data_access.core.resources_collection.app.entities.structure.LumberjackHouseRES import LumberjackHouseRES
from data_access.core.resources_collection.app.entities.structure.MineRES import MineRES
from data_access.core.resources_collection.app.entities.structure.PotteryWorkshopRES import PotteryWorkshopRES
from data_access.core.resources_collection.app.entities.structure.PublicWaterRES import PublicWaterRES
from data_access.core.resources_collection.app.entities.structure.RanchRES import RanchRES
from data_access.core.resources_collection.app.entities.structure.SawmillRES import SawmillRES
from data_access.core.resources_collection.app.entities.structure.SlaughterhouseRES import SlaughterhouseRES
from data_access.core.resources_collection.app.entities.structure.WindmillRES import WindmillRES



class ResourceCollection:

    """
        Contiene los recursos como edificios, depositos, vegetales
        y animales en una coleccion accedible como hashmap.
    """

    def __init__(self):
        self.inner = dict()
        self.addResource(NoneRES())
        self.addResource(DepositSalineRES())
        self.addResource(ForestPineRES())
        self.addResource(DepositMagmaticRES())
        self.addResource(ForestHouseRES())
        self.addResource(CraftWorkshopRES())
        self.addResource(FarmRES())
        self.addResource(LumberjackHouseRES())
        self.addResource(MineRES())
        self.addResource(PotteryWorkshopRES())
        self.addResource(PublicWaterRES())
        self.addResource(RanchRES())
        self.addResource(SawmillRES())
        self.addResource(SlaughterhouseRES())
        self.addResource(WindmillRES())
        return

    def addResource(self, resource):
        self.inner[resource.key] = resource

    def getResourceKeysMap(self):
        array = []
        for e in self.inner.keys():
            array.append(e)
        map = Basic().convertArrayToMap(array)
        return map

    def getResource(self, key):
        return self.inner[key]

    def getResourceByIndex(self, index):
        key = Basic().obtainKey(self.inner, index)
        return self.inner[key]
