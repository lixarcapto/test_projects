

import random

class Basic:

    def obtainBooleanWithProbability(self, probability):
        result = random.randint(0, 100)
        if(result < probability):
            return True
        return False

    def convertMatrixToMap(self, matrix):
        map = dict()
        for i in range(len(matrix)):
            map[matrix[i][0]] = matrix[i][1]
        return map

    def randomizeIntFromArray(self, intArray):
        if(len(intArray) == 0):
            return 0
        randomIndex = random.randint(0, len(intArray) -1)
        return intArray[randomIndex]

    def generateRandomArrayWithoutRepeat(self, quantityInt, maxSizeInt):
        randomizedIntArray = [None] * quantityInt
        randomInt = 0
        for i in range(quantityInt):
            while(True):
                randomInt = random.randint(0, maxSizeInt)
                if(self.haveNumberInArray(randomizedIntArray, randomInt) == False):
                    randomizedIntArray[i] = randomInt
                    print("random Number without repeat: " + str(randomInt))
                    break
        return randomizedIntArray
