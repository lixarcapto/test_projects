


from data_model.core.person_list.PersonList import PersonList
from data_model.core.market.Market import Market

class PersonListTest:

    def inner(self):
        market = Market()
        personList = PersonList()
        personList.createInitialPerson(12)
        market = personList.advanceTime(market)
        print(personList.writePersonData())
