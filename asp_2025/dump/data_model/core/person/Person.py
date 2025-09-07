


import random
from data_model.core.person.app.product.PersonPDT import PersonPDT

class Person:

    def __init__(self):
        self.inner = PersonPDT()
        return

    def receiveAttack(self, location, typeDamage, powerDamage, typeEffect,
    powerEffect):
        None

    def randomize(self, culture):
        mind = self.inner.getMind()
        body = self.inner.getBody()
        mind.inner.setCulture(culture)
        mind.randomizeMentalTraits(culture, body.inner.getGender())
        body.randomizeTraits(culture)
        self.inner.setMind(mind)
        self.inner.setBody(body)

    def writeHistory(self):
        text = ""
        for e in self.inner._mind.inner.history:
            text += e
        return text

    def writePersonUpdate(self, type):
        text = ""
        mind = self.inner.getMind()
        text += mind.inner.getName() + " " + mind.inner.getSecondName() + " "
        text += mind.inner.getLastName() + " " + mind.inner.getSecondLastName() + " "
        text += "tambien llamado " +  mind.inner.getNickname() + " "
        text += "su codigo es " + str(mind.inner.getCodeInt()) + " "
        text += self.inner.getBody().writePhyisalAppearance() + " "
        text += mind.writeSensations()
        text += self.writeHistory()
        return text

    def produceWork(self):
        profession = self.inner.getMind().inner._profession
        skillMatrix = self.inner.getMind().inner._skillMatrix
        if(skillMatrix == None):
            print("is none skillMatrix")
        workValue = skillMatrix[profession][1]
        array = [0] * 2
        array[0] = profession
        array[1] = workValue
        return array

    def writePhysicalDescription(self):
        text = ""
        text = self.inner.getBody().writePhyisalAppearance()
        return text

    def writeFullName(self):
        return self.inner.getMind().writeFullName()

    def writeWhatWillDo(self):
        translator = Translator()
        text = self.inner.getMind().writeFullName() + " desidio "
        text += translator.obtainDesition(self.inner.mind.inner.desition)
        return text

    def haveSex(self, personAProduct, personBProduct):
        bodyA = personAProduct.getBody()
        bodyArray = bodyA.haveSex(bodyA, personBProduct.getBody())
        personAProduct.setBody(bodyArray[0])
        personBProduct.setBody(bodyArray[1])
        personProductArray = []
        personProductArray.append(personAProduct)
        personProductArray.append(personBProduct)
        return personProductArray

    def takeTheBabyOut(self):
        return self.inner.getBody().takeTheBabyOut()

    def updateSensations(self):
        for e in self.inner._body.inner.sensationsArray:
            self.inner._mind.addSensation(e[0], e[1])

    def advanceOneDay(self, date, visionData, auditionData, olfactoryData):
        self.inner._mind.clearMemory()
        self.inner._body.advanceOneDay()
        self.updateSensations()
        self.inner._mind.inner.setPhysicalSelfDescription(self.writePhysicalDescription())
        self.inner._mind.inner.setVisionMemories(visionData)
        dateWritten = date.writeDate()
        self.inner._mind.inner.setCurrentDateWritten(dateWritten)
        self.inner._mind.createHistory()

    def advanceOneDayOld(self, date, visionRegion):
        self.inner.body.advanceOneDay()
        if(self.inner.body.inner.getAge().checkFulfiledYears()):
            self.inner.body.doYearActions()
            self.inner.mind.inner.setNeedToIntroduceHimself(True)
        self.inner.mind.takeDesition()
        self.inner.mind.inner.setPhysicalSelfDescription(self.writePhysicalDescription())
        self.inner.mind.inner.setVisionMemories(visionRegion)
        dateWritten = date.writeDate()
        self.inner.mind.inner.setCurrentDateWritten(dateWritten)
        self.inner.mind.createHistory()

    def addDailyEvent(self, text):
        self.inner.mind.inner.todayHistory += text

    def addDailyEvent(self, text):
        self.inner._mind.addDailyEvent(0, 0, text)

    def castAttack(self):
        if(self.inner._body.inner._energyReserve > 1):
            self.inner._body.inner._energyReserve -= 1
        self.addDailyEvent("lanzo un ataque ")

    def receiveAttack(self, type, power):
        quantityOrgan = len(self.inner._body.inner.systemMap)
        randomValue = random.randint(0, quantityOrgan -1)
        i = 0
        keyRandom = ""
        for e in self.inner._body.inner.systemMap.keys():
            print("key: " + e + " /keyRandom: " + keyRandom)
            if(i == randomValue):
                keyRandom = e
                break
            i += 1
        self.inner._mind.addDailyEvent(0, 0, "recibio un golpe en " + keyRandom)
        self.inner._body.inner.systemMap[keyRandom].causeDamage(power)
