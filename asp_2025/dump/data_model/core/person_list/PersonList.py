


from data_model.core.person.Person import Person
from basic.Basic import Basic

class PersonList:

    LAST_CODE_INT = 0

    def __init__(self):
        self.personArray = []
        self.deadArray = []
        return

#*** ACCESSORS **********************************************************************

    def isVoid(self):
        if(len(self.personArray) > 0):
            return False
        return True

    def addPerson(self, person):
        self.personArray.append(person)

    def hasPerson(self, person):
        codeInt = person.inner.getCodeInt()
        if(self.isVoid()):
            return False
        for e in self.personArray:
            if(e.inner.getCodeInt() == codeInt):
                return True
        return False

    def updatePerson(self, person):
        code = person.inner.getCodeInt()
        for i in range(len(self.personArray)):
            if(self.personArray[i].inner.getCodeInt() == code):
                self.personArray[i] = person
                break

    def setPerson(self, person):
        if(self.isVoid()):
            self.addPerson(person)
        elif(self.hasPerson(person)):
            self.updatePerson(person)

    def getPerson(self, codeInt):
        if(self.isVoid()):
            return None
        for e in self.personArray:
            if(e.inner.getCodeInt() == codeInt):
                return e
        return None

#*** MODIFIER ************************************************************************

    def writePersonListDescription(self):
        text = ""
        for e in self.personArray:
            text += e.writePersonUpdate(0)
        return text

    def generateLastCodeInt(self):
        code = PersonList.LAST_CODE_INT
        PersonList.LAST_CODE_INT += 1
        return code

    def createPerson(self):
        person = Person()
        person.inner.setCodeInt(self.generateLastCodeInt())
        return person

    def createInitialPerson(self, culture, quantity):
        for i in range(quantity):
            person = self.createPerson()
            person.randomize(culture)
            self.addPerson(person)

    def givingBirth(self, babyBody):
        newPerson = Person()
        newPerson.inner.setBody(babyBody)
        return person

    def produceWorkFromAllPerson(self):
        workArray = []
        for i in range(len(self.personArray)):
            print("produce work: " + str(i))
            workArray.append(self.personArray[i].produceWork())
        return workArray

    def advanceOneDay(self, worldProduct, visionRegion):
        babyBody = None
        person = None
        for i in range(len(self.personArray)):
            person = self.personArray[i]
            if(person != None):
                person.advanceOneDay(worldProduct, visionRegion)
                if(person.inner.getIsPregnant()
                and person.inner.getPregnantTime() >= 12):
                    babyBody = person.takeTheBabyOut()
                    person = self.givingBirth(babyBody)
                    self.addPerson(person)
            self.personArray[i] = person

    def getPersonLiveCodesArray(self):
        personLiveArray = []
        for i in range(len(self.personArray)):
            if(self.personArray[i] != None):
                codeInt = self.personArray[i].inner.getCodeInt()
                personLiveArray.append(codeInt)
        return personLiveArray

    def writeAllPersonDescription(self):
        text = " habia "
        endText = " "
        itIsTheFirstOne = True
        for e in self.personArray:
            if(itIsTheFirstOne):
                itIsTheFirstOne = False
                endText = ". \n"
            if(e != None):
                text += e.writePersonUpdate(0) + endText
        return text

    def obtainRandomPersonCode(self):
        codePeople = 0
        codeArray = self.getPersonLiveCodesArray()
        codePeople = Basic().randomizeIntFromArray(codeArray)
        person = self.getPerson(codePeople)
        print("code random;" + str(codePeople))
        return person.inner.getCodeInt()

    def cleanDeadPerson(self):
        None

#*************************************************************************************
