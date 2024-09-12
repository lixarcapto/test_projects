

from .get_collision_with import*
from .define_cam_points import*

"""
función que obtiene todos los 
objetos que se encuentran en 
el área de la cámara con sus 
puntos de camara traducidos
"""
def get_object_to_render(cam_id, 
        gobject_dict):
    # obtiene la camara
    go_cam = gobject_dict[cam_id]
    # deteca colisiones
    object_arr = get_collision_with(cam_id, 
        gobject_dict)
    # traduce los puntos
    object_arr = define_cam_points(
        object_arr,
        go_cam.get_box_square()
    )
    return object_arr