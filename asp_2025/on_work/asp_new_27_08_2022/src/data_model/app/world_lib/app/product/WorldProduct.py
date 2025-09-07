


from data_model.app.market_lib.MarketGlobal import MarketGlobal
from data_model.app.world_lib.core.region_matrix.RegionMatrix import RegionMatrix
from data_model.app.general_lib.core.date.Date import Date

class WorldProduct:

    def __init__(self):
        self.currentMode = 0
        self.marketGlobal = MarketGlobal()
        self.regionMatrix =  RegionMatrix()
        self.date = Date()
        self.year = 1080
        self.month = 0
        self.day = 0
        self.week = 0
        self.yearDay = 1
        self.monthDay = 1
        self.protagonistCodeRegion = 0
        self.protagonistCode = 0
        self.lastHistoryText = ""
        self.completeHistory = ""
        self.wasPresented = False
        self.textToDraw = ""
        self.nextDateDayWrited = ""
        self.dateWrited = ""
