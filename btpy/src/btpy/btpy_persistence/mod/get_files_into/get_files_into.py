

import os

def get_files_into(PATH_FOLDER)->list[str]:
    """
    Obtiene los nombres de todos los 
    archivos dentro de una carpeta
    By Gemini
    """
    nombres_archivos = []
    try:
        # Verifica si la ruta es un 
        # directorio válido
        if not os.path.isdir(PATH_FOLDER):
            print(f"Error: La ruta '{PATH_FOLDER}' no es un directorio válido.")
            return nombres_archivos  
        # Devuelve la lista vacía

        # Obtiene la lista de archivos 
        # en la carpeta
        nombres_archivos = os.listdir(
            PATH_FOLDER)
        # Filtra solo los archivos, 
        # excluyendo subdirectorios
        nombres_archivos = [
            nombre for nombre 
            in nombres_archivos 
            if os.path.isfile(
                os.path.join(
                    PATH_FOLDER, 
                    nombre
                ))]


    except Exception as e:
        print(f"Ocurrió un error al obtener los nombres de los archivos: {e}")
        return [] #devuelve una lista vacia si hay un error.

    return nombres_archivos