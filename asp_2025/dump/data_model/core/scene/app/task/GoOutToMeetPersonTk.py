

from data_model.app.translator_lib.Translator import Translator

class GoOutToMeetPersonTk:

    def inner(self, sceneProduct, personACode):
        translator = Translator()
        personProtagonist = sceneProduct.regionMatrix.getPersonInWorld(personACode)
        region = sceneProduct.regionMatrix.getRegionByCode(personProtagonist.getCurrentResidence())
        personCode = region.obtainRandomPersonCode()
        personSecondary = region.personList.getPerson(personCode)
        codeInt = personSecondary.getCodeInt()
        personProtagonist.inner.mind.inner.relationList.addRelation(0, codeInt, "known")
        codeInt = personProtagonist.getCodeInt()
        personSecondary.inner.mind.inner.relationList.addRelation(0, codeInt, "known")
        desition = personProtagonist.getDesition()
        historyProtagonist = translator.obtainDesitionConsequence(desition) + " " + personSecondary.writePresentation()
        desition = personSecondary.getDesition()
        historySecondary = translator.obtainDesitionConsequence(desition) + " " + personProtagonist.writePresentation()
        personProtagonist.inner.mind.addDailyEvent("conocio_a", personSecondary.getCodeInt(),
        historyProtagonist)
        personSecondary.inner.mind.addDailyEvent("conocio_a", personProtagonist.getCodeInt(),
        historySecondary)
        sceneProduct.regionMatrix.updatePersonInWorld(personProtagonist)
        sceneProduct.regionMatrix.updatePersonInWorld(personSecondary)
        return sceneProduct
