

from data_model.app.mind_lib.core.relation.Relation import Relation

class RelationList:

    LIMIT_RELATION = 100

    def __init__(self):
        self.relationArray = []

    def hasSomeRelation(self):
        if(len(self.relationArray) > 0):
            return True
        return False

    def clean(self):
        self.relationArray.clean()

    def checkIfHasRelationUsingCode(self, personCode):
        relation = None
        if(not self.hasSomeRelation()):
            return False
        for i in range(len(self.relationArray)):
            relation = self.relationArray[i]
            if(relation.getPersonCode() == personCode):
                return True
        return False

    def updateRelation(self, relationProduct):
        for i in range(len(self.relationArray)):
            if(self.relationArray[i].personCode == relationProduct.personCode):
                self.relationArray[i] = relationProduct

    def addRelation(self, value, personCode, type):
        relation = Relation()
        relation.setPersonCode(personCode)
        relation.setValue(value)
        relation.type = type
        if(self.checkIfHasRelationUsingCode(personCode)):
            self.updateRelation(relation)
        else:
            self.relationArray.append(relation)

    def getRelationByType(self, typeString):
        for i in range(len(self.relationArray)):
            if(self.relationArray[i].typeString == typeString):
                return self.relationArray[i]

    def getRelationPersonCodesArray(self):
        codesArray = []
        if(not self.hasSomeRelation()):
            return None
        for e in self.relationArray:
            codesArray.append(e.getPersonCode())
        return codesArray
