



"""
función que obtiene la lista de 
objetos colisionados de un objeto 
por su identificador
"""
def get_collision_with(id:str, gobject_dict)\
            ->list[str]:
        go = gobject_dict[id]
        id_arr = go.get_collision_id()
        print(f"camara {id} colisiono con {id_arr}; {go.was_free=} from get_collision_with" )
        gobject_arr = []
        e = None
        for id_collition in id_arr:
            e = gobject_dict[id_collition]
            gobject_arr.append(e)
        return gobject_arr