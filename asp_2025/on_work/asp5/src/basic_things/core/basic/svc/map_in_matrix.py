


"""
    Funcion que recorre un map2D o map3D aplicando una
    funcion a cada elemento
"""
# return matrix
def map_in_matrix(function, matrix):
    has_z_axe = False
    if(type([]) == type(matrix[0][0])): has_z_axe = True
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if(not has_z_axe):
                matrix[y][x] = function(\
                    matrix[y][x])
            else:
                for z in range(len(matrix[y][x])):
                    matrix[y][x][z] = function(\
                        matrix[y][x][z])
    return matrix
