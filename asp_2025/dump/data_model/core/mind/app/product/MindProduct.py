

from data_model.core.general.core.date.Date import Date
from data_model.core.mind.core.relation_list.RelationList import RelationList

class MindProduct:

    LIMIT_RELATION = 100
    LIMIT_PRACTICE = 10

    def __init__(self):
        self._profession = 0
        self._skillMatrix = None
        self._skillFavoritArray = []
        self._skillDisgustArray = []
        #information
        self._name = "none_name"
        self._secondName = "none_secondname"
        self._lastName = "none_lastname"
        self._secondLastName = "none_secondlastname"
        self._nickname = "none_nickname"
        self._codeInt = 0
        self._currentResidence = 0
        self._currentDateWritten = ""
        #ideas
        self._culture = 0
        self._lenguage = 0
        #place
        self._whatTerrainIsItOn = 0
        #property
        self._titlesArray = []
        self._isItAnAvatar = False
        self._caste = 0
        #messages
        self._causeOfDeath = "none"
        #dates
        self._bornDate = Date()
        self._deathDate = Date()
        self._needToIntroduceHimself = True
        self._visionMemories = "none"
        self._physicalSelfDescription = "none"
        self._soundDescriptions = "none"
        self.relationList = RelationList()

#PsychologicalTraits ----------------------------------------------------------------------------

        #memory
        #----MEMORIA DATOS -----------------------------------------------------
        self.sensationsDataArray = []
        self.hearingDataArray = []
        self.visionDataArray = []
        self.sussoDataArray = []
        self.actualDate = None
        #---------------------------------------------
        self.dailyEventList = []
        self.todayHistory = ""
        self.history = []
        self._desition = 0
        self.desitionDataCode = 0
        self._desitionGoal = 0
        self.emotionalState = 0
        self.thoughtsArray = []
        self.favortiteTopics = []
        self.hatedTopics = []
        self.wasPresented = False
        #States
        self.moodValue = 0

        self.uniqueTraitsArray = []

#NEEDS -----------------------------------------------------------------------------------

        self.hasHunger = False
        self.hasThirst = False
        self.isCold = False
        self.isHot = False
        self.isTired = False
        self.hasPain = False
        self.isBored  = False
        self.feelsLonely = False
        self.noHome = False
        self.dontHaveACar = False
        self.isSick = False
        self.cantBreatheRight = False
        self.hasJob = False
        self.hasSocialCircle = False
        self.hasReligion = False
        self.hasSexualIntimate = False
        self.hasFreeTime = False
        self.hasClothes = False
        #food
        self.hasFruit = False
        self.hasVegetable = False
        self.hasCarbohydrate = False
        self.hasProtein = False
        self.hasDairy = False
        #product needs
        self.hasFlavoring = False
        self.hasToiletPaper = False
        self.hasGasoline = False
        self.hasWaterService = False
        #basic services
        self.hasInternetAccess = False
        self.hasLighting = False
        self.hasGasService = False
        self.hasAPension = False
        self.hasHealthInsurance = False
        self.hasElectricService = False
        self.hasDrainageService = False
        self.hasDrinkingWaterService = False
#SKILLS -------------------------------------------------------------------------------
        #psycologist traits maximo 5 minimo 0
        self.conservatism = 2
        self.serenity = 2
        self.communication = 2
        self.selfcontrol = 2
        self.intelligence = 2
        self.memory = 2
        self.courage =  2
        self.proactivity = 2
        self.force = 2
        self.faith = 2
        self.mentalStability = 2
        self.empathy =  2
        self.sociability = 2
        self.realism = 2
        self.painTolerance = 2
#------------------------------------------------------------------------------------------

    def getName(self):
        return self._name

    def setName(self, text):
        self._name = text

    def setSecondName(self, text):
        self._secondName = text

    def getSecondName(self):
        return self._secondName

    def getLastName(self):
        return self._lastName

    def setLastName(self, lastName):
        self._lastName = lastName

    def getSecondLastName(self):
        return self._secondLastName

    def setSecondLastName(self, secondLastName):
        self._secondLastName = secondLastName

    def getNickname(self):
        return self._nickname

    def setNickname(self, nickname):
        self._nickname = nickname

    def setCodeInt(self, codeInt):
        self._codeInt = codeInt

    def getCodeInt(self):
        return self._codeInt

    def getCurrentResidence(self):
        return self._currentResidence

    def setCurrentResidence(self, currentResidence):
        self._currentResidence = currentResidence

    def getCurrentDateWritten(self):
        return self._currentDateWritten

    def setCurrentDateWritten(self, currentDateWritten):
        self._currentDateWritten = currentDateWritten

    def getAge(self):
        return self._age

    def setAge(self, age):
        self._age = age

    def getCulture(self):
        return self._culture

    def setCulture(self, culture):
        self._culture = culture

    def getLenguage(self):
        return self._lenguage

    def setLenguage(self, lenguage):
        self._lenguage = lenguage

    def getBornDate(self):
        return self._bornDate

    def setBornDate(self, date):
        self._bornDate = date

    def getDeathDate(self):
        return self._deathDate

    def setDeathDate(self, date):
        self._deathDate = date

    def getWhatTerrainIsItOn(self):
        return self._whatTerrainItIsOn

    def setWhatTerrainIsItOn(self, valueInt):
        self._whatTerrainItIsOn = valueInt

    def getTitlesArray(self):
        return self._titlesArray

    def setTitlesArray(self, titlesArray):
        self._titlesArray = titlesArray

    def getIsItAnAvatar(self):
        return self._isItAnAvatar

    def setIsItAnAvatar(self, valueBoolean):
        self._isItAnAvatar = valueBoolean

    def getCaste(self):
        return self._caste

    def setCaste(self, valueInt):
        self._caste = valueInt

    def getCauseOfDeath(self):
        return self._causeOfDeath

    def setCauseOfDeath(self, valueString):
        self._causeOfDeath = valueString

    def getNeedToIntroduceHimself(self):
        return self._needToIntroduceHimself

    def setNeedToIntroduceHimself(self, valueBoolean):
        self._needToIntroduceHimself = valueBoolean

    def getVisionMemories(self):
        return self._visionMemories

    def setVisionMemories(self, valueString):
        self._visionMemories = valueString

    def getPhysicalSelfDescription(self):
        return self._physicalSelfDescription

    def setPhysicalSelfDescription(self, valueString):
        self._physicalSelfDescription = valueString

    def getSoundDescription(self):
        return self._soundDescriptions

    def setSoundDescription(self, valueString):
        self._soundDescriptions = valueString

    def getDesitionCode(self):
        return self._desition

    def setDesitionCode(self, vint):
        self._desition = vint

    def getDesitionGoal(self):
        return self._desitionGoal

    def setDesitionGoal(self, vint):
        self._desitionGoal = vint
