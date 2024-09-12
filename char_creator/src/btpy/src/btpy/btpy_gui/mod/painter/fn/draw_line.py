

"""
    Función envoltorio para el método paint 
    del Canvas tkinter.
    """
def draw_line(painter_data, 
            point_ar1, point_ar2, 
            fill = "white", 
            width = 1):
    painter_data.widget.create_line(
            point_ar1[0],
            point_ar1[1],
            point_ar2[0],
            point_ar2[1],
            fill= fill, 
            width= width
    )
    return painter_data

"""
    Función envoltorio para el método paint 
    del Canvas tkinter. Esta función no tiene 
    ancho ni color, porque esas son 
    propiedades de la clase painter.
    """
def draw_line_arr(painter_data, 
            line_arr, 
            fill = "white", 
            width = 1):
    point_1 = 0
    point_2 = 0
    for line in line_arr:
        point_1 = line[0]
        point_2 = line[1]
        painter_data.widget.create_line(
            point_1[0],
            point_1[1],
            point_2[0],
            point_2[1],
            fill= fill, 
            width= width
        )
    return painter_data