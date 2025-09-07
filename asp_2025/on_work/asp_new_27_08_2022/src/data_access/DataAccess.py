

from data_access.app.person.PersonKeysData import PersonKeysData
from data_access.app.culture.RacesByCulturesData import RacesByCulturesData
from data_access.app.culture.CultureKeyData import CultureKeyData
from data_access.app.names.NamesData import NamesData
from data_access.app.region.RegionData import RegionData
from data_access.app.market.GoodsKeysData import GoodsKeysData
from data_access.app.market.WorkData import WorkData
from data_access.app.person.object.PersonValues import PersonValues
from data_access.app.person.object.HairStyleKeyMapData import HairStyleKeyMapData
from data_access.app.person.object.FacialHairStyleKeyArrayData import FacialHairStyleKeyArrayData
from data_access.app.person.object.PersonMoodMatrixData import PersonMoodMatrixData

from basic.Basic import Basic

class DataAccess:

    def __init__(self):
        return

    def getPersonData(self):
        return PersonKeysData()

    def getNamesData(self):
        return NamesData()

    def getRacesByCultureData(self):
        return RacesByCulturesData()

    def getCultureKeyData(self):
        return CultureKeyData()

    def getRegionData(self):
        return RegionData()

    def getGoodsKeysData(self):
        return GoodsKeysData()

    def getWorkData(self):
        return WorkData()

    def getPersonMoodMatrix(self):
        return PersonMoodMatrixData().INNER

    def getBodyValuesData(self):
        return PersonValues()

    def getHairStyleKeyMap(self):
        data = HairStyleKeyMapData()
        return Basic().convertMatrixToMap(data.INNER)

    def getFacialHairStyleKeyMap(self):
        data = FacialHairStyleKeyArrayData()
        return Basic().convertMatrixToMap(data.INNER)
