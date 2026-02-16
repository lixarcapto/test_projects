

import os

def get_files_into(PATH_FOLDER:str,
        EXTENSION:str = "")\
        ->list[str]:
    """
    Funcion que obtiene los nombres completos
    de todos los archivos dentro de una 
    carpeta con su extension. Si envia
    una extension entonces filtrara
    los nombres que tengan esa extension
    automaticamente.
    By Gemini
    """
    # VALIDATORS ------------------------
    if(not isinstance(PATH_FOLDER, str)):
        raise Exception("""
        the PATH_FOLDER argument is not 
        a string type
        """)
    if(not isinstance(EXTENSION, str)):
        raise Exception("""
        the EXTENSION argument is not 
        a string type
        """)
    # adapta el argumento PATH_FOLDER
    # en caso de no terminar en slash
    if(list(PATH_FOLDER)[0] != "/"):
        path_folder = PATH_FOLDER + "/"
    else:
        path_folder = PATH_FOLDER
    # adapta el argumento extension
    extension:str = ""
    if(not ("." in EXTENSION)):
        extension = "." + EXTENSION
    else:
        extension = EXTENSION
    # FUNCTION ---------------------------
    nombres_archivos = []
    result:list = []
    try:
        # Verifica si la ruta es un 
        # directorio válido
        if not os.path.isdir(path_folder):
            print(f"Error: La ruta '{path_folder}' no es un directorio válido.")
            return nombres_archivos  
        # Devuelve la lista vacía

        # Obtiene la lista de archivos 
        # en la carpeta
        nombres_archivos = os.listdir(
            path_folder)
        # Filtra solo los archivos, 
        # excluyendo subdirectorios
        nombres_archivos = [
            nombre for nombre 
            in nombres_archivos 
            if os.path.isfile(
                os.path.join(
                    path_folder, 
                    nombre
                ))]


    except Exception as e:
        print(f"Ocurrió un error al obtener los nombres de los archivos: {e}")
        return [] #devuelve una lista vacia si hay un error.
    if(extension == "."):
        result = nombres_archivos
    else:
        for e in nombres_archivos:
            if(extension in e):
                result.append(e)
    return result