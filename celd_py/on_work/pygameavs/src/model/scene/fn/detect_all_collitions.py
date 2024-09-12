
from .get_all_box import*
from .set_colision_data import*
from detect_collisions.detect_collisions import detect_collisions

def detect_all_collitions(gobject_dict):
    # obtiene los box_square de cada
    # objeto
    box_dict = get_all_box(gobject_dict)
    # detecta los cuadrados colisionados
    # retornando sus claves
    keys_pair_arr = detect_collisions(
            box_dict)
    # asigna las colisiones a cada
    # objeto
    gobject_dict = set_colision_data(
        keys_pair_arr, gobject_dict)
    return gobject_dict
    