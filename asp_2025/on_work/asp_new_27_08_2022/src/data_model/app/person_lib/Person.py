


from data_model.app.person_lib.app.task.InteractionHaveSexTk import InteractionHaveSexTk
from data_model.app.person_lib.app.product.PersonProduct import PersonProduct

from data_model.app.translator_lib.Translator import Translator

class Person:

    def __init__(self):
        self.inner = PersonProduct()
        return

# MUTATORS *********************************************************************************

    def writePhysicalDescription(self):
        return self.inner.body.writePhysicalDescription()

    def advanceOneDay(self, worldProduct, visionRegion):
        self.inner.body.advanceOneDay()
        if(self.inner.body.inner.age.checkFulfiledYears()):
            self.inner.body.doYearActions()
            self.inner.mind.inner.setNeedToIntroduceHimself(True)
        self.inner.mind.takeDesition()
        self.inner.mind.inner.setPhysicalSelfDescription(self.writePhysicalDescription())
        self.inner.mind.inner.setVisionMemories(visionRegion)
        dateWritten = worldProduct.date.writeDate()
        self.inner.mind.inner.setCurrentDateWritten(dateWritten)
        self.inner.mind.createHistory()

    def endDay(self):
        self.inner.mind.createHistory()

    def writeAge(self):
        return self.inner.body.writeAge()

    def takeTheBabyOut(self):
        return self.inner.body.takeTheBabyOut()

    def randomize(self, culture, regionPresentation):
        self.inner.mind.inner.setCulture(culture)
        self.inner.body.randomizeBody(culture)
        self.inner.mind.randomizeMentalTraits(culture, self.inner.body.getGender())
        return

    def writeHistory(self):
        text = ""
        for e in self.inner.mind.inner.history:
            text += e
        return text

    def writeFullName(self):
        return self.inner.mind.writeFullName()

    def writeWhatWillDo(self):
        translator = Translator()
        text = self.inner.mind.writeFullName() + " desidio "
        text += translator.obtainDesition(self.inner.mind.inner.desition)
        return text

    def writePresentation(self):
        text = ""
        text += self.inner.mind.writeFullName() + " "
        text += "era " + self.inner.body.writePhysicalDescription()
        return text

    def addDailyEvent(self, text):
        self.inner.mind.inner.todayHistory += text

    def haveSex(self, personB):
        interactionHaveSex = InteractionHaveSexTk()
        result = interactionHaveSex.inner(self.inner, personB.inner)
        self.inner = result[0]
        personB.inner = result[1]
        return personB



# ACCESSORS *********************************************************************************

    def getCoordinate(self):
        return self.inner.coordinate

    def setCoordinate(self, coordinate):
        self.inner.coordinate = coordinate

# ACCESSORS/BODY--------------------------------------------------------------------------------

    def getIsPregnant(self):
        return self.inner.body.inner.getIsPregnant()

    def getPregnantTime(self):
        return self.inner.body.inner.getPregnantTime()

    def getIsDeath(self):
        return self.inner.body.inner.getIsDeath()

    def getDeadDays(self):
        return self.inner.body.inner.getDeadDays()

# ACCESSORS/MIND------------------------------------------------------------------------------

    def getCodeInt(self):
        return self.inner.mind.inner.getCodeInt()

    def setCodeInt(self, valueInt):
        self.inner.mind.inner.setCodeInt(valueInt)

    def getCurrentResidence(self):
        return self.inner.mind.inner.getCurrentResidence()

    def setCurrentResidence(self, valueInt):
        self.inner.mind.inner.setCurrentResidence(valueInt)

    def setIsItAnAvatar(self, valueBoolean):
        self.inner.mind.inner.setIsItAnAvatar(valueBoolean)

    def setVisionMemories(self, valueString):
        self.inner.mind.inner.setVisionMemories(valueString)

    def getVisionMemories(self):
        return self.inner.mind.inner.getVisionMemories()

    def getDesition(self):
        return self.inner.mind.inner.desition

    def setDesition(self, codeInt):
        self.inner.mind.inner.desition = codeInt

    def getDesitionDataCode(self):
        return self.inner.mind.inner.desitionDataCode

    def setDesitionDataCode(self, codeInt):
        self.inner.mind.inner.desitionDataCode = codeInt

    def getRelationList(self):
        return self.inner.mind.inner.relationList

#---------------------------------------------------------------------------------------
