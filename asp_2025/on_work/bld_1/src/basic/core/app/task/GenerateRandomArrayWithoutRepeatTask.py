


from basic.core.app.task.ArrayHasNumberTask import ArrayHasNumberTask
import random

class GenerateRandomArrayWithoutRepeatTask:

    def inner(self, quantityInt, maxSizeInt):
        randomizedIntArray = [None] * quantityInt
        randomInt = 0
        for i in range(quantityInt):
            while(True):
                randomInt = random.randint(0, maxSizeInt)
                if(ArrayHasNumberTask().inner(randomizedIntArray,
                randomInt) == False):
                    randomizedIntArray[i] = randomInt
                    print("random Number without repeat: " + str(randomInt))
                    break
        return randomizedIntArray
