


"""
    Funcion que crea una matrix 2D cargada de datos null
    recibiendo su tamaño en x e y
"""

def create_matrix(size_y, size_x, size_z = -1,
        type = "none"):
    matrix = []
    n = 0
    for y in range(size_y):
        matrix.append([])
        for x in range(size_x):
            if(type == "none"):
                matrix[y].append(None)
            elif(type == "number"):
                matrix[y].append(n)
            n += 1
        # si la matriz tiene eje Z
        else:
            for z in range(size_z):
                if(type == "none"):
                    matrix[y][x].append(None)
                elif(type == "number"):
                    matrix[y][x].append(n)
                n += 1
    return matrix


""" old
def create_matrix(size_x, size_y):
    matrix = [None] * size_y
    for i in range(size_y):
        matrix[i] = [None] * size_x
    return matrix
"""
