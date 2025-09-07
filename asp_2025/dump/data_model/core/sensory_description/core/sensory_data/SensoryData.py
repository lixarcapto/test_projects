


from basic.Basic import Basic
from data_access.DataAccess import DataAccess

class SensoryData:

    FORMAT_MAP = None

    def __init__(self, type, format, power):
        array = ["image", "sound", "smell", "sensation"]
        SensoryData.FORMAT_MAP = Basic().convertArrayToMap(array)
        self.type = 0
        self.format = SensoryData.FORMAT_MAP[format]
        self.power = 0
        return
