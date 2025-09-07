

from ..set_in_range.set_in_range import*

def set_point_in_range(
        POINT_LIST:list[list[int]],
        RANGE_X:list[list[int]], 
        RANGE_Y:list[list[int]])\
        ->list[list[int]]:
    p_result = [0, 0]
    p_result[0] = set_in_range(
        POINT_LIST[0],
        RANGE_X
    )
    p_result[1] = set_in_range(
        POINT_LIST[1],
        RANGE_Y
    )
    return p_result