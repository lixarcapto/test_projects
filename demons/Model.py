

from Demon import Demon
from demon_dict import demon_dict
from btpy.Btpy import Btpy

class Model:

    def __init__(self):
        self.demon_key = "jacara"
        self.candle_list = []
        self.symbol_selected = 0
        self.symbol_quantity = 6

    def get_symbol_paths(self):
        list_ = []
        res = "./res/symbol/"
        format_ = ".png"
        for i in range(self.symbol_quantity):
            list_.append(
                res + "symbol_" + str(i)\
                    + format_
            )
        return list_

    def create_demon(self):
        self.demon_key = ""
        for k in demon_dict:
            if(demon_dict[k]["symbol_number"]
               == self.symbol_selected
            and demon_dict[k]["candle_list"]
               == self.candle_list):
                self.demon_key = k

    def render_dict(self)->dict:
        return {
            "NAME":self.demon_key,
            "PATH":"./res/" \
                + self.demon_key\
                    + ".png"
        }
    
import webbrowser

def abrir_url_en_navegador(url):
    """
    Abre la URL indicada en el navegador web predeterminado del sistema.

    :param url: La URL (string) que se desea abrir. Debe incluir el esquema (p. ej., 'https://').
    :return: True si el navegador se abrió exitosamente, False en caso contrario.
    """
    try:
        # webbrowser.open(url) abrirá la URL. 
        # Si quieres que siempre se abra en una nueva pestaña, puedes usar:
        # return webbrowser.open_new_tab(url)
        return webbrowser.open(url)
    except Exception as e:
        print(f"Ocurrió un error al intentar abrir la URL: {e}")
        return False


import os
import subprocess
import sys

def buscar_y_abrir_primera_imagen(directorio_base=None):
    """
    Realiza una búsqueda recursiva de la primera imagen con formato común 
    en un directorio base (por defecto, la carpeta personal del usuario) 
    y la abre con el visor predeterminado del sistema.

    :param directorio_base: La ruta donde comenzar la búsqueda. 
                            Por defecto es la carpeta personal (~).
    :return: True si se encontró y abrió una imagen, False en caso contrario.
    """
    # 1. Definir extensiones de imagen comunes
    extensiones_imagen = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.tiff')
    
    # 2. Definir el directorio base de búsqueda
    if directorio_base is None:
        # Usa la carpeta personal del usuario como punto de partida seguro
        directorio_base = os.path.expanduser('~')

    print(f"Iniciando búsqueda de imágenes desde: {directorio_base}")
    print("Esto puede tardar unos momentos, dependiendo de la cantidad de archivos.")

    # 3. Realizar la búsqueda recursiva
    imagen_encontrada = None
    
    try:
        # os.walk() genera nombres de directorios en un árbol, recorriéndolo
        for raiz, directorios, archivos in os.walk(directorio_base):
            for nombre_archivo in archivos:
                nombre, extension = os.path.splitext(nombre_archivo)
                
                # Comprobar si la extensión coincide con un formato de imagen
                if extension.lower() in extensiones_imagen:
                    imagen_encontrada = os.path.join(raiz, nombre_archivo)
                    print("-" * 50)
                    print(f"¡Imagen encontrada! 🎯")
                    print(f"Ruta: {imagen_encontrada}")
                    break  # Salir del bucle de archivos
            
            if imagen_encontrada:
                break  # Salir del bucle os.walk (detiene la búsqueda)

    except PermissionError:
        print(f"Advertencia: No se tienen permisos para acceder a la carpeta: {raiz}")
        # La búsqueda continúa, saltando esta carpeta.
    except Exception as e:
        print(f"Ocurrió un error inesperado durante la búsqueda: {e}")
        return False

    # 4. Abrir la imagen encontrada
    if imagen_encontrada:
        try:
            # Lógica para abrir el archivo según el sistema operativo
            if sys.platform == 'win32':
                os.startfile(imagen_encontrada)
            elif sys.platform == 'darwin':
                subprocess.call(['open', imagen_encontrada])
            else:
                subprocess.call(['xdg-open', imagen_encontrada])

            print("Éxito: La imagen se ha abierto con el visor predeterminado.")
            return True

        except Exception as e:
            print(f"Error al intentar abrir la imagen con el visor del sistema: {e}")
            return False
    else:
        print("-" * 50)
        print("Fallo: No se encontró ninguna imagen con formato común en el directorio base.")
        return False

