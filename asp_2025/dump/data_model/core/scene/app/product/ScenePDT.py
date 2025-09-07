


#from data_model.app.market_lib.MarketGlobal import MarketGlobal
from data_model.core.world.World import World
from data_model.core.general.core.date.Date import Date

class ScenePDT:

    def __init__(self):
        self._currentMode = 0
        #self._marketGlobal = MarketGlobal()
        self._world =  World()
        self._date = Date()
        self._protagonistCode = 0

    def getCurrentMode(self):
        return self._currentMode

    def setCurrentMode(self, vint):
        self._currentMode = vint

    def getWorld(self):
        return self._world

    def setWorld(self, world):
        self._world = world

    def getDate(self):
        return self._date

    def setDate(self, date):
        self._date = date

    def getProtagonistCode(self):
        return self._protagonistCode

    def setProtagonistCode(self, vint):
        self._protagonistCode = vint
