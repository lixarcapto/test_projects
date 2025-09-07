



from data_model.core.person.Person import Person

class TestPerson:

    def __init__(self):
        personA = Person()
        personA.randomize(0)
        print(personA.writePersonUpdate(0))
        personB = Person()
        personB.randomize(0)
        personProductArray = personA.haveSex(personA.inner, personB.inner)
        personA.inner = personProductArray[0]
        personB.inner = personProductArray[1]
        bodyBaby = personA.takeTheBabyOut()
        print("work: " + str(personA.produceWork()))
        #personA.advanceOneDay()
        return
