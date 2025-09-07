

from data_model.app.person_lib.Person import Person
from data_model.app.person_list_lib.app.product.PersonListPDT import PersonListPDT
from data_model.app.person_list_lib.app.task.GetPersonTk import GetPersonTk
from data_model.app.person_list_lib.app.task.SetPersonTk import SetPersonTk

class PersonList:

    actualPersonCode = 0
    personLimit = 50

    def __init__(self):
        self.inner = PersonListPDT()

    def givingBirth(self, babyBody):
        newPerson = Person()
        newPerson.inner = babyBody
        return person

    def advanceOneDay(self, worldProduct, visionRegion):
        babyBody = None
        person = None
        for i in range(len(self.inner.personArray)):
            person = self.inner.personArray[i]
            if(person != None):
                person.advanceOneDay(worldProduct, visionRegion)
                if(person.getIsPregnant()
                and person.getPregnantTime() >= 12):
                    babyBody = person.takeTheBabyOut()
                    person = self.givingBirth(babyBody)
                    self.addPerson(person)
            self.personArray[i] = person

    def createPerson(self):
        person = Person()
        person.setCodeInt(PersonList.actualPersonCode)
        PersonList.actualPersonCode += 1
        return person

    def createInitialPerson(self, culture, codeRegion, regionPresentation):
        for i in range(len(self.inner.personArray)):
            person = Person()
            person.setCodeInt(PersonList.actualPersonCode)
            person.randomize(culture, regionPresentation)
            person.setCurrentResidence(codeRegion)
            PersonList.actualPersonCode += 1
            self.addPerson(person)

    def endDay(self):
        for i in range(len(self.personArray)):
            if(self.personArray[i] != None):
                self.personArray[i].endDay()

    def getPersonLiveCodesArray(self):
        personLiveArray = []
        for i in range(len(self.inner.personArray)):
            if(self.inner.personArray[i] != None):
                codeInt = self.inner.personArray[i].getCodeInt()
                personLiveArray.append(codeInt)
        return personLiveArray

    def writeAllPersonDescription(self):
        text = " habia "
        endText = " "
        itIsTheFirstOne = True
        for e in self.inner.personArray:
            if(itIsTheFirstOne):
                itIsTheFirstOne = False
                endText = ", "
            if(e != None):
                text += e.writePhysicalDescription() + endText
        return text

    def writeInformation(self):
        text = ""
        for e in self.inner.personArray:
            if(e != None):
                text += e.writeInformation()
        return text

    def writePresentation(self):
        text = ""
        for e in self.inner.personArray:
            if(e != None):
                text += e.writePresentation()
        return text

    def writeFullName(self):
        text = ""
        for e in self.inner.personArray:
            if(e != None):
                text += e.writeFullName()
        return text

    def updatePerson(self, person):
        for i in range(len(self.inner.personArray)):
            if(person == None):
                continue
            codeIntPersonA = person.getCodeInt()
            codeIntPersonB = self.inner.personArray[i].getCodeInt()
            if(codeIntPersonA == codeIntPersonB):
                self.inner.personArray[i] = person
                return 0
        return -1

    def extractPerson(self, codeIntWanted):
        person = None
        for i in range(len(self.inner.personArray)):
            if(person == None):
                continue
            codeInt = self.inner.personArray[i].getCodeInt()
            if(codeInt == codeIntWanted):
                person = self.inner.personArray[i]
            self.inner.personArray[i] = None
        return person

    def cleanDeadPerson(self):
        deadProduct = None
        person = None
        for i in range(len(self.inner.personArray)):
            person = self.inner.personArray[i]
            if(person == None):
                continue
            if(person.getIsDeath()
            and person.getDeadDays() >= 2):
                self.deadArray.append(person)
                self.extractPerson(person.getCodeInt())

#*** ACCESSORS *******************************************************************

    def getPerson(self, personCode):
        getPerson = GetPersonTk()
        return getPerson.inner(self.inner, personCode)

    def setPerson(self, person):
        setPerson = SetPersonTk()
        return setPerson.inner(self.inner, person)

    def addPerson(self, person):
        return self.setPerson(person)

    def getPersonArray(self):
        return self.inner.personArray

    def setPersonArray(self, personArray):
        self.inner.personArray = personArray

    def getSize(self):
        return len(self.inner.personArray)

#*******************************************************************************
