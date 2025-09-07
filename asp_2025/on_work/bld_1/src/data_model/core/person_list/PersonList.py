


from data_model.core.person.Person import Person

class PersonList:

    LAST_CODE = 0

    def __init__(self):
        self.personArray = []
        return

    def getLastCode(self):
        code = PersonList.LAST_CODE
        PersonList.LAST_CODE += 1
        return code

    def createPerson(self):
        person = Person()
        person.codeInt = self.getLastCode()
        return person

    def setPerson(self, person):
        self.personArray.append(person)

    def size(self):
        return len(self.personArray)

    def hasPerson(self):
        if(range(len(self.personArray)) > 0):
            return True
        return False

    def getPerson(self, codeInt):
        for i in range(len(self.personArray)):
            if(self.personArray[i].codeInt == codeInt):
                return self.personArray[i]

    def extractPerson(self, codeInt):
        person = None
        for i in range(len(self.personArray)):
            if(self.personArray[i].codeInt == codeInt):
                person = self.personArray[i]
                del(self.personArray[i])
                return person

    def calculeHappyPeople(self):
        number = 0
        for i in range(len(self.personArray)):
            if(self.personArray[i].mood >= 0):
                number += 1
            else:
                number -= 1
        return number

    def createInitialPerson(self, quantity):
        person = None
        for i in range(quantity):
            person = self.createPerson()
            self.setPerson(person)

    def advanceTime(self, market):
        for i in range(len(self.personArray)):
            market = self.personArray[i].advanceTime(market)
        return market

    def writePersonData(self):
        text = "person: \n"
        for i in range(len(self.personArray)):
            text += " > " + self.personArray[i].writeData() + "\n"
        return text
