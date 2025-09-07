


#task
from data_model.app.body_lib.app.task.RandomizeCultureTraitsTk import RandomizeCultureTraitsTk
from data_model.app.body_lib.app.task.HaveSexTk import HaveSexTk
from data_model.app.body_lib.app.task.EatProductTk import EatProductTk
from data_model.app.body_lib.app.task.PerformMetabolismTk import PerformMetabolismTk
from data_model.app.body_lib.app.task.WritePhysicalDescriptionTk import WritePhysicalDescriptionTk
#product
from data_model.app.body_lib.app.product.PersonBodyProduct import PersonBodyProduct

from data_access.DataAccess import DataAccess
import random
from basic.Basic import Basic

class PersonBody:

    def __init__(self):
        self.inner = PersonBodyProduct()
        return

#MODIFIER -------------------------------------------------------------------------------------------

    def growHeight(self):
        if(self.inner.getHeight() <= self.inner.getLimitHeight()):
            height = self.inner.getHeight() + 1
            self.inner.setHeight(height)

    def growHair(self):
        if(self.inner.getHairStyle() <= PersonBodyProduct.HAIR_STYLE_QUANTITY -1):
            height = self.inner.getHairStyle() + 1
            self.inner.setHairStyle(height)
        if(self.inner.getFacialHairStyle() <= PersonBodyProduct.FACIAL_HAIR_STYLE_QUANTITY -1
        and self.inner.getGender() == 0):
            height = self.inner.getFacialHairStyle() + 1
            self.inner.setFacialHairStyle(height)
        elif(self.inner.getFacialHairStyle() <= 2
        and self.inner.getGender() == 1):
            height = self.inner.getFacialHairStyle() + 1
            self.inner.setFacialHairStyle(height)

    def generateRaceByCulture(self, culture):
        array = None
        racesByCulture = DataAccess().getRacesByCultureData()
        array = racesByCulture.RACES_BY_CULTURE_ARRAY[culture]
        return Basic().randomizeIntFromArray(array)

    def randomizeBody(self, culture):
        randomizeCultureTraits = RandomizeCultureTraitsTk()
        personKeys = DataAccess().getPersonData()
        race = self.generateRaceByCulture(culture)
        self.inner.setRace(race)
        ageRandom = random.randint(personKeys.AGE.TEEN, personKeys.AGE.LIMIT)
        self.inner.setAgeCode(ageRandom)
        self.inner = randomizeCultureTraits.inner(self.inner)
        #si es mayor a joven tendra su tamaño maximo
        if(personKeys.AGE.YOUNG < ageRandom):
            self.inner.height = self.inner.limitHeight
        else:
            self.inner.height = 2

    def eatProduct(self, product):
        eatProduct = EatProductTk()
        self.inner = eatProduct.inner(self.inner)

    def haveSex(self, personBodyB):
        haveSex = HaveSexTk()
        return haveSex.inner(self.inner, personBodyB.inner)

    def performMetabolism(self):
        performMetabolism = PerformMetabolismTk()
        self.inner = performMetabolism.inner(self.inner)

    def writePhysicalDescription(self):
        writePhysicalDescription = WritePhysicalDescriptionTk()
        return writePhysicalDescription.inner(self.inner)

    def writeAge(self):
        return self.inner.getAge().writeAge()

    def takeTheBabyOut(self):
        self.inner.setIsPregnant(False)
        self.inner.setPregnantTime(0)
        babyBody = self.inner.getEmbryoBody()
        self.inner.setEmbryoBody(None)
        return babyBody

    def advanceOneDay(self):
        self.inner.age.advanceOneDay()
        self.performMetabolism()

    def doYearActions(self):
        self.growHair()
        self.growHeight()

#PHYISCAL TRAITS --------------------------------------------------------------------------------------

    def getWeight(self):
        return self.inner.weight

    def setWeight(self, valueInt):
        self.inner.weight = valueInt

    def getHeight(self):
        return self.inner.height

    def setHeight(self, valueInt):
        self.inner.height = valueInt

    def getAgeCode(self):
        return self.inner.getAgeCode()

    def setAgeCode(self, valueInt):
        self.inner.setAgeCode(valueInt)

    def getGender(self):
        return self.inner.gender

    def setGender(self, valueInt):
        self.inner.gender = valueInt

    def getHairStyle(self):
        return self.inner.hairStyle

    def setHairStyle(self, valueInt):
        self.inner.hairStyle = valueInt

    def getHairColor(self):
        return self.inner.hairColor

    def setHairColor(self, valueInt):
        self.inner.hairColor = valueInt

    def getHairType(self):
        return self.inner.hairType

    def setHairType(self, valueInt):
        self.inner.hairType = valueInt

    def getEyeColor(self):
        return self.inner.eyeColor

    def setEyeColor(self, valueInt):
        self.inner.eyeColor = valueInt

    def getEyeType(self):
        return self.inner.eyeType

    def setEyeType(self, valueInt):
        self.inner.eyeType = valueInt

    def getEyeBrowType(self):
        return self.inner.eyeBrowType

    def setEyeBrowType(self, valueInt):
        self.inner.eyeBrowType = valueInt

    def getJawType(self):
        return self.inner.jawType

    def setJawType(self, valueInt):
        self.inner.jawType = valueInt

    def getNoseType(self):
        return self.inner.noseType

    def setNoseType(self, valueInt):
        self.inner.noseType = valueInt

    def getRace(self):
        return self.inner.race

    def setRace(self, valueInt):
        self.inner.valueInt = valueInt

    def getLimitHeight(self):
        return self.inner.limitHeight

    def setLimitHeight(self, valueInt):
        self.inner.limitHeight = valueInt

    def getMuscleMass(self):
        return self.inner.muscleMass

    def setMuscleMass(self, valueInt):
        self.inner.muscleMass = valueInt

#---------------------------------------------------------------------------------------
