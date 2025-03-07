

from ....btpy_checkers.mod.is_point\
    .is_point import is_point_2D
from ....btpy_checkers.mod.is_number.is_number import*

# return point
def center_square(
        POINT_2D:list[int|float], 
        WIDTH:int|float, 
        HEIGHT:int|float)\
        ->list[int|float]:
    """
    TESTED
    This function return the center 
    point of a square.
    """
    if(not is_point_2D(POINT_2D)):
        raise Exception(f"<!>Error: The parameter POINT_2D is not a 2D point in array format; its value is \"{POINT_2D}\" and the type is {type(WIDTH)}.")
    if(not is_number(WIDTH)):
        raise Exception(f"<!>Error: The parameter WIDTH is not a number, its value is \"{WIDTH}\" and the type is {type(WIDTH)}.")
    if(not is_number(HEIGHT)):
        raise Exception(f"<!>Error: The parameter HEIGHT is not a number, its value is \"{HEIGHT}\" and the type is {type(WIDTH)}.")
    if(WIDTH <= 0):
        raise Exception(f"<!>Error: The parameter WIDTH cannot be 0 or less than zero, its value is \"{WIDTH}\".")
    if(HEIGHT <= 0):
        raise Exception(f"<!>Error: The parameter HEIGHT cannot be 0 or less than zero, its value is \"{HEIGHT}\".")
    return [
        POINT_2D[0] + WIDTH / 2,
        POINT_2D[1] + HEIGHT / 2
    ]