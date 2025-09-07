



from data_model.core.person_list.PersonList import PersonList
from data_model.core.general.core.coordinate.Coordinate import Coordinate

class RegionPDT:

    def __init__(self):
        self._coordinate = Coordinate()
        self._personList = PersonList()
        self._relief = 0
        self._windRegime = 0
        self._temperatureRegime = 0
        self._globalZone = 0
        self._currentTime = 0
        self._codeInt = 0
        self._culture = 0
        self._biome = 0
        self._isInhabited = False
        self._typeSoil = 0
        self._actualClime = 0
        self._actualTemperature = 0
        self._actualWindSpeed = 0
        self._latitude = 0
        self._longitude = 0
        self._name = "no_name"
        self._ownerCode = 0
        return

#*** ACCESSORS ************************************************************************

    def getCoordinate(self):
        return self._coordinate

    def setCoordinate(self, coordinate):
        self._coordinate = coordinate

    def getPersonList(self):
        return self._personList

    def setPersonList(self, personList):
        self._personList = personList

    def getRelief(self):
        return self._relief

    def setRelief(self, vInt):
        self._relief = vInt

    def getWindRegime(self):
        return self._windRegime

    def setWindRegime(self, vInt):
        self._windRegime = vInt

    def getTemperatureRegime(self):
        return self._temperatureRegime

    def setTemperatureRegime(self, vInt):
        self._temperatureRegime = vInt

    def getGlobalZone(self):
        return self._globalZone

    def setGlobalZone(self, vInt):
        self._globalZone = vInt

    def getCurrenTime(self):
        return self._currentTime

    def setCurrentTime(self, vInt):
        self._currentTime = vInt

    def getCodeInt(self):
        return self._codeInt

    def setCodeInt(self, vInt):
        self._codeInt = vInt

    def getCulture(self):
        return self._culture

    def setCulture(self, vInt):
        self._culture = vInt

    def getIsInhabited(self):
        return self._isInhabited

    def setIsInhabited(self, vBoolean):
        self._isInhabited = vBoolean

    def getTypeSoil(self):
        return self._typeSoil

    def setTypeSoil(self, vInt):
        self._typeSoil = vInt

    def getActualClime(self):
        return self._actualClime

    def setActualClime(self, vInt):
        self._actualClime = vInt

    def getActualTemperature(self):
        return self._actualTemperature

    def setActualTemperature(self, vInt):
        self._actualTemperature = vInt

    def getActualWindSpeed(self):
        return self._actualWindSpeed

    def setActualWindSpeed(self, vInt):
        self._actualWindSpeed = vInt

    def getLatitude(self):
        return self._latitude

    def setLatitude(self, vint):
        self._latitude = vint

    def getLongitude(self):
        return self._longitude

    def setLongitude(self, vint):
        self._longitude = vint

    def getName(self):
        return self._name

    def setName(self, vstring):
        self._name = vstring

    def getOwnerCode(self):
        return self._ownerCode

    def setOwnerCode(self, vint):
        self._ownerCode = vint

    def getBiome(self):
        return self._biome

    def setBiome(self, vint):
        self._biome = vint

#*************************************************************************************
