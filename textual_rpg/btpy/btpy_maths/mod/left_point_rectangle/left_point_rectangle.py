


def left_point_rectangle(
        range_location:list[int], 
        size_x:int, size_y:int)->list[int]:
    """
    calcula las coordenadas del punto 
    inferior izquierdo de un rectángulo 
    dado su ubicación superior derecha 
    y su tamaño.
    """
    height = size_x
    width = size_y
    top_right_y = range_location[0]
    top_right_x = range_location[1]
    bottom_left_x = top_right_x + width
    # Calculate bottom-left x-coordinate
    bottom_left_y = top_right_y + height
    # Calculate bottom-left y-coordinate
    point_ar = [bottom_left_y, bottom_left_x]
    return point_ar