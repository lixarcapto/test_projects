

from data_model.app.person_list_lib.core.person.app.task.randomize_values_task.RandomizeCultureTraitsTk import RandomizeCultureTraitsTk
from data_model.app.person_list_lib.core.person.app.task.show_task.WritePersonPresentationTk import WritePersonPresentationTk
from data_model.app.person_list_lib.core.data_generator.DataGenerator import DataGenerator
import random

class RandomizePersonTk:

    def inner(self, personProduct, culture, regionPresentation):
        randomizeName = RandomizeNameTk()
        randomizeLastname = RandomizeLastnameTk()
        dataGenerator = DataGenerator()
        writePersonPresentation = WritePersonPresentationTk()
        randomizeCulturalTraits = RandomizeCultureTraitsTk()
        personInformation = personProduct.getPersonInformation()
        personProduct.physicalTraits.weight = random.randint(0, personProduct.PERSON_KEYS.WEIGHT.LIMIT)
        personProduct.physicalTraits.age = random.randint(0, personProduct.PERSON_KEYS.AGE.LIMIT)
        personProduct.physicalTraits.height = random.randint(0, personProduct.PERSON_KEYS.HEIGHT.LIMIT)
        personProduct.physicalTraits.gender = random.randint(0, 1)
        personInformation.inner.setCulture(culture)
        personProduct.physicalTraits.race = dataGenerator.generateRaceByCulture(culture)
        personProduct = randomizeCulturalTraits.inner(personProduct)
        text = ""
        text += writePersonPresentation.inner(personProduct)
        text += " el vivia en " + regionPresentation
        personProduct.addHistory(text)
        return personProduct
