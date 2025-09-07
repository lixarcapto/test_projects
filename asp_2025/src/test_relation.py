

from model.mod.citizen.mod.relationship.Relationship import Relationship

def main():
    rel = Relationship()
    id_ = 6
    for i in range(3):
        rel.set_relation(id_, "FAMILY", 105)
        print(rel.get_relation(id_))

main()