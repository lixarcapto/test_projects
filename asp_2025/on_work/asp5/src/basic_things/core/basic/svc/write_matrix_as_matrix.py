

"""
    Funcion que escribe una matriz 2D como una matrix
    en formato texto.
"""
# return string
def write_matrix_as_matrix(matrix):
    text = "matrix = [\n"
    margin = " " * 3
    for y in range(len(matrix)):
        text += margin + "array " + str(y) + " = ["
        for x in range(len(matrix[y])):
            text += str(matrix[y][x])
            if(x < len(matrix[y]) -1):
                text += ","
        if(y < len(matrix) -1):
            text += ","
        text += "]\n"
    text += "]\n"
    return text
