


from btpy_lib.btpy.src.btpy.Btpy import Btpy

"""
Crea un arbol de diccionarios anidados
para ordenar los diccionarios javascript
de clases; con el objetivo de ordenar 
por jerarquia los modulo de clase.
TODO: Hay un error en el arbol asi que debo
crear una implementacion de arbol mejor.
"""
def create_class_three(script_data_js):
    data_class = None
    three = Btpy.Three()
    # search no dad dict
    for i in range(len(script_data_js)):
        data_class = script_data_js[i]
        if(data_class.extends_key == ""):
            three.set_in_node(
                data_class.class_name)
    # search child dict
    
    for i in range(len(script_data_js)):
        data_class = script_data_js[i]
        dad_key = data_class.extends_key
        if(not data_class.extends_key == ""):
            three.set_in_node(
                data_class.class_name, 
                dad_key
            )
    return three