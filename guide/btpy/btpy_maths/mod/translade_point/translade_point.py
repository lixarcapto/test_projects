

def translade_point( 
        POINT_TO_MOVE:list[int|float], 
        POINT_AREA:list[int|float])\
        ->list[int|float]:
    """
    Funcion que translada un punto hacia
    un area determinada.
    """
    POINT_R:list = [0, 0]
    POINT_R[0] = POINT_TO_MOVE[0] \
        - POINT_AREA[0]
    POINT_R[1] = POINT_TO_MOVE[1] \
        - POINT_AREA[1]
    return POINT_R