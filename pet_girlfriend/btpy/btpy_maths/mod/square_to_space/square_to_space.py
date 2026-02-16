

def square_to_space(POINT, size_x, size_y):
    """
    Funcion que convierte un square dict 
    en un space range.
    """
    range_x = [0, 0]
    range_y = [0, 0]
    range_x[0] = POINT[0]
    range_x[1] = POINT[0] + size_x
    range_y[0] = POINT[1]
    range_y[1] = POINT[1] + size_x
    return {
        "range_x":range_x,
        "range_y":range_y
    }