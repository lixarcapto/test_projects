


from data_model.core.body.core.genes.Genes import Genes
from data_model.core.body.core.age.Age import Age
from data_model.core.body.core.system.System import System
from data_access.DataAccess import DataAccess
from data_model.core.battle.core.skill.Skill import Skill

class BodyProduct:

    SYSTEMS_QUANTITY = 20

    def __init__(self):
        self._genesMom = Genes()
        self._genesDad = Genes()
        self._genesThis = Genes()
        self._isPregnant = False
        self._pregnantTime = 0
        self._bodyEmbryo = None
        self._gender = 0
        self._hairStyle = 0
        self._facialHairStyle = 0
        self._weight = 0
        self._height = 0
        self._age = Age()
        self._race = 0
        #add news accessors
        self._muscleMass = 0 #streght
        self._fulfiledYears = False
        self._causeOfDeath = 0
        #Magical power--------------------------------------------------
        self._qiReserve = 0
        self._divineFavorReserve = 0
        #--- ESTADOS PRODUCTO DE LA SALUD ---------------------------------------
        self._brainEfficiency = 0
        self._changeInPhysicalAppearance = 0
        self._breathingResistance = 0 #aporta resistencia fisica
        self._cardiacEndurance = 0
        self._currentSkinTone = 0
        #--- INVENTORY --------------------------------------------------------
        self._clothing = None
        self._armor = None
        self._weapon = None
        self._accessory = None
        self._skill = Skill()
        #----------------------------------------------------------------------
        #States--------------------------------------------------------------------------------
        self._hasHypovolemicShock = False
        self._sepsis = False
        self._itIsPoisoned = False
        self._hasACardiacArrest = False
        self._extremePain = False #causa desmayos o ataque al corazon
        self._disablingPain = False #impide movimiento
        self._isDeath = False
        self._isSick = False
        self._isUnconscious = False
        self._isInACome = False
        self._deadDays = 0
        self._lackOfVitamin = False
        self._lackOfMineral = False
        self._itIsHungry = False
        self._itIsThirsty = False
        self._isDehydrated = False #extremo de la sed
        self._hasExhaustion = False
        self._areStarving = False
        self._isBleeding = False
        #--- VARIABLES DEL CUERPO ---------------------------------------------
        self._heartRate = 80
        self._temperatureCelsius = 20
        self._bodyTemperature = 20
        self._toxinsLevel = 0
        self._infectionLevel = 0
        self._painLevel = 0
        self._openWoundLevel = 0
        #--- CONSTANTES DEL CUERPO --------------------------------------------
        self._HEART_RATE_MAXIMUM = 100
        self._HEART_RATE_MINUM = 60
        self._TEMPERATURE_CELSIUS_MAXIMUM = 57
        self._TEMPERATURE_CELSIUS_MINIMUM = -5
        self._INFECTION_LEVEL_MAXIMUM = 4
        #--- informacion corporal ---------------------------------------------------
        #--- RESERVES ----------------------------------------------------------
        self._hepatocytesReserve = 10 #elimina toxinas, forman el higado
        self._whiteBloodCellsReserve = 10
        self._nutrientReserve = 10
        self._plateletsReserve = 10
        self._stemCellsReserve = 10
        self._redBloodCellsReserve = 10
        self._glucoseInBloodReserve = 10 #energy bar 1
        self._carbohydrateReserve = 10 #energy bar 2
        self._fatReserve = 10 #energy bar 3
        self._proteinReserve = 10
        self._mineralReserve  = 10
        self._vitaminReserve = 10
        self._waterReserve = 10
        self._energyReserve = 10
        self._wasteAccumulation = 10
        self._urineAccumulation = 10
        self._saltReserve = 10
        self._bloodReserve = 400
        self._bloodArray = []

        self.sensationsArray = []
        #systems --------------------------------------------------------------
        organTypeMap = DataAccess().getPersonKeys().getOrganTypeMap()
        self.systemMap = dict()
        self.systemMap["circulatory"] = System(organTypeMap["circulatory"])
        self.systemMap["higher_digestive"] = System(organTypeMap["higher_digestive"])
        self.systemMap["nervous"] = System(organTypeMap["nervous"])
        self.systemMap["brain"] = System(organTypeMap["brain"])
        self.systemMap["respiratory"] = System(organTypeMap["respiratory"])
        self.systemMap["endocrine"] = System(organTypeMap["endocrine"])
        self.systemMap["excretory"] = System(organTypeMap["excretory"])
        self.systemMap["lower_digestive"] = System(organTypeMap["lower_digestive"])
        self.systemMap["skin"] = System(organTypeMap["skin"])
        self.systemMap["mouth"] = System(organTypeMap["mouth"])
        self.systemMap["voice"] = System(organTypeMap["voice"])
        self.systemMap["vision"] = System(organTypeMap["vision"])
        self.systemMap["legs"] = System(organTypeMap["legs"])
        self.systemMap["arms"] = System(organTypeMap["arms"])
        self.systemMap["audition"] = System(organTypeMap["audition"])
        self.systemMap["bone"] = System(organTypeMap["bone"])
        self.systemMap["muscular"] = System(organTypeMap["muscular"])
        self.systemMap["reproductive"] = System(organTypeMap["reproductive"])
        self.systemMap["olfactory"] = System(organTypeMap["olfactory"])
        self.systemMap["middle_digestive"] = System(organTypeMap["middle_digestive"])
        self.systemMap["neck"] = System(organTypeMap["neck"])

        #health----------------------------------------------------------------------------------
        self._handHygiene = 3 #facilita enfermedades infecciosas
        self._internalTissueHealth = 3 #causa desangrado interno
        self._externalTissueHealth = 3 #causa desangrado externo
        self._circulatorySystemState = 3
        self._higherDigestiveSystemState = 3
        self._nervousSystemState = 3
        self._brainState = 3
        self._amountOfBloodToDie = 100 #porcentaje
        self._respiratorySystemState = 3
        self._endocrineSystemState = 3 #permite el crecimiento
        self._excretorySystemState = 3
        self._lowerDigestiveSystemState = 3
        self._skinState = 3
        self._teethState = 3
        self._voiceState = 3
        self._hygiene = 3 #causa escaras y problemas de piel
        self._hairState = 3 #causa piojos
        self._dentalHygiene = 3 #causa caries e infecciones
        self._visionState = 3
        self._legsState = 3
        self._armState = 3
        self._auditionState = 3
        self._bonesState = 3
        self._muscularSystemState = 3
        self._reproductiveSystemState = 3
        #diseases-------------------------------------------------------------------------------------
        self._hasCancerLevel = 0
        self._hasAIDS = True
        self._hasGonorrhea = True
        #-------------------------------------------------------------------------------------------
        self._embryo = None
        return

#*** ACCESSORS ***********************************************************************

    def getGenesMom(self):
        return self._genesMom

    def setGenesMom(self, genes):
        self._genesMom = genes

    def getGenesDad(self):
        return self._genesDad

    def setGenesDad(self, genes):
        self._genesDad = genes

    def getGenesThis(self):
        return self._genesThis

    def setGenesThis(self, genes):
        self._genesThis = genes

    def getGender(self):
        return self._gender

    def setGender(self, vInt):
        self._gender = vInt

    def setAgeCode(self, vint):
        self._age.setAge(vint)

    def getAgeCode(self):
        return self._age.getAge()

    def setRace(self, vint):
        self._race = vint

    def getRace(self):
        return self._race

    def getHeight(self):
        return self._height

    def setHeight(self, vint):
        self._height = vint

    def getWeight(self):
        return self._weight

    def setWeight(self, vint):
        self._weight = vint

    def getFacialHairStyle(self):
        return self._facialHairStyle

    def setFacialHairStyle(self, vint):
        self._facialHairStyle = vint

#---------------------------------------------------------------------------------------

    def getEmbryoBody(self):
        return self._embryo

    def setEmbryoBody(self, bodyProduct):
        self._embryo = bodyProduct

#ACCESSORS/STATES--------------------------------------------------------------------------------

    def getIsDeath(self):
        return self._isDeath

    def setIsDeath(self, valueBoolean):
        self._isDeath = valueBoolean

    def getIsSick(self):
        return self._isSick

    def setIsSick(self, valueBoolean):
        self._isSick = valueBoolean

    def getIsUnconscious(self):
        return self._isUnconscious

    def setIsUnconscious(self, valueBoolean):
        self._isUnconscious = valueBoolean

    def getIsInACome(self):
        return self._isInACome

    def setIsInACome(self, valueBoolean):
        self._isInACome = valueBoolean

    def getDeadDays(self):
        return self._deadDays

    def setDeadDays(self, valueInt):
        self._deadDays = valueInt

    def getIsPregnant(self):
        return self._isPregnant

    def setIsPregnant(self, vBoolean):
        self._isPregnant = vBoolean

    def getPregnantTime(self):
        return self._pregnantTime

    def setPregnantTime(self, vInt):
        self._pregnantTime = vInt

    def getHairStyle(self):
        return self._hairStyle

    def setHairStyle(self, vint):
        self._hairStyle = vint

#--- RESERVES ----------------------------------------------------------------------

    def getCarbohydrateReserve(self):
        return self._carbohydrateReserve

    def setCarbohydrateReserve(self, vInt):
        self.carbohydrateReserve = vInt

    def getProteinReserve(self):
        return self._proteinReserve

    def setProteinReserve(self, vInt):
        self._proteinReserve = vInt

    def getFatReserve(self):
        return self._fatReserve

    def setFatReserve(self, vint):
        self._fatReserve = vint

    def getMineralReserve(self):
        return self._mineralsReserve

    def setMineralReserve(self, vint):
        self._mineralsReserve = vint

    def getVitaminReserve(self):
        return self._vitaminReserve

    def setVitaminReserve(self, vint):
        self._vitaminReserve = vint

    def getWaterReserve(self):
        return self._waterReserve

    def setWaterReserve(self, vint):
        self._waterReserve = vint

    def getEnergyReserve(self):
        return self._energyReserve

    def setEnergyReserve(self, vint):
        self._energyReserve = vint

    def getWasteAccumulation(self):
        return self._wasteAccumulation

    def setWasteAccumulation(self, vint):
        self._wasteAccumulation = vint

    def getUrineAccumulation(self):
        return self._urineAccumulation

    def setUrineAccumulation(self, vint):
        self._urineAccumulation = vint
