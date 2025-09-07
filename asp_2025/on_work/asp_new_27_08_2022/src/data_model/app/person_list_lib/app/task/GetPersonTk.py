


class GetPersonTk:

    def inner(self, personListPDT, personCode):
        person = None
        if(personListPDT.isVoid()):
            return None
        for i in range(len(personListPDT.personArray)):
            person = personListPDT.personArray[i]
            if(person.getCodeInt() == personCode):
                return person
        return None
