

import sys
import os

# Obtiene la ruta absoluta del directorio del script actual.
directorio_actual = os.path.dirname(os.path.abspath(__file__))
# Sube dos niveles en la jerarquía de directorios.
directorio_padre = os.path.dirname(directorio_actual)
directorio_abuelo = os.path.dirname(directorio_padre)
# Añade el directorio abuelo al sys.path.
sys.path.append(directorio_abuelo)

from btpy.Btpy import Btpy

def main(): 
    data = Btpy.MultikeyDict()
    # prueba si set funciona
    data.set(["perro", "lobo", "canido"], 
        "canidos")
    r = data.get_most_matched(["lobo"])
    print("canidos" == r)
    # prueba si has funciona
    r = data.has(["lobo"])
    print(r == True)
    r = data.has(["perro"])
    print(r == True)
    r = data.has(["canido"])
    print(r == True)
    # prueba si remove funciona
    data.set(["gato, leon, felino"], 
        "felinos")
    data.remove_all_with(["leon"])
    r = data.has(["leon"])
    print(r == False)
    # set no recibe un array
    try:
        data.set("perro", 
        "canidos")
    except Exception as e:
        print(True, e)
    # set no recibe un array string
    try:
        data.set([1, 2, 3, 4], 
        "canidos")
    except Exception as e:
        print(True, e)
    # si get no es un string
    try:
        data.get_most_matched(5)
    except Exception as e:
        print(True, e)
    # si remove no es un string
    try:
        data.remove_all_with(5)
    except Exception as e:
        print(True, e)
    print(data.dict)

main()