


from ....btpy_checkers.mod.in_range import*
from ..sum_in_range.sum_in_range import*



def sum_point( 
        old_point:list[int], 
        new_point:list[int], 
        range_x:list[int],
        range_y:list[int]
    ) -> list[int]:
    """
    Función que desplaza un a otro 
    punto sin superar los límites 
    que los ejes enviados como 
    intervalos.
    """
    #
    result_point = [0, 0]
    # mueve al punto dentro del rango
    result_point[0] = sum_in_range(
        old_point[0],
        new_point[0], 
        range_x)
    result_point[1] = sum_in_range(
        old_point[1],
        new_point[1], 
        range_y)
    return result_point