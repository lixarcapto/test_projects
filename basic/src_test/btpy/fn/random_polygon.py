

from .random_point import*

"""
Función que genera una lista al de puntos 
aleatorios es la cantidad indicada dentro 
del Rango enviado
"""
def random_polygon(quantity:int, 
            range_ar:list[int])\
            ->list[list[int]]:
        point_array = []
        point = None
        for i in range(quantity):
            point = random_point(
                range_ar)
            point_array.append(point)
        return point_array