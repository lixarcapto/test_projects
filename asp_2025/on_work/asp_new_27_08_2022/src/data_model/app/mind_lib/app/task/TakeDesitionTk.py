


import random
from data_access.DataAccess import DataAccess

class TakeDesitionTk:

    def inner(self, mindProduct):
        personKeys = DataAccess().getPersonData()
        randomInt = random.randint(0, personKeys.DESITION.LIMIT)
        mindProduct.desition = randomInt
        meetFriendDesition = ["saludar", "sexo", "pelear"]
        if(mindProduct.desition == 8):
            randomValue = random.randint(0, len(meetFriendDesition) -1)
            mindProduct.desitionGoal = randomValue
        return mindProduct
