

from ..is_point.is_point import is_point_2D
from ..is_number.is_number import*

def is_point_in_rect(
        POINT2D:list[int|float], 
        RECT_ORIGEN_POINT2D:list[int|float], 
        HEIGHT:int|float, 
        WIDTH:int|float
        )-> bool:
    """
    Function that returns true if the 
    sent 2D point is inside the sent 
    rectangle; and returns false if 
    it is not inside.
    """
    if(not is_number(WIDTH)):
        raise Exception(f"<!>Error: parameter WIDTH(\"{WIDTH}\") is not a number.")
    if(not is_number(HEIGHT)):
        raise Exception(f"<!>Error: parameter HEIGHT(\"{HEIGHT}\") is not a number.")
    if(not is_point_2D(POINT2D)):
        raise Exception(f"<!>Error: parameter POINT2D(\"{POINT2D}\") It is not a 2d point in array format.")
    if(not is_point_2D(RECT_ORIGEN_POINT2D)):
        raise Exception(f"<!>Error: parameter RECT_ORIGEN_POINT2D(\"{RECT_ORIGEN_POINT2D}\") It is not a 2d point in array format.")
    x, y = POINT2D
    x_origen = RECT_ORIGEN_POINT2D[0]
    y_origen = RECT_ORIGEN_POINT2D[1]
    x_min = x_origen
    y_min = y_origen
    x_max = x_origen + WIDTH
    y_max = y_origen + HEIGHT
    if ((x_min <= x <= x_max) 
    and (y_min <= y <= y_max)):
        return True
    else:
        return False