


import random
from data_access.DataAccess import DataAccess
from data_access.core.translator.Translator import Translator
from data_model.core.region.app.product.RegionPDT import RegionPDT

class Region:

    def __init__(self):
        self.inner = RegionPDT()
        return

    def writeRegionDescription(self):
        text = "Region description: \n"
        if(self.inner.getIsInhabited()):
            text = self.inner.getPersonList().writePersonListDescription()
        return text

    def createInitialPerson(self, quantityStartedPerson):
        personList = self.inner.getPersonList()
        personList.createInitialPerson(self.inner.getCulture(),
        quantityStartedPerson)
        self.inner.setPersonList(personList)

    def generateNameOfRegion(self, cultureCode):
        regionNamesMatrix = DataAccess().getNamesData().getRegionNamesMatrix()
        nameArray = regionNamesMatrix[cultureCode]
        randomInt = random.randint(0, len(nameArray) -1)
        return nameArray[randomInt]

    def randomizeNames(self):
        name = self.generateNameOfRegion(self.inner.getCulture())
        self.inner.setName(name)

    def randomize(self):
        regionKeys = DataAccess().getRegionKeys()
        relief = random.randint(0, len(regionKeys.getReliefMap()) -1)
        self.inner.setRelief(relief)
        temperatureRegime = random.randint(0, len(regionKeys.getTemperatureRegimeMap()) -1)
        self.inner.setTemperatureRegime(temperatureRegime)
        windRegime = random.randint(0, len(regionKeys.getWindSpeedMap()) -1)
        self.inner.setWindRegime(windRegime)
        typeSoil = random.randint(0, len(regionKeys.getTypeSoilMap()) -1)
        self.inner.setTypeSoil(typeSoil)

    def writeInformation(self):
        translator = Translator()
        text = ""
        text += "El " + translator.obtainBiome(self.inner.getBiome()) + " "
        text += self.inner.getName() + " "
        text += "un/a " + translator.obtainTemperatureRegime(self.inner.getTemperatureRegime()) + " "
        text += translator.obtainRelief(self.inner.getRelief()) + " cubierta de "
        text += translator.obtainTypeSoil(self.inner.getTypeSoil()) + " y vientos "
        text += translator.obtainWindRegime(self.inner.getWindRegime()) + ", "
        text += "se encuentra en latitud " + str(self.inner.getLatitude()) + "° "
        text += "longitud " + str(self.inner.getLongitude()) + "° "
        text += "habitada por " + translator.obtainCulture(self.inner.getCulture())
        return text

    def advanceOneDay(self, worldProduct):
        if(self.isItInhabited):
            self.personList.advanceOneDay(worldProduct, self.writeInformation())
            self.personList.cleanDeadPerson()

    def writeListOfPersonInformation(self):
        text = ""
        if(self.isItInhabited):
            text += "habitada por \n"
            text += self.personList.writeInformation()
        else:
            text += "no esta habitada \n"
        return text
