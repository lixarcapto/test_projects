



from basic.Basic import Basic

class RandomizeProtagonistCodeTk:

    def inner(self, scenePDT):
        randomInt = 0
        codeArray = scenePDT._world.getAllCodesOfLivePersonInWorld()
        for e in codeArray:
            print("person lives codes: " + str(e))
        randomValue = Basic().randomizeIntFromArray(codeArray)
        print("randomCode: " + str(randomValue))
        scenePDT._protagonistCode = randomValue
        person = scenePDT._world.getPersonInWorld(scenePDT._protagonistCode)
        if(person == None):
            print("<!> Error: persona "+ str(scenePDT._protagonistCode) +" no encontrada en RandomizeProtagonistCodeTk()")
        person.inner._mind.inner.setIsItAnAvatar(True)
        scenePDT._world.updatePersonInWorld(person)
        return scenePDT
