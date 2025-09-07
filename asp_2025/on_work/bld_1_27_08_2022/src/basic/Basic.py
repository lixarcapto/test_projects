

import random

class Basic:

    def __init__(self):
        self.messagesOnHold = ""

    def obtainMessagesOnHold(self):
        message = self.messagesOnHold
        self.messagesOnHold = ""
        return message

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

    def extractFromString(self, text, textToFind, endKey):
        indexInit = text.find(textToFind)
        char = ""
        i = indexInit + len(textToFind)
        result = ""
        textFinal = ""
        nameError = "<!>Error extractFromString()"
        if(len(text) < 2):
            self.messagesOnHold += nameError + " text less than 2 [" + text + "]."
            return ""
        if(len(text) < 1):
            self.messagesOnHold += nameError + " textToFind less than 1 [" + textToFind + "]."
            return ""
        while(i < len(text)):
            char = text[i:i + 1]
            if(char == endKey):
                result = textFinal
                break
            if(len(text)-1 == i):
                self.messagesOnHold += nameError + " not has endkey  [" + endKey + "]."
                return ""
            i += 1
            textFinal += char
            if(i > 1000):
                self.messagesOnHold += nameError + " limit iteration " + str(i) + "."
                result = ""
                break
        return result

    def fullfillText(self, text, size):
        sizeMaximum = size
        if(len(text) < sizeMaximum):
            spacesRemaining = sizeMaximum - len(text)
            addText = " " * spacesRemaining
            text += addText
        return text

    def obtainKey(self, map, value):
        for e in map.keys():
            if(map[e] == value):
                return e

    def hasTheKey(self, map, key):
        for e in map.keys():
            if(e == key):
                return True
        return False
