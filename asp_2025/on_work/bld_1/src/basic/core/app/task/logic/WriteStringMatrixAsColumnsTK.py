


class WriteStringMatrixAsColumnsTK:

    def inner(self, matrixArray):
        text = ""
        spaces = " " * 5
        quantityColumns = 3
        counterColumns = 0
        for y in range(len(matrixArray)):
            for i in range(len(matrixArray[y])):
                text += matrixArray[y][i]
                if(counterColumns == quantityColumns):
                    counterColumns = 0
                    text += "\n"
                else:
                    text += spaces
                    counterColumns += 1
        return text
