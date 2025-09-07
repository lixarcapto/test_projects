


from basic.core.mailbox.Mailbox import Mailbox
#TASK ---------------------------------------------------------------------
from basic.core.graphic.Graphic import Graphic
from basic.core.app.task.CutMatrixTask import CutMatrixTask
from basic.core.app.task.WriteMatrixStringTask import WriteMatrixStringTask
from basic.core.app.task.graphic.PaintImageNamesMatrixInCanvasTK import PaintImageNamesMatrixInCanvasTK
from basic.core.app.task.FullfillTextTask import FullfillTextTask
from basic.core.app.task.graphic.ConvertNumberMapToArrayStringBarsTK import ConvertNumberMapToArrayStringBarsTK
from basic.core.app.task.CreateVoidMatrixTask import CreateVoidMatrixTask
from basic.core.app.task.logic.IsANumberTK import IsANumberTK
from basic.core.app.task.logic.HasTheKeyTK import HasTheKeyTK
from basic.core.app.task.logic.IndexFromMapTK import IndexFromMapTK
from basic.core.app.task.logic.IsALetterTK import IsALetterTK
from basic.core.app.task.logic.ObtainKeyTK import ObtainKeyTK
from basic.core.app.task.logic.RandomIndexTK import RandomIndexTK
from basic.core.app.task.logic.ArrayHasIntTK import ArrayHasIntTK
from basic.core.app.task.logic.WriteStringMatrixAsColumnsTK import WriteStringMatrixAsColumnsTK
from basic.core.app.task.logic.PrintArrayTK import PrintArrayTK
from basic.core.app.task.logic.IndexFromArrayTK import IndexFromArrayTK
from basic.core.app.task.logic.AreAllThoseNumbersTK import AreAllThoseNumbersTK
from basic.core.app.task.logic.AreAllThoseLettersTK import AreAllThoseLettersTK
from basic.core.app.task.logic.ConvertArrayToMapTK import ConvertArrayToMapTK
from basic.core.app.task.ObtainBooleanWithProbabilityTask import ObtainBooleanWithProbabilityTask
from basic.core.app.task.GenerateRandomArrayWithoutRepeatTask import GenerateRandomArrayWithoutRepeatTask
from basic.core.app.task.ExtractStringFromStringTask import ExtractStringFromStringTask
from basic.core.app.task.ArrayHasNumberTask import ArrayHasNumberTask
#-----------------------------------------------------------------
from tkinter import *
from PIL import Image, ImageTk

import random

class Basic:

    def __init__(self):
        self.messagesOnHold = ""

    def graphic(self):
        return Graphic()

    def paintImageNamesMatrixInCanvas(self, canvas, imageNamesMatrix,
    sizeImageArray):
        map = PaintImageNamesMatrixInCanvasTK().inner(canvas, imageNamesMatrix,
        sizeImageArray)
        return map

    def randomIndex(self, maximum):
        return RandomIndexTK().inner(maximum)

    def convertNumberMapToArrayStringBars(self, map, quantityLow,
    quantityMid, spacesToBar, mode):
        return ConvertNumberMapToArrayStringBarsTK().inner(map, quantityLow,
        quantityMid, spacesToBar, mode)

    def writeStringMatrixAsColumns(self, matrixArray):
        return WriteStringMatrixAsColumnsTK().inner(matrixArray)

    def writeNumberMapAsBars(self, map, quantityLow,
    quantityMid, spacesToBar, mode):
        stringArray = self.convertNumberMapToArrayStringBars(map, quantityLow,
        quantityMid, spacesToBar, mode)

    def mailbox(self):
        return Mailbox()

    def indexFromMap(self, map, key):
        return IndexFromMapTK().inner(map, key)

    def indexFromArray(self, array, value):
        return IndexFromArrayTK().inner(array, value)

    def matrix(self, arraySize):
        return CreateVoidMatrixTask().inner(arraySize)

    def cutMatrix3D(self, matrix3D, locationY, locationX, sizeY, sizeX):
        return CutMatrixTask().inner(matrix3D, locationY, locationX,
        sizeY, sizeX)

    def writeMatrixOfStringArray(self, matrixOfStringArray):
        return WriteMatrixStringTask().inner(matrixOfStringArray)

    def writeMatrixOfStringArrayWihoutFill(self, matrixOfStringArray):
        sizeBlockInX = len(matrixOfStringArray[0][0]) * 3
        text = ""
        spaces = "_" * (sizeBlockInX + 2) * len(matrixOfStringArray[0])
        isFirstLine = True
        for y in range(len(matrixOfStringArray)):
            if(isFirstLine):
                text += spaces + "\n"
                isFirstLine = False
            for i in range(len(matrixOfStringArray[0][0])):
                for x in range(len(matrixOfStringArray[y])):
                    text += "[" + matrixOfStringArray[y][x][i] + "]"
                text += "\n"
            text += spaces + "\n"
        return text

    def writeMatrix(self, matrix):
        text = ""
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                text += "[" + str(matrix[y][x]) + "]"
            text += "\n"
        return text

    def printMatrix(self, matrix):
        print(self.writeMatrix(matrix))

    def obtainMessagesOnHold(self):
        message = self.messagesOnHold
        self.messagesOnHold = ""
        return message

    def obtainBooleanWithProbability(self, probability):
        return ObtainBooleanWithProbabilityTask().inner(probability)

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
        return ArrayHasNumberTask().inner(intArray, number)

    def generateRandomArrayWithoutRepeat(self, quantityInt, maxSizeInt):
        return GenerateRandomArrayWithoutRepeatTask().inner(quantityInt,
        maxSizeInt)

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
        return ConvertArrayToMapTK().inner(array)

    def convertStringArrayToMapNumber(self, array, initialNumber):
        map = dict()
        for i in range(len(array)):
            map[array[i]] = initialNumber
        return map

    def printArray(self, array):
        PrintArrayTK().inner(array)

    def printArrayAsText(self, array):
        text = ""
        for e in array:
            text += e + "\n"
        print(text)

    def printMap(self, map):
        n = 0
        text = "map(" + str(len(map)) + "):\n"
        for key in map.keys():
            text += "  map[\"" + key + "\"] = " + str(map[key]) + "\n"
            n += 1
        print(text)

    def extractFromString(self, text, textToFind, endKey):
        task = ExtractStringFromStringTask()
        result = task.inner(text, textToFind,
        endKey)
        self.messagesOnHold += task.messagesOnHold
        return result

    def fullfillText(self, text, size):
        return FullfillTextTask().inner(text, size)

    def obtainKey(self, map, vint):
        return ObtainKeyTK().inner(map, vint)

    def hasTheKey(self, map, key):
        return HasTheKeyTK().inner(map, key)

    def arrayHasInt(self, array, vint):
        return ArrayHasIntTK().inner(array, vint)

    def isANumber(self, letter):
        return IsANumberTK().inner(letter)

    def isALetter(self, letter):
        return IsALetterTK().inner(letter)

    def areAllThoseNumbers(self, text):
        return AreAllThoseNumbersTK().inner(text)

    def areAllThoseLetters(self, text):
        return AreAllThoseLettersTK().inner(text)
