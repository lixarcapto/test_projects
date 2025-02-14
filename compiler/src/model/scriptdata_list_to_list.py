


"""
Convierte la lista de script_data_js
 en una lista de string comun
"""
def script_data_list_to_list(
        script_data_list,
        order_list):
    str_list = []
    script_data = None
    for i in range(len(order_list)):
        script_data = get_dict_js(
            script_data_list,
            order_list[i]
        )
        str_list.append(
            script_data.string_js)
    return str_list

"""
Busca un diccionario de datos
javascript de clase por la clave
enviada en el array enviado.
"""
def get_dict_js(dict_js_array, key):
    for i in range(len(dict_js_array)):
        print("class_name", 
              dict_js_array[i].class_name,
              "key", key)
        if(dict_js_array[i].class_name 
                == key):
            return dict_js_array[i]
    return None