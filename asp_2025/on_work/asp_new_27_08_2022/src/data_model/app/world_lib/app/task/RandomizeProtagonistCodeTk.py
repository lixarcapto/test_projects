



from basic.Basic import Basic

class RandomizeProtagonistCodeTk:

    def inner(self, worldProduct):
        randomInt = 0
        codeArray = worldProduct.regionMatrix.getAllCodesOfLivePersonInWorld()
        for e in codeArray:
            print("person lives codes: " + str(e))
        randomValue = Basic().randomizeIntFromArray(codeArray)
        print("randomCode: " + str(randomValue))
        worldProduct.protagonistCode = randomValue
        person = worldProduct.regionMatrix.getPersonInWorld(worldProduct.protagonistCode)
        if(person == None):
            print("<!> Error: persona "+ str(worldProduct.protagonistCode) +" no encontrada en RandomizeProtagonistCodeTk()")
        person.setIsItAnAvatar(True)
        worldProduct.protagonistCodeRegion = person.getCurrentResidence()
        worldProduct.regionMatrix.updatePersonInWorld(person)
        return worldProduct
