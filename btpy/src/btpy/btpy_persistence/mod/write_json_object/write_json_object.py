

import json

def write_json_object(
        PATH: str, 
        DICT: dict)-> bool:
    """
    Crea un archivo JSON y escribe en 
    él un diccionario de Python.
    Returns:
        bool: Retorna True si el archivo 
        se creó y escribió con éxito, 
        False en caso contrario.
    """
    f_path = PATH
    if(".json" not in PATH):
        f_path += ".json"
    try:
        # Abre el archivo en modo escritura ('w').
        # Si el archivo no existe, lo crea. Si ya existe, borra su contenido y escribe el nuevo.
        # 'encoding="utf-8"' es crucial para manejar correctamente caracteres especiales (ñ, tildes, etc.).
        with open(f_path, 'w', encoding='utf-8') as archivo_json:
            # json.dump() toma el diccionario 'datos_diccionario' y lo escribe directamente al 'archivo_json'.
            # 'indent=4' hace que el JSON sea fácil de leer, añadiendo 4 espacios de indentación.
            # 'ensure_ascii=False' permite que los caracteres no ASCII se escriban tal cual,
            # lo que mejora la legibilidad para caracteres latinos, por ejemplo.
            json.dump(DICT, archivo_json, indent=4, ensure_ascii=False)
        print(f"✅ Archivo '{f_path}' creado y diccionario guardado exitosamente.")
        return True
    except TypeError as e:
        print(f"❌ Error de tipo: El objeto '{DICT}' no se puede serializar a JSON. Detalles: {e}")
        return False
    except IOError as e:
        print(f"❌ Error de entrada/salida: No se pudo escribir el archivo '{PATH}'. Detalles: {e}")
        return False
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado al escribir el JSON. Detalles: {e}")
        return False