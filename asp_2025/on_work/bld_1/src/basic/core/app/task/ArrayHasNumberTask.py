



class ArrayHasNumberTask:

    def inner(self, intArray, number):
        for e in intArray:
            if(e == number):
                return True
        return False
