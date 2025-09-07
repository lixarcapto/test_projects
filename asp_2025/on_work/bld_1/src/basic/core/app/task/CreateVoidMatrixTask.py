



class CreateVoidMatrixTask:

    def inner(self, arraySize):
        matrix = []
        array = None
        sizeY = arraySize[0]
        sizeX = arraySize[1]
        for y in range(sizeY):
            array = []
            matrix.append(array)
            for x in range(sizeX):
                matrix[y].append(None)
        return matrix
