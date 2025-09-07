



from data_model.core.person_list.PersonList import PersonList

class TestPersonList:

    def __init__(self):
        personList = PersonList()
        p1 = personList.createPerson()
        personList.setPerson(p1)
        personList.createInitialPerson(0, 6)
        code = personList.obtainRandomPersonCode()
        print(personList.writeAllPersonDescription())
        personList.produceWorkFromAllPerson()
        return
