

from data_model.core.body.app.task.RandomizeCultureTraitsTk import RandomizeCultureTraitsTk
from basic.Basic import Basic
from data_access.DataAccess import DataAccess
import random

class RandomizeBodyTraitsTK:

    def generateRaceByCulture(self, culture):
        array = None
        racesByCulture = DataAccess().createValuesSupplier().getRacesByCulturesData()
        array = racesByCulture[culture]
        return Basic().randomizeIntFromArray(array)

    def inner(self, bodyProduct, culture):
        randomizeCultureTraits = RandomizeCultureTraitsTk()
        #randomizeGenes
        genes = bodyProduct.getGenesThis()
        genes.randomizeGenes()
        bodyProduct.setGenesThis(genes)
        genes = bodyProduct.getGenesDad()
        genes.randomizeGenes()
        bodyProduct.setGenesDad(genes)
        genes = bodyProduct.getGenesMom()
        genes.randomizeGenes()
        bodyProduct.setGenesMom(genes)
        #randomizeTraits
        bodyProduct.setGender(random.randint(0, 1))
        #analizar y actualizar
        ageMap = DataAccess().createValuesSupplier().getAgeMap()

        race = self.generateRaceByCulture(culture)
        bodyProduct.setRace(race)
        ageRandom = random.randint(ageMap["teen"], len(ageMap) -1)
        bodyProduct.setAgeCode(ageRandom)
        bodyProduct = randomizeCultureTraits.inner(bodyProduct)
        #si es mayor a joven tendra su tamaño maximo
        if(ageMap["young"] < ageRandom):
            bodyProduct.setHeight(bodyProduct.getGenesThis().getHeightLimit())
        else:
            bodyProduct.setHeight(2)
        return bodyProduct
