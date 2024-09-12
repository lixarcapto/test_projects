



"""
función que asigna una lista de 
claves  de colisión a los objetos 
colisionados.
"""
def set_colision_data( 
            keys_pair_arr:list[str],
            gobject_dict)->None:
        go = None
        k1 = ""
        k2 = ""
        for keys_pair in keys_pair_arr:
            k1 = keys_pair[0]
            k2 = keys_pair[1]
            gobject_dict[k2]\
                .add_colition_id(k1)
            gobject_dict[k1]\
                .add_colition_id(k2)
        return gobject_dict