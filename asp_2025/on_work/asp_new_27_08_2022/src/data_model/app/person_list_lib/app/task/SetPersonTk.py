




class SetPersonTk:

    def updatePerson(self, personListPDT, personNew):
        for i in range(len(personListPDT.personArray)):
            person = personListPDT.personArray[i]
            if(person.getCodeInt() == personNew.getCodeInt()):
                personListPDT.personArray[i] = personNew
                return 0
        return -1

    def hasPerson(self, personListPDT, personNew):
        for i in range(len(personListPDT.personArray)):
            person = personListPDT.personArray[i]
            if(person.getCodeInt() == personNew.getCodeInt()):
                return True
        return False

    def inner(self, personListPDT, personNew):
        person = None
        if(personListPDT.isVoid()):
            personListPDT.personArray.append(personNew)
            return 0
        if(self.hasPerson(personListPDT, personNew)):
            self.updatePerson(personListPDT, personNew)
        else:
            personListPDT.personArray.append(personNew)
            return 0
        return -1
