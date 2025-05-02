


from .in_range import*
from .sum_in_range import*

"""
Función que desplaza un a otro punto sin 
superar los límites que los ejes enviados 
como intervalos.
TODO: añadir este algoritmo de mover 
puntos a basic things.
"""
# return point
def move_point( 
        old_point:list[int], 
        new_point:list[int], 
        range_space,
    ) -> list[int]:
    range_x = range_space.range_x
    range_y = range_space.range_y
    result_point = [0, 0]
    # mueve al punto dentro del rango
    result_point[0] = sum_in_range(
        old_point[0],
        new_point[0], 
        range_y)
    result_point[1] = sum_in_range(
        old_point[1],
        new_point[1], 
        range_y)
    return result_point