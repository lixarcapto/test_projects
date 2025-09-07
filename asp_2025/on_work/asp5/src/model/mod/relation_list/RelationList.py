

from .Relation import Relation

class RelationList:

    RELATION_KEYS = [
        "family",
        "distant",
        "another"
    ]

    def __init__(self):
        self.relations_array = []

    def write(self):
        text = ""
        for relation in self.relations_array:
            text += str(relation.code) + "/ "
            text += str(relation.point) + " "
            text += relation.type
        return text

    def relate(self, person, quantity, type):
        if(not type in RelationList.RELATION_KEYS):
            print("=> Error in RelationList.relate")
            return None
        relation = None
        if(self.has_relation(person.data.code)):
            relation = self.get_relation(person.data.code)
            relation.point += quantity
            self.set_relation(relation)
        else:
            relation =  self \
                .create_new_relation(person.data.code, type)
            self.relations_array.append(relation)

    def has_relation(self, code):
        for e in self.relations_array:
            if(e.code == code):
                return True
        return False

    def set_relation(self, new_relation):
        relation = None
        for i in range(len(self.relations_array)):
            relation = self.relations_array[i]
            if (relation.code == new_relation.code):
                self.relations_array[i] = new_relation

    def get_relation(self, code):
        for relation in self.relations_array:
            if relation.code == code: return relation

    def create_new_relation(self, code, type):
        relation = Relation()
        relation.code = code
        relation.type = type
        return relation
