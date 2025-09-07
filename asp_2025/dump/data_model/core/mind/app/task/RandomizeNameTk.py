

from data_access.DataAccess import DataAccess
import random

class RandomizeNameTk:

    def inner(self, culture, gender):
        namesData = DataAccess().getNamesData()
        namesMaleMatrix = namesData.getNamesMaleMatrix()
        namesFemaleMatrix = namesData.getNamesFemaleMatrix()
        sizeArray = 0
        randomNumber = 0
        nameArray = None
        resultName = ""
        if(gender == 0):
            nameArray = namesMaleMatrix[culture]
            sizeArray = len(nameArray) -1
            random.random()
            randomNumber = random.randint(0, sizeArray)
            resultName = nameArray[randomNumber]
        else:
            nameArray = namesFemaleMatrix[culture]
            sizeArray = len(nameArray) -1
            random.random()
            randomNumber = random.randint(0, sizeArray)
            resultName = nameArray[randomNumber]
        return resultName
