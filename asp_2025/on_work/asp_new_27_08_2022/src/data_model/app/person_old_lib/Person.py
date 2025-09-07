


import random
#interface
import data_model.app.translator_lib.Translator as Translator
from data_model.app.person_list_lib.core.relation_list.RelationList import RelationList
from data_model.app.person_list_lib.core.thought.Thought import Thought
from data_model.app.market_lib.core.product.Product import Product
#products
#library person
from data_model.app.person_list_lib.core.person.app.product.PersonProduct import PersonProduct
#Task
from data_model.app.person_list_lib.core.person.app.task.mental_task.GetMoodNameTk import GetMoodNameTk
from data_model.app.person_list_lib.core.person.app.task.mental_task.CreateHistoryTk import CreateHistoryTk
from data_model.app.person_list_lib.core.person.app.task.show_task.WritePersonPresentationTk import WritePersonPresentationTk
from data_model.app.person_list_lib.core.person.app.task.randomize_values_task.RandomizePersonTk import RandomizePersonTk
from data_model.app.person_list_lib.core.person.app.task.show_task.WritePersonUpdateTk import WritePersonUpdateTk
from data_model.app.person_list_lib.core.person.app.task.show_task.WriteFullName import WriteFullName
from data_model.app.person_list_lib.core.person.app.task.mental_task.TakeDesitionTk import TakeDesitionTk
from data_model.app.person_list_lib.core.person.app.task.InteractionHaveSexTk import InteractionHaveSexTk
#
from basic.Basic import Basic

class Person:

    translator = Translator.Translator()

    def __init__(self):
        self.inner = PersonProduct()
        return

    def getRelationArray(self):
        return self.inner.relationList.relationArray

    def haveSex(self, personB):
        interactionHaveSex = InteractionHaveSexTk()
        result = interactionHaveSex.inner(self.inner, personB.inner)
        self.inner = result[0]
        personB.inner = result[1]
        return personB

    def obtainBooleanWithProbability(self, probability):
        result = random.randint(0, 100)
        if(result < probability):
            return True
        return False

    def analyseIfDie(self, sceneProduct):
        if(self.inner.body.isDeath):
            self.inner.traits.causeOfDeath = causeOfDeath
            date = self.inner.getDeathDate()
            date.setDay(sceneProduct.day)
            date.setMonth(sceneProduct.month)
            date.setYear(sceneProduct.year)
            self.inner.setDeathDate(date)
        return personProduct

    #BODIE EVENTS----------------------------------------------------------------

    def addThought(self, thoughtType, text):
        thought = ThoughtProduct()
        thought.thoughtType = thoughtType
        thought.remimber = text
        self.inner.traits.thoughtsArray.append(thought)

    def getMoodName(self, mood):
        getMoodName = GetMoodNameTk()
        return getMoodName.inner(mood)

    def goIntoCome(self):
        return

    #-----------------------------------------------------------------------------

    def buyProducts(self, marketGlobalProduct):
        consumeProduct = ConsumeProductTk()
        economicProduct = consumeProduct.inner(self.inner, marketGlobalProduct)
        self.inner = economicProduct.personProduct
        return marketGlobalProduct

    def addTitle(self,titleProduct):
        self.inner.traits.titlesArray.append(titleProduct)

    def addHistory(self, text):
        self.inner.traits.history.append(text)

    def writeHistory(self):
        text = ""
        for e in self.inner.psychologicalTraits.history:
            text += e
        return text

    def takeDesition(self):
        takeDesition = TakeDesitionTk()
        self.inner = takeDesition.inner(self.inner)

    def askWhoIs(self):
        return

    def askHowDoesItFeel(self):
        return

    def addRelation(self, value, personCode):
        self.inner.relationList.addRelation(value, personCode, "")

    def eatProduct(product):
        eatProduct = EatProductTk()
        self.inner = eatProduct.inner(self.inner, product)

    def randomizeMonthsDiseases(self):
        if(self.person.body.isProneToCancer):
            if(self.obtainBooleanWithProbability(10)):
                None
        return

    def writeWhatTheProtagonistWillDo(self):
        text = ""
        text += "al dia siguiente" + " "
        text += self.writeFullName() + "... "
        return text

    def performReasoning(self):
        performReasoning = PerformReasoningTk()
        self.inner = performReasoning.inner(self.inner)

    def performMetabolism(self, sceneProduct):
        performMetabolism = PerformMetabolismTk()
        self.inner = performMetabolism.inner(self.inner, sceneProduct)

    def resetThoughts(self):
        self.inner.psychologicalTraits.thoughtsArray.clear()
        self.inner.psychologicalTraits.todayHistory = ""

    def updateDate(self, sceneProduct):
        self.inner.traits.currentDateWritten = sceneProduct.dateWrited

    def actionsForDays(self, sceneProduct):
        self.performMetabolism(sceneProduct)
        self.performReasoning()
        if(not self.inner.traits.isItAnAvatar):
            self.takeDesition()
        self.updateDate(sceneProduct)
        self.createHistory(sceneProduct)

    def endDay(self):
        self.resetThoughts()

    def countTheTime(self):
        countTheTime = CountTheTimeTk()
        self.inner = countTheTime.inner(self.inner)

    def advanceOneDay(self, sceneProduct, marketGlobalProduct):
        age = self.inner.getAge()
        age.advanceOneDay()
        self.inner.setAge(age)
        self.actionsForDays(sceneProduct)
        return self.buyProducts(marketGlobalProduct)

    def writeThoughts(self):
        text = ""
        for e in self.inner.traits.thoughtsArray:
            text += e.remimber
        return text

    def writeUpdate(self):
        writePersonUpdate = WritePersonUpdateTk()
        self.inner = writePersonUpdate.inner(self.inner)
        return text

    def writePresentation(self):
        writePersonPresentation = WritePersonPresentationTk()
        return writePersonPresentation.inner(self.inner)

    def writeFullName(self):
        writeFullName = WriteFullName()
        return writeFullName.inner(self.inner)

    def addTodayHistory(self, text):
        self.inner.psychologicalTraits.todayHistory += text

    def createHistory(self, sceneProduct):
        createHistory = CreateHistoryTk()
        self.inner = createHistory.inner(self.inner, sceneProduct)

    def randomize(self, culture, regionPresentation):
        randomizePerson = RandomizePersonTk()
        self.inner = randomizePerson.inner(self.inner, culture, regionPresentation)

#ACCESSORS---------------------------------------------------------------------------------------------

    def getName():
        return self.inner.information.getName()

    def getSecondName():
        return self.inner.information.getSecondName()

    def getLastName():
        return self.inner.information.getLastName()

    def getSecondLastName():
        return self.inner.information.getSecondLastName()

    def getNickname():
        return self.inner.information.getNickname()

    def getCodeInt():
        return self.inner.information.getCodeInt()

    def setCodeInt(valueInt):
        self.inner.information.setCodeInt(valueInt)

    def getCurrentResidence():
        return self.inner.information.getCurrentResidence()

    def setCurrentResidence(valueInt):
        self.inner.information.setCurrentResidence(valueInt)

    def getCurrentDateWritten():
        self.inner.information.getCurrentDateWritten()

    def setCulture(valueInt):
        self.inner.information.setCulture(valueInt)

    def getCulture():
        return self.inner.information.getCulture()

    def getAge():
        return self.inner.information.getAge()

    def setWhatTerrainIsItOn(valueInt):
        self.inner.information.setWhatTerrainIsItOn(valueInt)

    def getWhatTerrainIsItOn():
        return self.inner.information.getWhatTerrainIsItOn()

    def getTitlesArray():
        return self.inner.information.getTitlesArray()

    def setIsItAnAvatar():
        self.inner.information.setIsItAnAvatar()

    def getCaste():
        return self.inner.information.getCaste()

    def getBornDate():
        return self.inner.information.getBornDate()

    def getDeathDate():
        return self.inner.information.getDeathDate()

#--------------------------------------------------------------------------------------------
