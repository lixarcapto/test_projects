




class CutMatrixTask:

    def inner(self, matrix3D, locationY, locationX, sizeY, sizeX):
        matrix = []
        array = None
        value = None
        for y in range(sizeY):
            array = []
            matrix.append(array)
            for x in range(sizeX):
                value = matrix3D[locationY + y][locationX + x]
                matrix[y].append(value)
        return matrix
