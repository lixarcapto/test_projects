

from btpy.src.btpy.Btpy import Btpy


def create_bar(part, limit, point, 
            size_x):
    """
    Función que Calcula los dos puntos 
    para una barra de recursos basado en  
    el total,  el tamaño máximo y una 
    parte del total.
    """
    point2 = point.copy()
    # calcula el porcentaje de recursos
    percent = Btpy.percent_from_part(
        part,
        limit
    )
    # calcula el tamaño en x final
    size_line_x = Btpy.part_from_percent(
        percent,
        size_x
    )
    # evita el valor negativo de la barra
    point2[0] += round(size_line_x)
    line_dict = {
        "point1":point,
        "point2": point2
    }
    return line_dict