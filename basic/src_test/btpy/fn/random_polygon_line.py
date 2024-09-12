

from .random_point import*

"""
Función que genera un polígono de 
líneas aleatorio en el rango enviado 
con el número de líneas indicado.
"""
def random_polygon_line(quantity:int, 
            range_ar:list[int]|list[float])\
            -> list[list[int] \
            |list[list[float]]]:
        line_arr = []
        line = []
        point_1 = []
        point_2 = []
        is_first = True
        for i in range(quantity):
            line.clear()
            point_1 = point_2
            point_2 = random_point(
                range_ar)
            if(not is_first):
                line.append(point_1)
                line.append(point_2)
                line_arr.append(line.copy())
            if(is_first):
                is_first = False
        return line_arr