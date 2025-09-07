


from data_model.core.person.Person import Person
from data_model.core.market.Market import Market

class PersonTest:

    def inner(self):
        market = Market()
        person = Person()
        for i in range(10):
            market = person.advanceTime(market)
        person.calculeMood()
        print(person.writeData())
        return
