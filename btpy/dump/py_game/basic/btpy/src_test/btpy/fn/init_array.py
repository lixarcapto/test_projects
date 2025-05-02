

from ..mod.iterator.Iterator import Iterator
from ..const.abc_tuple import*

"""
    Funcion que sirve para crear un array nuevo y lleno del dato
    indicado. Segun la clave enviada como format añadira un dato
    diferente, estas son:
    * abc para abecedario
    * number para numero
    ademas la clave order indica el orden de los datos de
    menor a mayor o alreves; las claves son normal e invert.
"""
def init_array(range, value = None):
    if(len(range) == 1):
        return create_array(range[0], value, type)
    if(len(range) == 2):
        return create_matrix(range[0], range[1], value, type)
    if(len(range) == 3):
        return create_matrix_3d(range[0], range[1], range[2],
                value, type)

def create_array(size, value, type):
    iterador = Iterator(ABC_TUPLE, True)
    array = []
    n = 0
    for i in range(size):
        if(value == "abc"):
            iterador.next()
            array.append(iterador.get())
        elif(value == "numeric"):
            array.append(n)
            n += 1
        else:
            array.append(value)
    return array

def create_matrix(size_y, size_x, value, type):
    array = []
    iterador = Iterator(ABC_TUPLE, True)
    matrix = []
    n = 0
    for y in range(size_y):
        array = []
        for x in range(size_x):
            if(value == "abc"):
                iterador.next()
                array.append(iterador.get())
            elif(value == "numeric"):
                array.append(n)
                n += 1
            else:
                array.append(value)
        matrix.append(array)
    return matrix

def create_matrix_3d(size_y, size_x, size_z, value, type):
    iterador = Iterator(ABC_TUPLE, True)
    array = []
    matrix = []
    matrix_3d = []
    n = 0
    for y in range(size_y):
        matrix = []
        for x in range(size_x):
            array = []
            for z in range(size_z):
                if(value == "abc"):
                    iterador.next()
                    array.append(iterador.get())
                elif(value == "numeric"):
                    array.append(n)
                    n += 1
                else:
                    array.append(value)
            matrix.append(array)
        matrix_3d.append(matrix)
    return matrix_3d