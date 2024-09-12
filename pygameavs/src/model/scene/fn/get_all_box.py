



"""
función que obtiene un diccionario 
con las box de todos los objetos  
usando como clave el id
"""
def get_all_box(gobject_dict)\
            ->list[dict]:
    go = None
    square_dict = {}
    # obtiene los box_square de cada
    # objeto
    for k in gobject_dict:
        go = gobject_dict[k]
        square_dict[k] = go.get_box_square()
    return square_dict