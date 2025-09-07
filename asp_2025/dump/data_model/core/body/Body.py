

import random
from data_model.core.body.app.product.BodyProduct import BodyProduct
from data_model.core.body.app.task.RandomizeBodyTraitsTK import RandomizeBodyTraitsTK
from data_model.core.body.app.task.WritePhysicalDescriptionTk import WritePhysicalDescriptionTk
from data_model.core.body.app.task.DoBasicMetabolismTk import DoBasicMetabolismTk
from data_model.core.body.app.task.GrowHairTK import GrowHairTK
from data_model.core.body.core.genes.Genes import Genes
from basic.Basic import Basic
from data_access.DataAccess import DataAccess

class Body:

    """
        Cada sensacion contiene el valor tipo de sensacion y tipo de causa,
        las sensaciones provienen del tacto y el sistema nervioso periferico.
    """

    def __init__(self):
        self.inner = BodyProduct()
        return

#*** MUTTATORS *******************************************************************

    def writePhyisalAppearance(self):
        text = ""
        translator = DataAccess().createTranslator()
        writePhysicalDescription = WritePhysicalDescriptionTk()
        text = writePhysicalDescription.inner(self.inner)
        return text

    def addSensation(self, typeString, organString):
        organMap = DataAccess().getPersonKeys().getOrganTypeMap()
        topicMap = DataAccess().getPersonKeys().getTopicKeysMap()
        array = [None] * 2
        array[0] = topicMap[typeString]
        array[1] = organMap[organString]
        self.inner.sensationsArray.append(array)

    def addSensationCode(self, typeString, organCode):
        topicMap = DataAccess().getPersonKeys().getTopicKeysMap()
        array = [None] * 2
        array[0] = topicMap[typeString]
        array[1] = organCode
        self.inner.sensationsArray.append(array)

    def breathe(self):
        return

    def writeOrganismAppearance(self):
        text = ""
        for e in self.inner.systemMap.keys():
            text += self.inner.systemMap[e].writeAppearance() + ".\n"
        return text

    def randomizeTraits(self, culture):
        randomizeBodyTraits = RandomizeBodyTraitsTK()
        self.inner = randomizeBodyTraits.inner(self.inner, culture)

    def reproduceNewBody(self, bodyMomInterface, bodyDadInterface):
        bodyMom = bodyMomInterface.inner
        bodyDad = bodyDadInterface.inner
        genesRealDad = bodyDad.getGenesThis()
        genesRealMom = bodyMom.getGenesThis()
        genesDad = genesRealDad.convertToIntArray()
        genesMom = genesRealMom.convertToIntArray()
        genesLenght = len(genesDad)
        genesFinalArray = [0] * genesLenght
        randomValue = 0
        arrayToSelect = []
        for i in range(genesLenght):
            arrayToSelect.append(genesMom[i])
            arrayToSelect.append(genesDad[i])
            randomValue = random.randint(0, 1)
            genesFinalArray[i] = arrayToSelect[randomValue]
            print("genesMom: " + str(genesMom[i]))
            print("genesDad: " + str(genesDad[i]))
            print("genes: " + str(genesFinalArray[i]))
            arrayToSelect.clear()
        body = Body()
        body.inner.setGenesDad(bodyDad.getGenesThis())
        body.inner.setGenesMom(bodyMom.getGenesThis())
        genesEmbryo = Genes()
        genesEmbryo.convertIntArrayToGenes(genesFinalArray)
        body.inner.setGenesThis(genesEmbryo)
        bodyMom._isPregnant = True
        bodyMom._bodyEmbryo = body
        bodyMomInterface.inner = bodyMom
        bodyDadInterface.inner = bodyDad
        bodyArray = []
        bodyArray.append(bodyMomInterface)
        bodyArray.append(bodyDadInterface)
        return bodyArray

    def haveSex(self, bodyA, bodyB):
        return self.reproduceNewBody(bodyA, bodyB)

    def growHeight(self):
        if(self.inner.getHeight() <= self.inner.getLimitHeight()):
            height = self.inner.getHeight() + 1
            self.inner.setHeight(height)

    def growHair(self):
        growHair = GrowHairTK()
        self.inner = growHair.inner(self.inner)

    def generateRaceByCulture(self, culture):
        array = None
        racesByCulture = DataAccess().getRacesByCultureData()
        array = racesByCulture.RACES_BY_CULTURE_ARRAY[culture]
        return Basic().randomizeIntFromArray(array)

    def eatProduct(self, product):
        eatProduct = EatProductTk()
        self.inner = eatProduct.inner(self.inner)

    def doBasicMetabolism(self):
        doBasicMetabolism = DoBasicMetabolismTk()
        self.inner = doBasicMetabolism.inner(self.inner)

    def performMetabolism(self):
        performMetabolism = PerformMetabolismTk()
        self.inner = performMetabolism.inner(self.inner)

    def takeTheBabyOut(self):
        self.inner.setIsPregnant(False)
        self.inner.setPregnantTime(0)
        babyBody = self.inner.getEmbryoBody()
        self.inner.setEmbryoBody(None)
        return babyBody

    def doYearActions(self):
        self.growHair()
        self.growHeight()

    def generateCorporalSenses(self):
        self.inner.sensationsArray.clear()
        if(self.inner._itIsHungry):
            self.addSensation("pain", "higher_digestive")
        if(self.inner._openWoundLevel):
            self.addSensation("pain", "skin")
        if(self.inner._itIsPoisoned):
            self.addSensation("pain", "middle_digestive")
        if(self.inner._sepsis):
            self.addSensation("pain", "brain")
            self.addSensation("pain", "circulatory")
            self.addSensation("cold", "skin")
        if(self.inner._itIsThirsty):
            self.addSensation("dryness", "skin")
            self.addSensation("dryness", "mouth")
        if(self.inner._isBleeding):
            self.addSensation("pain", "circulatory")
            self.addSensation("cold", "skin")
        if(self.inner._lackOfMineral):
            self.addSensation("pain", "circulatory")
        if(self.inner._lackOfVitamin):
            self.addSensation("irritation", "skin")
            self.addSensation("fatigue", "respiratory")
            self.addSensation("paralysis", "arms")
            self.addSensation("paralysis", "legs")
        for e in self.inner.systemMap.keys():
            if(self.inner.systemMap[e].getState() < 3):
                self.addSensationCode("pain", self.inner.systemMap[e].getType())

    def writeSensations(self):
        text = "sentia "
        translator = DataAccess().createTranslator()
        array = None
        for i in range(len(self.inner.sensationsArray)):
            array = self.inner.sensationsArray[i]
            text += translator.obtainSensationsType(array[0]) + " en "
            text += translator.obtainOrganType(array[1]) + ", "
        return text

    def writeSoundDescription(self):
        text = ""
        return text

    def advanceAge(self):
        ageQuantity = len(DataAccess().getPersonKeys().getAgeKeyMap())
        if(self.inner._age.age < ageQuantity -1):
            self.inner._age.advanceOneDay()

    def advanceOneDay(self):
        self.advanceAge()
        self.doBasicMetabolism()
        self.generateCorporalSenses()
