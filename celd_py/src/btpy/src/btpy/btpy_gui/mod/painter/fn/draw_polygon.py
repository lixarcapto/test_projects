


from .draw_line import*

"""
    Función que dibuja un array de puntos 
    conectados en el canvas.
"""

def draw_polygon(painter_data, 
            poligon:list[list], fill = "white", 
            width = 1)\
            -> None:
    final_point = [0, 0]
    is_first = True
    for point_ar in poligon:
            if(is_first):
                is_first = False
            else:
                painter_data = draw_line(
                    painter_data,
                    point_ar,
                    final_point,
                    fill, 
                    width
                )
            final_point = point_ar
    return painter_data
        