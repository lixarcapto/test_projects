

import json

def read_json_object(PATH:str)->dict:
    """
    Funcion que lee un archivo json
    y lo convierte en un objeto dict
    """
    try:
        with open(PATH, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        print(f"Error: El archivo '{PATH}' no fue encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Error: El archivo '{PATH}' no contiene JSON válido.")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None