


#XXX
def center_square_by_point(
    punto_a_centrar, 
    sup_point, 
    inf_point,
    size_square
    ):
    mid_square = round(size_square/2)
    new_sup_point = sup_point.copy()
    new_inf_point = inf_point.copy()
    new_sup_point[0] = punto_a_centrar[0] - mid_square
    new_sup_point[1] = punto_a_centrar[1] - mid_square
    new_inf_point[0] = punto_a_centrar[0] + mid_square
    new_inf_point[1] = punto_a_centrar[1] + mid_square
    return [new_sup_point, new_inf_point]
        
