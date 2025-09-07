



from data_model.core.person_list.PersonList import PersonList
from data_model.core.person.Person import Person

class Army:

    def __init__(self):
        self.SIZE_ARMY = 6
        self.personArray = [None] * self.SIZE_ARMY
        for i in range(len(self.personArray)):
            self.personArray[i] = Person()
            self.personArray[i].randomize(0)
        return

    def orderArmy(self):
        for i in range(len(self.personArray)):
            if(self.personArray[i] == None):
                continue
            if(self.personArray[i].inner.getIsDeath()):
                print("encontro muerto")
                self.personArray[i] = None
        #ordena la lista
        newPersonArray = [None] * self.SIZE_ARMY
        n = 0
        for i in range(len(self.personArray)):
            if(self.personArray[i] != None):
                newPersonArray[n] = self.personArray[i]
                n += 1
        self.personArray = newPersonArray

    def thereAreSurvivors(self):
        for i in range(len(self.personArray)):
            if(self.personArray[i] == None):
                continue
            if(not self.personArray[i].inner.getIsDeath()):
                return True
        return False

    def advanceOneDay(self, date, visionData, auditionData, olfactoryData):
        self.personArray[0].advanceOneDay(date, visionData, auditionData, olfactoryData)
        self.orderArmy()
