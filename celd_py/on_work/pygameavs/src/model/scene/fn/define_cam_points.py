

from ...fn.translade_points import translade_points
from .set_point_in_cam import*

"""
función Que  obtiene los puntos en 
cámara de los objetos enviados en 
una lista
"""
def define_cam_points(gobject_arr:list, 
        cam_square:dict[int])->list:
    # crea lista de puntos
    point_arr = []
    go = None
    for go in gobject_arr:
        point_arr.append(go.point)
    # traduce puntos
    translate_points = translade_points(
        point_arr,
        cam_square["x"],
        cam_square["y"],
        cam_square["width"],
        cam_square["height"]
    )
    # asigna los puntos a los objetos
    gobject_arr = set_point_in_cam(
        gobject_arr,
        translate_points
    )
    print(f"from define_cam_points gobject_arr {len(gobject_arr)} translate_points {len(translate_points)}")
    return gobject_arr