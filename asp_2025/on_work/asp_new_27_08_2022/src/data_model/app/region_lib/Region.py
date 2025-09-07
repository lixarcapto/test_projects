

import random
from data_model.app.market_lib.core.market_local.MarketLocal import MarketLocal
from data_model.app.person_list_lib.PersonList import PersonList
from data_model.app.translator_lib.Translator import Translator
from data_model.app.region_lib.core.terrain_matrix.TerrainMatrix import TerrainMatrix
from data_model.app.general_lib.core.coordinate.Coordinate import Coordinate

from data_access.DataAccess import DataAccess

from basic.Basic import Basic

class Region:

    personLimitInt = 50

    def __init__(self):
        # values
        self.terrainMatrix = TerrainMatrix()
        self.personList = None
        self.coordinate = Coordinate()
        # data
        self.relief = 0
        self.biome = 0
        self.windRegime = 0
        self.windSpeed = 0
        self.typeSoil = 0
        self.actualTemperature = 0
        self.temperatureRegime = 0
        self.actualClime = 0
        self.locationX = 0
        self.locationY = 0
        self.latitude = 0
        self.longitude = 0
        self.name = "no_name"
        self.code = 0
        self.culture = 0
        self.ownerCode = 0
        self.isItInhabited = False
        return

    def generateNameOfRegion(self, cultureCode):
        regionNamesMatrix = DataAccess().getNamesData().getRegionNamesMatrix()
        nameArray = regionNamesMatrix[cultureCode]
        randomInt = random.randint(0, len(nameArray) -1)
        return nameArray[randomInt]

    def randomizeNames(self):
        self.name = self.generateNameOfRegion(self.culture)

    def randomize(self):
        regionData = DataAccess().getRegionData()
        self.relief = random.randint(0, regionData.RELIEF_MAX)
        self.temperatureRegime = random.randint(0, regionData.TEMPERATURE_REGIME_MAX)
        self.windRegime = random.randint(0, regionData.WIND_REGIME_MAX)
        self.typeSoil = random.randint(0, regionData.TYPE_SOIL_MAX)

    def createAllTitles(self):
        totalTerrains = len(terrainMatrix.terrainMatrix) * len(terrainMatrix.terrainMatrix)
        for i in range(totalTerrains):
            None

    def endDayForRegion(self):
        self.personList.endDay()

    def goOutToMeetPerson(self, origenCode):
        personOrigen = self.personList.getPerson(origenCode)
        randomCode = self.obtainRandomPersonCode(personDestiny)
        personDestiny = self.personList.getPerson(randomCode)
        personOrigen.relationList.addRelation(0, personDestiny.codeInt, "known")
        personDestiny.relationList.addRelation(0, personOrigen.codeInt, "known")
        personDestiny.addHistory(
        " y entonces conocio a " + personOrigen.writePresentation())
        personOrigen.addHistory(
        " y entonces conocio a " + personDestiny.writePresentation())
        self.regionMatrix.updatePersonInWorld(personOrigen)
        self.regionMatrix.updatePersonInWorld(personDestiny)

    def obtainRandomPersonCode(self):
        codePeople = 0
        codeArray = self.personList.getPersonLiveCodesArray()
        codePeople = Basic().randomizeIntFromArray(codeArray)
        person = self.personList.getPerson(codePeople)
        print("code random;" + str(codePeople))
        return person.getCodeInt()

    def writeInformation(self):
        translator = Translator()
        text = ""
        text += "El " + translator.obtainBiome(self.biome) + " " + self.name + " "
        text += "un/a " + translator.obtainTemperatureRegime(self.temperatureRegime) + " "
        text += translator.obtainRelief(self.relief) + " cubierta de "
        text += translator.obtainTypeSoil(self.typeSoil) + " y vientos "
        text += translator.obtainWindRegime(self.windRegime) + ", "
        text += "se encuentra en latitud " + str(self.latitude) + "° "
        text += "longitud " + str(self.longitude) + "° "
        text += "habitada por " + translator.obtainCulture(self.culture)
        return text

    def advanceOneDay(self, worldProduct):
        if(self.isItInhabited):
            self.personList.advanceOneDay(worldProduct, self.writeInformation())
            self.personList.cleanDeadPerson()

    def createFirstPerson(self, culture):
        self.culture = culture
        self.isItInhabited = True
        self.personList = PersonList()
        self.randomizeNames()
        self.personList.createInitialPerson(culture, self.code, self.writeInformation())

    def writeListOfPersonInformation(self):
        text = ""
        if(self.isItInhabited):
            text += "habitada por \n"
            text += self.personList.writeInformation()
        else:
            text += "no esta habitada \n"
        return text

#*** ACCESSORS *******************************************************************

    def getCoordinate(self):
        return self.coordinate

    def setCoordinate(self, coordinate):
        self.coordinate = coordinate

#*********************************************************************************
