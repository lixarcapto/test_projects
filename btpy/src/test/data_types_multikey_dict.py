

import sys
import os

# Obtiene el directorio del script actual
current_dir = os.path.dirname(os.path.abspath(__file__))
# Obtiene el directorio padre
parent_dir = os.path.dirname(current_dir)
# Agrega el directorio padre a sys.path
sys.path.append(parent_dir)

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