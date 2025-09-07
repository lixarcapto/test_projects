


from data_model.app.translator_lib.Translator import Translator

class HaveSexTk:

    def inner(self, worldProduct, personACode):
        translator = Translator()
        personA = worldProduct.regionMatrix.getPersonInWorld(personACode)
        region = worldProduct.regionMatrix.getRegionByCode(personA.getCurrentResidence())
        personCode = region.obtainRandomPersonCode()
        personB = region.personList.getPerson(personCode)
        codeInt = personB.getCodeInt()
        personA.inner.mind.inner.relationList.addRelation(1, codeInt, "couple")
        codeInt = personA.getCodeInt()
        personB.inner.mind.inner.relationList.addRelation(1, codeInt, "couple")
        desition = personA.getDesition()
        historyPersonA = translator.obtainDesitionConsequence(desition)
        historyPersonA += " " + personB.writeFullName()
        desition = personB.getDesition()
        historyPersonB = translator.obtainDesitionConsequence(desition)
        historyPersonB += " " + personA.writeFullName()
        personA.inner.mind.addDailyEvent("tuvo_sexo_con", personB.getCodeInt(),
        historyPersonA)
        personB.inner.mind.addDailyEvent("tuvo_sexo_con", personA.getCodeInt(),
        historyPersonB)
        worldProduct.regionMatrix.updatePersonInWorld(personA)
        worldProduct.regionMatrix.updatePersonInWorld(personB)
        return worldProduct
