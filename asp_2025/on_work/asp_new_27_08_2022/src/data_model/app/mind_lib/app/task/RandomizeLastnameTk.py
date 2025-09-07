

from data_access.DataAccess import DataAccess
import random

class RandomizeLastnameTk:

    def inner(self, culture, caste):
        namesData = DataAccess().getNamesData()
        lastnameMidCasteMatrix = namesData.getLastnameMidCasteMatrix()
        lastnameHighCasteMatrix = namesData.getLastnameMidCasteMatrix()
        sizeArray = 0
        randomNumber = 0
        nameArray = None
        resultName = ""
        if(caste == 0):
            nameArray = lastnameMidCasteMatrix[culture]
            sizeArray = len(nameArray) -1
            random.random()
            randomNumber = random.randint(0, sizeArray)
            resultName = nameArray[randomNumber]
        elif(caste == 1):
            nameArray = lastnameHighCasteMatrix[culture]
            sizeArray = len(nameArray) -1
            random.random()
            randomNumber = random.randint(0, sizeArray)
            resultName = nameArray[randomNumber]
        return resultName
