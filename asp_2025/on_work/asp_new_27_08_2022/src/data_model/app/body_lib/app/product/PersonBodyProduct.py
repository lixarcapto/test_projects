

from data_access.DataAccess import DataAccess
from data_model.app.body_lib.core.age.Age import Age

class PersonBodyProduct:

    HAIR_STYLE_QUANTITY = len(DataAccess().getHairStyleKeyMap())
    FACIAL_HAIR_STYLE_QUANTITY = len(DataAccess().getFacialHairStyleKeyMap())

    def __init__(self):
        #Physicial traits----------------------------------------------------------------------------
        self.weight = 0
        self.height = 0
        self.age = 0
        self.gender = 0
        self.hairStyle = 0
        self.skinColor = 0
        self.hairColor = 0
        self.hairType = 0
        self.eyeColor = 0
        self.eyeType = 0
        self.eyeBrowType = 0
        self.jawType = 0
        self.noseType = 0
        self.race = 0
        self.muscleMass = 0
        self.limitHeight = 0
        self.facialHairStyle = 0
        self.age = Age()
        self.fulfiledYears = False
        self.causeOfDeath = ""

        #States--------------------------------------------------------------------------------
        self.isDeath = False
        self.isSick = False
        self.isUnconscious = False
        self.isInACome = False
        self.deadDays = 0
        self.isPregnant = False
        self.pregnantTime = 0
        #reserve---------------------------------------------------------------------------------
        self.carbohydrateReserve = 10
        self.proteinReserve = 10
        self.fatReserve = 10
        self.mineralsReserve  = 10
        self.vitaminReserve = 10
        self.waterReserve = 10
        self.energyReserve = 10
        self.wasteAccumulation = 10
        self.urineAccumulation = 10
        #health----------------------------------------------------------------------------------
        self.handHygiene = 3 #facilita enfermedades infecciosas
        self.internalTissueHealth = 3 #causa desangrado interno
        self.externalTissueHealth = 3 #causa desangrado externo
        self.circulatorySystemState = 3
        self.higherDigestiveSystemState = 3
        self.nervousSystemState = 3
        self.brainState = 3
        self.amountOfBloodToDie = 100 #porcentaje
        self.respiratorySystemState = 3
        self.endocrineSystemState = 3 #permite el crecimiento
        self.excretorySystemState = 3
        self.lowerDigestiveSystemState = 3
        self.skinState = 3
        self.teethState = 3
        self.voiceState = 3
        self.hygiene = 3 #causa escaras y problemas de piel
        self.hairState = 3 #causa piojos
        self.dentalHygiene = 3 #causa caries e infecciones
        self.visionState = 3
        self.legsState = 3
        self.armState = 3
        self.auditionState = 3
        self.bonesState = 3
        self.muscularSystemState = 3
        self.reproductiveSystemState = 3
        #diseases-------------------------------------------------------------------------------------
        self.hasCancerLevel = 0
        self.hasAIDS = True
        self.hasGonorrhea = True
        #-------------------------------------------------------------------------------------------
        self.embryo = None

#PHYISCAL TRAITS --------------------------------------------------------------------------------------

    def getFulfiledYears():
        return self.fulfiledYears

    def setFulfiledYears(valueBoolean):
        self.fulfiledYears = valueBoolean

    def getWeight(self):
        return self.weight

    def setWeight(self, valueInt):
        self.weight = valueInt

    def getHeight(self):
        return self.height

    def setHeight(self, valueInt):
        self.height = valueInt

    def getAgeCode(self):
        return self.age.getAge()

    def getAgeCode(self):
        return self.age.getAge()

    def setAgeCode(self, codeInt):
        self.age.setAge(codeInt)

    def getGender(self):
        return self.gender

    def setGender(self, valueInt):
        self.gender = valueInt

    def getHairStyle(self):
        return self.hairStyle

    def setHairStyle(self, valueInt):
        self.hairStyle = valueInt

    def getSkinColor(self):
        return self.skinColor

    def setSkinColor(self, valueInt):
        self.skinColor = valueInt

    def getHairColor(self):
        return self.hairColor

    def setHairColor(self, valueInt):
        self.hairColor = valueInt

    def getHairType(self):
        return self.hairType

    def setHairType(self, valueInt):
        self.hairType = valueInt

    def getEyeColor(self):
        return self.eyeColor

    def setEyeColor(self, valueInt):
        self.eyeColor = valueInt

    def getEyeType(self):
        return self.eyeType

    def setEyeType(self, valueInt):
        self.eyeType = valueInt

    def getEyeBrowType(self):
        return self.eyeBrowType

    def setEyeBrowType(self, valueInt):
        self.eyeBrowType = valueInt

    def getJawType(self):
        return self.jawType

    def setJawType(self, valueInt):
        self.jawType = valueInt

    def getNoseType(self):
        return self.noseType

    def setNoseType(self, valueInt):
        self.noseType = valueInt

    def getRace(self):
        return self.race

    def setRace(self, valueInt):
        self.race = valueInt

    def getLimitHeight(self):
        return self.limitHeight

    def setLimitHeight(self, valueInt):
        self.limitHeight = valueInt

    def getMuscleMass(self):
        return self.muscleMass

    def setMuscleMass(self, valueInt):
        self.muscleMass = valueInt

    def getFacialHairStyle(self):
        return self.facialHairStyle

    def setFacialHairStyle(self, valueInt):
        self.facialHairStyle = valueInt

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age

#---------------------------------------------------------------------------------------

    def getEmbryoBody(self):
        return self.embryo

    def setEmbryoBody(self, bodyProduct):
        self.embryo = bodyProduct

#ACCESSORS/STATES--------------------------------------------------------------------------------

    def getIsDeath(self):
        return self.isDeath

    def setIsDeath(self, valueBoolean):
        self.isDeath = valueBoolean

    def getIsSick(self):
        return self.isSick

    def setIsSick(self, valueBoolean):
        self.isSick = valueBoolean

    def getIsUnconscious(self):
        return self.isUnconscious

    def setIsUnconscious(self, valueBoolean):
        self.isUnconscious = valueBoolean

    def getIsInACome(self):
        return self.isInACome

    def setIsInACome(self, valueBoolean):
        self.isInACome = valueBoolean

    def getDeadDays(self):
        return self.deadDays

    def setDeadDays(self, valueInt):
        self.deadDays = valueInt

    def getIsPregnant(self):
        return self.isPregnant

    def setIsPregnant(self, valueBoolean):
        self.isPregnant = valueBoolean

    def getPregnantTime(self):
        return self.pregnantTime

    def setPregnantTime(self, valueInt):
        self.pregnantTime = valueInt
