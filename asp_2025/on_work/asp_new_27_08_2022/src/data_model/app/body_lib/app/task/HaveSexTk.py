

import random
from data_model.app.body_lib.app.task.MakeABabyBodyTk import MakeABabyBodyTk
from data_access.DataAccess import DataAccess

class HaveSexTk:

    def inner(self, personBodyA, personBodyB):
        personKeys = DataAccess().getPersonData()
        makeABabyBody = MakeABabyBodyTk()
        arrayToRandomize = None
        #personA.needs.haveSex = True
        personBodyA.hasGonorrhea = personBodyB.hasGonorrhea
        personBodyA.hasAIDS = personBodyB.hasAIDS
        bodyArray = None
        #TODO....añadir que detecte la madre y el padre
        if(personBodyA.getGender() == personKeys.SEX.FEMALE):
            bodyArray = makeABabyBody.inner(personBodyA, personBodyB)
            personBodyA = bodyArray[0]
            personBodyB = bodyArray[1]
        if(personBodyA.getGender() == personKeys.SEX.HERMAPHRODITE_FEMALE):
            bodyArray = makeABabyBody.inner(personBodyA, personBodyB)
            personBodyA = bodyArray[0]
            personBodyB = bodyArray[1]
        array = []
        array.append(personBodyA)
        array.append(personBodyB)
        return array
