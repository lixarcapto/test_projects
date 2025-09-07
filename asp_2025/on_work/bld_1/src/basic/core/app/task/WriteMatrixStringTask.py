


from basic.core.app.task.FullfillTextTask import FullfillTextTask

class WriteMatrixStringTask:

    def inner(self, matrixOfStringArray):
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
                    text += "[" + FullfillTextTask().inner(matrixOfStringArray[y][x][i],
                    sizeBlockInX) + "]"
                text += "\n"
            text += spaces + "\n"
        return text
