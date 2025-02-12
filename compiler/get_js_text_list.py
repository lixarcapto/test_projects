

from btpy_lib.btpy.src.btpy.Btpy import Btpy
import os
import networkx as nx

def get_js_text_list(directorio):
    """
    Lee todos los archivos .js en un 
    directorio y sus subdirectorios, 
    y devuelve una lista con el 
    contenido de cada archivo.
    """
    archivos_js = []
    def explorar_directorio(directorio):
        for archivo in os.listdir(directorio):
            ruta_completa = os.path.join(directorio, archivo)
            if os.path.isfile(ruta_completa) and archivo.endswith('.js'):
                with open(ruta_completa, 'r', encoding='utf-8') as f:
                    contenido = f.read()
                    archivos_js.append(contenido)
            elif os.path.isdir(ruta_completa):
                explorar_directorio(ruta_completa)
    explorar_directorio(directorio)
    return archivos_js

"""
Este metodo retorna un dict con dos listas; 
la class_list contiene dict con datos de 
clases de cada archivo js
y la no_class_list contiene solo string
de cada archivo js.
Tipos de archivos: script, class
"""
def create_js_file_data(str_js_list):
    dict_result = {
        "class_list":[],
        "no_class_list":[]
    }
    dict_js = {}
    str_js = ""
    dad_class = ""
    type_file_key = "script"
    class_name = ""
    for i in range(len(str_js_list)):
        dict_js = {}
        str_js = str_js_list[i]
        r = Btpy.get_between(str_js, 
            "extends ", "{")
        if(not r == str_js): dad_class = r
        if(not " class " in str_js):
            dict_result["no_class_list"]\
                .append(str_js)
            continue
        type_file_key = "class"
        class_name = Btpy.get_between(str_js, 
            "class ", " ")
        dict_js["extends"] = dad_class\
            .strip()
        dict_js["string"] = str_js
        dict_js["type_file"] = type_file_key\
            .strip()
        dict_js["class_name"] = class_name\
            .strip()
        dict_result["class_list"].append(
            dict_js)
        dad_class = ""
        type_file_key = "script"
        class_name = ""
    return dict_result

"""
Crea un arbol de diccionarios anidados
para ordenar los diccionarios javascript
de clases; con el objetivo de ordenar 
por jerarquia los modulo de clase.
TODO: Hay un error en el arbol asi que debo
crear una implementacion de arbol mejor.
"""
def create_three(dict_js_list):
    dict_js = {}
    three_dict = {}
    # search no dad dict
    for i in range(len(dict_js_list)):
        dict_js = dict_js_list[i]
        if(dict_js["extends"] == ""):
            three_dict[dict_js["class_name"]]\
                = {}
    # search child dict
    
    for i in range(len(dict_js_list)):
        dict_js = dict_js_list[i]
        dad_key = dict_js["extends"]
        if(not dict_js["extends"] == ""):
            three_dict[dad_key]\
               [dict_js["class_name"]] = {}
    return three_dict

def get_order_list(diccionario, camino=[]):
    """
    Realiza una búsqueda en profundidad 
    en un diccionario anidado y devuelve 
    una lista con las claves de los nodos, 
    desde los más profundos hasta los 
    más elevados.
    Args:
        diccionario: El diccionario 
        anidado a explorar.
        camino: Una lista que almacena 
        el camino actual hasta el nodo 
        actual.
    Returns:
        Una lista de listas, donde cada 
        lista interna representa un 
        camino desde la raíz
        hasta un nodo hoja.
    """
    resultados = []
    for clave, valor in diccionario.items():
        nuevo_camino = camino + [clave]
        if isinstance(valor, dict) and valor:  # Verificamos si es un diccionario no vacío
            resultados.extend(
                get_order_list(valor, 
                    nuevo_camino))
        else:
            resultados.append(nuevo_camino)
    return resultados

"""
Busca un diccionario de datos
javascript de clase por la clave
enviada en el array enviado.
"""
def get_dict_js(dict_js_array, key):
    for i in range(len(dict_js_array)):
        if(dict_js_array[i]["class_name"] 
                == key):
            return dict_js_array[i]
    return None

"""
Convierte la lista de javascript string
de clases en una lista de string comun
"""
def write_js_str_as_list(dict_js_list,
        order_list):
    str_list = []
    order_list = order_list[0]
    dict_js = {}
    for i in range(len(order_list)):
        dict_js = get_dict_js(
            dict_js_list,
            order_list[i]
        )
        str_list.append(dict_js["string"])
    return str_list