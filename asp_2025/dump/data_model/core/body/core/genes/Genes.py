


import random

class Genes:

    def __init__(self):
        self._skinColor = 0
        self._noseType = 0
        self._eyeType = 0
        self._eyeColor = 0
        self._jawType = 0
        self._heightLimit = 0
        self._muscleLimit = 0
        self._hairColor = 0
        self._frecklesType = 0
        self._hairType = 0
        self._limitFacialHair = 0

    def randomPositive(self, maximum):
        return random.randint(0, maximum)

    def randomizeGenes(self):
        self.setSkinColor(self.randomPositive(5))
        self.setNoseType(self.randomPositive(5))
        self.setEyeType(self.randomPositive(5))
        self.setEyeColor(self.randomPositive(5))
        self.setJawType(self.randomPositive(5))
        self.setHeightLimit(self.randomPositive(5))
        self.setMuscleLimit(self.randomPositive(5))
        self.setHairColor(self.randomPositive(5))
        self.setFrecklesType(self.randomPositive(5))
        self.setHairType(self.randomPositive(5))
        self.setLimitFacialHair(self.randomPositive(5))

    def convertToIntArray(self):
        array = []
        array.append(self.getSkinColor())
        array.append(self.getNoseType())
        array.append(self.getEyeType())
        array.append(self.getEyeColor())
        array.append(self.getJawType())
        array.append(self.getHeightLimit())
        array.append(self.getMuscleLimit())
        array.append(self.getHairColor())
        array.append(self.getFrecklesType())
        array.append(self.getHairType())
        array.append(self.getLimitFacialHair())
        return array

    def convertIntArrayToGenes(self, intArray):
        self.setSkinColor(intArray[0])
        self.setNoseType(intArray[1])
        self.setEyeType(intArray[2])
        self.setEyeColor(intArray[3])
        self.setJawType(intArray[4])
        self.setHeightLimit(intArray[5])
        self.setMuscleLimit(intArray[6])
        self.setHairColor(intArray[7])
        self.setFrecklesType(intArray[8])
        self.setHairType(intArray[9])
        self.setLimitFacialHair(intArray[10])

    def setSkinColor(self, vInt):
        self._skinColor = vInt

    def getSkinColor(self):
        return self._skinColor

    def setNoseType(self, vInt):
        self._noseType = vInt

    def getNoseType(self):
        return self._noseType

    def setEyeType(self, vInt):
        self._eyeType = vInt

    def getEyeType(self):
        return self._eyeType

    def setEyeColor(self, vInt):
        self._eyeColor = vInt

    def getEyeColor(self):
        return self._eyeColor

    def setJawType(self, vInt):
        self._jawType = vInt

    def getJawType(self):
        return self._jawType

    def setHeightLimit(self, vInt):
        self._heightLimit = vInt

    def getHeightLimit(self):
        return self._heightLimit

    def setMuscleLimit(self, vInt):
        self._muscleLimit = vInt

    def getMuscleLimit(self):
        return self._muscleLimit

    def setHairColor(self, vInt):
        self._muscleLimit = vInt

    def getHairColor(self):
        return self._hairColor

    def getFrecklesType(self):
        return self._frecklesType

    def setFrecklesType(self, vInt):
        self._frecklesType = vInt

    def getHairType(self):
        return self._hairType

    def setHairType(self, vInt):
        self._hairType = vInt

    def getLimitFacialHair(self):
        return self._limitFacialHair

    def setLimitFacialHair(self, vInt):
        self._limitFacialHair = vInt
