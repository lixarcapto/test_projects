

import random
from data_model.app.world_lib.app.product.WorldProduct import WorldProduct
from data_model.app.market_lib.MarketGlobal import MarketGlobal
from data_model.app.translator_lib.Translator import Translator
from data_model.app.world_lib.app.task.MakeDesitionTk import MakeDesitionTk
from data_model.app.world_lib.app.task.RandomizeProtagonistCodeTk import RandomizeProtagonistCodeTk
from basic.Basic import Basic

class World:

    MONTH_ARRAY = [
    "warmary",
    "dryary",
    "wetary",
    "coldary"
    ]

    DAY_NAME = [
    "dawnty",
    "sunsety",
    "duskty",
    "darkty"
    ]

    DAY_LIMIT = 3
    YEAR_MAX = 1492
    YEAR_MIN = 870
    MONTH_LIMIT = 3

    def __init__(self):
        self.inner = WorldProduct()
        return

#*** MUTATTORS ***************************************************************************

    def writePresentation(self):
        text = ""
        region = self.inner.regionMatrix.getRegionByCode(self.protagonistCodeRegion)
        person = self.inner.regionMatrix.getPersonInWorld(self.protagonistCode)
        text += person.writePresentation()
        text += " el vivia en "
        text += region.writeInformation()
        return text

    def writeDate(self):
        text = ""
        return text

    def takeDesitionWithProtagonist(self, desitionCode):
        personProtagonist = self.inner.regionMatrix.getPersonInWorld(self.inner.protagonistCode)
        personProtagonist.setDesition(desitionCode)
        self.inner.regionMatrix.updatePersonInWorld(personProtagonist)

    def writeWhatTheProtagonistWillDo(self):
        personProtagonist = self.inner.regionMatrix.getPersonInWorld(self.inner.protagonistCode)
        return personProtagonist.writeWhatWillDo()

    def writeTheFullNameOfProtagonist(self):
        personProtagonist = self.inner.regionMatrix.getPersonInWorld(self.inner.protagonistCode)
        return personProtagonist.writeFullName()

    def takeDesitionGoal(self, desitionCode):
        personProtagonist = self.inner.regionMatrix.getPersonInWorld(self.inner.protagonistCode)
        personProtagonist.person.traits.desitionGoal = desitionCode
        self.inner.regionMatrix.updatePersonInWorld(personProtagonist)

    def makeDesitions(self):
        makeDesitions = MakeDesitionTk()
        self.inner = makeDesitions.inner(self.inner)

    def meetSomeone(self):
        self.inner.regionMatrix.getRegionByCode(self.inner.protagonistCodeRegion)

    def randomizeProtagonistCode(self):
        randomizeProtagonistCode = RandomizeProtagonistCodeTk()
        self.inner = randomizeProtagonistCode.inner(self.inner)

    def initNewLife(self):
        self.randomizeProtagonistCode()

    def writeInformation(self):
        date = self.inner.date
        text = ""
        text += "date: " + str(date.getDay())
        text += " of " + str(date.getMonth())
        text += " from "  + str(date.getYear()) + " \n"
        text += self.inner.regionMatrix.writeInformation()
        return text

    def createNewScenario(self):
        year = random.randint(World.YEAR_MIN, World.YEAR_MAX)
        day = random.randint(0, World.DAY_LIMIT)
        month = random.randint(0, World.MONTH_LIMIT)
        self.inner.date.setYear(year)
        self.inner.date.setDay(day)
        self.inner.date.setMonth(month)
        self.inner.regionMatrix.createMatrix()
        self.inner.regionMatrix.calculeData()
        self.inner.regionMatrix.createFirstSettlement(15)
        return

    def actionsInADay(self):
        self.inner.dateWrited = self.writeDate()
        self.makeDesitions()
        self.inner.regionMatrix.advanceOneDayToEachRegion(self.inner)

    def protagonistIsDead(self):
        person = self.inner.regionMatrix.getPersonInWorld(self.inner.protagonistCode)
        if(person.person.getIsDeath()):
            return True
        return False

    def writeHistoryOfProtagonist(self):
        text = ""
        person = self.inner.regionMatrix.getPersonInWorld(self.inner.protagonistCode)
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
        person = self.inner.regionMatrix.getPersonInWorld(self.inner.protagonistCode)
        relationList = person.getRelationList()
        if(not relationList.hasSomeRelation()):
            array.append("no tiene amigos ni parientes")
        else:
            n = 0
            personRelated = None
            codesArray = relationList.getRelationPersonCodesArray()
            for e in codesArray:
                personRelated = self.inner.regionMatrix.getPersonInWorld(e)
                array.append(personRelated.writeFullName())
        return array

    def decideWhoYouWantToVisit(self, codeInt):
        person = self.inner.regionMatrix.getPersonInWorld(self.inner.protagonistCode)
        person.person.inner.mind.inner.desitionDataCode = codeInt
        self.inner.regionMatrix.updatePersonInWorld(person)

    def advanceOneDay(self):
        self.inner.date.advanceOneDay()
        self.actionsInADay()

#*** ACCESSORS **********************************************************************



#*********************************************************************************
