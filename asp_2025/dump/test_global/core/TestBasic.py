




from basic.Basic import Basic

class TestBasic:

    def __init__(self):
        print("generateRandomArrayWithoutRepeat()")
        intArray =  Basic().generateRandomArrayWithoutRepeat(10, 30)
        for e in intArray:
            print(str(e))
        print("randomizeCoordinates()")
        coordinatesArray = Basic().randomizeCoordinates(10, 100, 100)
        for e in coordinatesArray:
            print("y: " + str(e[0]) + "/x: " + str(e[1]))
        return
