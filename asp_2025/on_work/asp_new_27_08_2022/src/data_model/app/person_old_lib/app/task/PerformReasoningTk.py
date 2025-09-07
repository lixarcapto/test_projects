


class PerformReasoningTk:

    def inner(self, personProduct):
        if(personProduct.needs.hasHunger):
            personProduct.addThought(personProduct.PERSON_KEYS.TOPIC.HUNGER," estar hambriento,")
        if(personProduct.needs.hasThirst):
            personProduct.addThought(personProduct.PERSON_KEYS.TOPIC.THIRST, " tener sed,")
        #tejidos
        if(personProduct.body.externalTissueHealth <= 2):
            personProduct.addThought(personProduct.PERSON_KEYS.TOPIC.PAIN, " tener una pequeña herida abierta,")
        elif(personProduct.body.externalTissueHealth <= 1):
            personProduct.addThought(personProduct.PERSON_KEYS.TOPIC.PAIN, " tener una gran herida abierta,")
        elif(personProduct.body.externalTissueHealth <= 0):
            personProduct.addThought(personProduct.PERSON_KEYS.TOPIC.PAIN, " haber perdido parte la carne hasta sus huesos,")
        if(personProduct.body.internalTissueHealth <= 2):
            personProduct.addThought(personProduct.PERSON_KEYS.TOPIC.PAIN, " tener frio en el interior,")
        elif(personProduct.body.internalTissueHealth <= 1):
            personProduct.addThought(personProduct.PERSON_KEYS.TOPIC.PAIN, " sentirse confundido con frio en el interior,")
        elif(personProduct.body.internalTissueHealth <= 0):
            personProduct.addThought(personProduct.PERSON_KEYS.TOPIC.PAIN, " sentirse debil y confundido con frio en el interior,")
        #estados
        if(personProduct.body.isInACome):
            personProduct.addThought(personProduct.PERSON_KEYS.TOPIC.PAIN, " entrar en coma,")
        if(personProduct.body.isUnconscious):
            personProduct.addThought(personProduct.PERSON_KEYS.TOPIC.PAIN, " no estar conciente,")
        if(personProduct.body.circulatorySystemState <= 2):
            personProduct.addThought(personProduct.PERSON_KEYS.TOPIC.PAIN, " sentir punzadas en el pecho,")
        if(personProduct.body.nervousSystemState <= 2):
            personProduct.addThought(personProduct.PERSON_KEYS.TOPIC.PAIN, " no sentir su cuerpo,")
        if(personProduct.body.brainState <= 2):
            personProduct.addThought(personProduct.PERSON_KEYS.TOPIC.PAIN, " tener lagunas de memoria,")
        if(personProduct.body.amountOfBloodToDie <= 5):
            personProduct.addThought(personProduct.PERSON_KEYS.TOPIC.PAIN, " tener frio en las extremidades,")
        if(personProduct.body.respiratorySystemState <= 2):
            personProduct.addThought(personProduct.PERSON_KEYS.TOPIC.PAIN, " no poder respirar,")
        personProduct.psychologicalTraits.moodValue = personProduct.needs.calculeNeedsValue()
        return personProduct
