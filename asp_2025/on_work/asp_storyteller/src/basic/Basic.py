


import random

class Basic:

    def createMapOfInt(self, stringArray, vint):
        map = dict()
        for e in stringArray:
            map[e] = vint
        stringArray = map
        return map

    def randomizeIndexFromArray(self, length):
        if(length > 1):
            result = random.randint(0, length -1)
        else:
            result = array[0]
        return result

    def randomizeElementFromArray(self, array):
        result = array[self.randomizeIndexFromArray(len(array))]
        return result
