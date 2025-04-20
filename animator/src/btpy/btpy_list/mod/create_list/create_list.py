


def create_list(size:list)->list:
    """
     función que genera una lista con 
     los tamaños determinados ya 
     inicializada con valores None;  
     los tamaños deben enviarse como 
     una lista de máximo 3 de largo de 
     números enteros Qué indican en este 
     orden el tamaño en y, x y z.
    """
    dimension = len(size)
    if(dimension == 1):
        return __fill_with_none(size[0])
    elif(dimension == 2):
        return __create_matrix_2d(size[0], 
            size[1])
    elif(dimension == 3):
        return __create_matrix_3d(size[0], 
            size[1], size[2])
    
def __create_matrix_3d(size_y, size_x, size_z):
    matrix = []
    array = []
    for y in range(size_y):
        array = __create_matrix_2d(size_x, 
            size_z)
        matrix.append(array)
    return matrix
    
def __create_matrix_2d(size_y, size_x):
    array = []
    for y in range(size_y):
            array.append(
                __fill_with_none(size_x)
            )
    return array

def __fill_with_none(size):
    return [None for e in range(size)]


                
