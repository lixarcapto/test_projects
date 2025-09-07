


class Relation:

    def __init__(self):
        self.value = 0
        self.typeString = "none"
        self.personCode = 0

    def getPersonCode(self):
        return self.personCode

    def setPersonCode(self, number):
        self.personCode = number

    def setValue(self, number):
        self.value = number

    def setType(self, typeString):
        self.typeString = typeString
