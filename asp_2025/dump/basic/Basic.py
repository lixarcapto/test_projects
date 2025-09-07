

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

    def haveNumberInArray(self, intArray, number):
        for e in intArray:
            if(e == number):
                return True
        return False

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

    def randomizeCoordinates(self, quantity, sizeY, sizeX):
        coordinatesMatrix = []
        arrayX = self.generateRandomArrayWithoutRepeat(quantity, sizeX)
        arrayY = self.generateRandomArrayWithoutRepeat(quantity, sizeY)
        for i in range(quantity):
            coordinateArray = [0] * 2
            coordinateArray[0] = arrayY[i]
            coordinateArray[1] = arrayX[i]
            coordinatesMatrix.append(coordinateArray)
        return coordinatesMatrix

    def convertArrayToMap(self, array):
        map = dict()
        for i in range(len(array)):
            map[array[i]] = i
        return map

    def printArray(self, array):
        n = 0
        text = "array(" + str(len(array)) + "):\n"
        for e in array:
            text += "  array[" + str(n) + "] = " + e + "\n"
            n += 1
        print(text)

    def printMap(self, map):
        n = 0
        text = "map(" + str(len(map)) + "):\n"
        for key in map.keys():
            text += "  map[\"" + key + "\"] = " + str(map[key]) + "\n"
            n += 1
        print(text)
