

import os


def write_txt(PATH:str, TEXT:str = "")\
        ->bool:
    """
    Escribe el texto proporcionado en 
    un archivo de texto en la ruta 
    especificada.
    Si el archivo ya existe, lo 
    sobreescribe.
    Returns:bool: True si el archivo se 
    escribió correctamente, False si 
    hubo un error.
    """
    try:
        # 'w' modo:  Abre el archivo para escritura.  Si el archivo existe, lo trunca (lo deja en cero).
        with open(PATH, 'w', encoding='utf-8') as archivo:
            archivo.write(TEXT)
        return True
    except Exception as e:
        print(f"Error al escribir en el archivo: {e}")  # Imprime el error
        return False
