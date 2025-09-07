


from data_access.core.region_keys.app.data.DaysArrayData import DaysArrayData
from data_access.core.region_keys.app.data.MonthsArrayData import MonthsArrayData
from data_access.core.region_keys.app.data.ReliefArrayData import ReliefArrayData
from data_access.core.region_keys.app.data.TypeSoilArrayData import TypeSoilArrayData
from data_access.core.region_keys.app.data.BiomeArrayData import BiomeArrayData
from data_access.core.region_keys.app.data.TemperatureRegimeArrayData import TemperatureRegimeArrayData
from data_access.core.region_keys.app.data.WindSpeedArrayData import WindSpeedArrayData
from basic.Basic import Basic

class RegionKeys:

    def __init__(self):
        return

    def getReliefMap(self):
        array = ReliefArrayData().INNER
        return Basic().convertArrayToMap(array)

    def getMonthsMap(self):
        array = MonthsArrayData().INNER
        return Basic().convertArrayToMap(array)

    def getDaysMap(self):
        array = DaysArrayData().INNER
        return Basic().convertArrayToMap(array)

    def getTypeSoilMap(self):
        array = TypeSoilArrayData().INNER
        return Basic().convertArrayToMap(array)

    def getBiomeMap(self):
        array = BiomeArrayData().INNER
        return Basic().convertArrayToMap(array)

    def getTemperatureRegimeMap(self):
        array = TemperatureRegimeArrayData().INNER
        return Basic().convertArrayToMap(array)

    def getWindSpeedMap(self):
        array = WindSpeedArrayData().INNER
        return Basic().convertArrayToMap(array)
