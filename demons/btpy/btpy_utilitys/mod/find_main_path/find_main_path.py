



import os

def find_main_path() -> str:
    """
    Retorna la ruta completa del 
    directorio donde se está 
    ejecutando el script.
    """
    # os.getcwd() significa "Get Current Working Directory"
    ruta_actual = os.getcwd()
    return ruta_actual