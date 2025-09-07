


from data_model.app.translator_lib.Translator import Translator
from data_access.DataAccess import DataAccess
from basic.Basic import Basic
import random

class MeetAFriendTk:

    def inner(self, sceneProduct, personCode):
        translator = Translator()
        personKeys = DataAccess().getPersonData()
        relation = None
        personProtagonist = sceneProduct.regionMatrix.getPersonInWorld(personCode)
        region = sceneProduct.regionMatrix.getRegionByCode(personProtagonist.getCurrentResidence())
        relationList = personProtagonist.getRelationList()
        randomValue = 0
        #si tiene relaciones
        if(relationList.hasSomeRelation()):
            relationCodesArray = relationList.getRelationPersonCodesArray()
            secondaryPersonCode = Basic().randomizeIntFromArray(relationCodesArray)
            personSecondary = region.personList.getPerson(secondaryPersonCode)
            historyProtagonist = translator.obtainDesitionConsequence(personProtagonist.getDesition())
            historyProtagonist += " " + personSecondary.writePresentation()
            historySecondary = translator.obtainDesitionConsequence(personSecondary.getDesition())
            historySecondary +=  " " +  personProtagonist.writePresentation()
            #
            personProtagonist.inner.mind.addDailyEvent("visito_a_amigo", personSecondary.getCodeInt() ,historyProtagonist)
            personSecondary.inner.mind.addDailyEvent("visito_a_amigo", personSecondary.getCodeInt() ,historySecondary)
            sceneProduct.regionMatrix.updatePersonInWorld(personProtagonist)
            sceneProduct.regionMatrix.updatePersonInWorld(personSecondary)
        #si no tiene relaciones
        else:
            historyProtagonist = translator.obtainDesitionConsequence(personProtagonist.getDesition())
            historyProtagonist += " no tenia amigos para encontrarse "
            personProtagonist.inner.mind.addDailyEvent("no_hizo_nada", 0, historyProtagonist)
            sceneProduct.regionMatrix.updatePersonInWorld(personProtagonist)
        return sceneProduct
