
import Region as Region
import Person as Person

class Scene:

    personCode = 0

    def __init__(self):
        self.quantityRegion = 10
        self.regionArray = [None] * self.quantityRegion
        self.day = 0
        self.month = 0
        self.year = 0
        self.hour = 0
        self.quantityZones = 0

    def createScenario(self):
        region = Region.Region()
        for i in range(self.quantityRegion):
            region = Region.Region()
            region.setCode(i)
            region.setCoordianteX(i)
            region.setCoordianteY(i)
            self.regionArray[i] = region

    def createPersons(self):
        person = Person.Person()
        baseQuantityPersonByRegion = 6
        for i in range(self.quantityRegion):
            for i in range(baseQuantityPersonByRegion):
                person = Person.Person()
                person.setCode(Scene.personCode)
                self.regionArray[i].addPerson(person)
                Scene.personCode += 1

    def startScene(self):
        self.createScenario()
        self.createPersons()

    def advanceGlobalTime(self):
        self.day += 1
        if(self.day == 4):
            self.month += 1
        if(self.month == 4):
            self.year += 1
        for i in range(self.quantityRegion):
            self.regionArray[i].advanceTime()
