



from data_model.core.scene.app.task.RandomizeProtagonistCodeTk import RandomizeProtagonistCodeTk
from data_model.core.scene.app.product.ScenePDT import ScenePDT
import random
from data_access.DataAccess import DataAccess

class Scene:

    def __init__(self):
        self.inner = ScenePDT()
        return

    def advanceTime(self):
        self.inner._world.advanceTime()

    def createNewGame(self):
        self.inner._world.createNewMap()

#--- PROTAGONIST INTERACTION ------------------------------------------------------

    def takeDesitionWithProtagonist(self, desitionCode):
        personProtagonist = self.inner._world.getPersonInWorld(
        self.inner.getProtagonistCode())
        personProtagonist.inner.setDesitionCode(desitionCode)
        self.inner._world.updatePersonInWorld(personProtagonist)

    def writeWhatTheProtagonistWillDo(self):
        personProtagonist = self.inner._world.getPersonInWorld(
        self.inner.getProtagonistCode())
        return personProtagonist.writeWhatWillDo()

    def writeTheFullNameOfProtagonist(self):
        personProtagonist = self.inner._world.getPersonInWorld(self.inner.getProtagonistCode())
        return personProtagonist.writeFullName()

    def takeDesitionGoal(self, desitionCode):
        personProtagonist = self.inner._world.getPersonInWorld(self.inner.getProtagonistCode())
        personProtagonist.person.inner.setDesitionGoal(desitionCode)
        self.inner._world.updatePersonInWorld(personProtagonist)

    def protagonistIsDead(self):
        person = self.inner._world.getPersonInWorld(self.inner.getProtagonistCode())
        if(person.person.getIsDeath()):
            return True
        return False

    def writeHistoryOfProtagonist(self):
        text = ""
        person = self.inner._world.getPersonInWorld(self.inner.getProtagonistCode())
        text += person.writeHistory()
        return text

    def writeDesitionsList(self):
        textArray = []
        translator = Translator()
        i = 0
        text = " "
        while(text != ""):
            text = translator.obtainDesition(i)
            textArray.append(text)
            i += 1
        return textArray

    def writeWhoYouWantToVisit(self):
        print("writeWhoYouWantToVisit")
        array = []
        person = self.inner._world.getPersonInWorld(self.inner.getProtagonistCode())
        relationList = person.getRelationList()
        if(not relationList.hasSomeRelation()):
            array.append("no tiene amigos ni parientes")
        else:
            n = 0
            personRelated = None
            codesArray = relationList.getRelationPersonCodesArray()
            for e in codesArray:
                personRelated = self.inner._world.getPersonInWorld(e)
                array.append(personRelated.writeFullName())
        return array

    def decideWhoYouWantToVisit(self, codeInt):
        None
        """
        person = self.inner._world.getPersonInWorld(self.inner.getProtagonistCode())
        person.person.inner.mind.inner.desitionDataCode = codeInt
        self.inner.regionMatrix.updatePersonInWorld(person)
        """

#--- SCENE START -----------------------------------------------------------------

    def randomizeProtagonistCode(self):
        randomizeProtagonistCode = RandomizeProtagonistCodeTk()
        self.inner = randomizeProtagonistCode.inner(self.inner)

    def actionsInADay(self):
        self.makeDesitions()
        self.inner._world.advanceOneDayToEachRegion(self.inner)

    def createNewGame(self):
        self.inner._world.createNewMap()
        self.randomizeProtagonistCode()
