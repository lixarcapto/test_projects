


import os
import networkx as nx

def read_js_folder(directorio):
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