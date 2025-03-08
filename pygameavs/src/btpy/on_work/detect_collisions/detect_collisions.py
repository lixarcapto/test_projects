

from btpy.src.btpy.Btpy import Btpy


def detect_collisions(square_dict):
    """
    función que detecta las colisiones 
    de una lista de cuadrados indexados 
    y almacena los índices de los objetos 
    qué colisionan entre sí para 
    retornarlos.
    """
    collision_index_arr = []
    keys_pair_arr = []
    for k1 in square_dict:
         for k2 in square_dict:
            if(k1 == k2): continue
            is_collide = Btpy.is_colliding_rect(
                square_dict[k1],
                square_dict[k2]
            )
            if(is_collide):
                keys_pair_arr.append([k1, k2])
    return keys_pair_arr