

from ....btpy_random.mod.randint_list.randint_list import*

def random_polygon(quantity:int, 
            range_ar:list[int])\
            ->list[list[int]]:
    """
    Función que genera una lista 
    al de puntos aleatorios es la 
    cantidad indicada dentro del 
    Rango enviado
    """
    point_array = []
    point = None
    for i in range(quantity):
        point = randint_list(
            2, range_ar)
        point_array.append(point)
    return point_array