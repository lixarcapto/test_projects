

import os

def create_folder(PATH: str) -> bool:
    """
    Crea una carpeta en la ruta 
    especificada.
    bool: True si la carpeta fue 
    creada (o ya existía), False si 
    hubo un error.
    """
    try:
        # os.makedirs crea todos los directorios intermedios necesarios.
        # exist_ok=True evita un error si la carpeta ya existe.
        os.makedirs(PATH, exist_ok=True)
        print(f"✅ Carpeta '{PATH}' creada o ya existe.")
        return True
    except OSError as e:
        print(f"❌ Error al crear la carpeta '{PATH}': {e}")
        return False
    except Exception as e:
        print(f"❌ Ocurrió un error inesperado: {e}")
        return False