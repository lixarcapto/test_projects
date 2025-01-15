

from btpy_lib.btpy.src.btpy.Btpy import Btpy
import os

def leer_archivos_js(directorio):
    """
    Lee todos los archivos .js en un directorio y sus subdirectorios, y devuelve una lista con el contenido de cada archivo.

    Args:
        directorio (str): Ruta al directorio inicial.

    Returns:
        list: Lista de cadenas, donde cada cadena es el contenido de un archivo .js.
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

"""
Funcion que elimina las lineas de 
import from y export de cada texto
en el array enviado. Solo funciona si 
estan bien escritos.
"""
def process_array(array):
    for i in range(len(array)):
        while("import" in array[i]
        or "export" in array[i]):
            array[i] = remove_text(array[i])
    return array

def remove_text(text):
    r = Btpy.remove_between(text,
            "import", "}")
    r = Btpy.remove_between(r,
            "from \"", "\";")
    r = r\
        .replace("export ", "")
    return r

def crear_archivo_html( 
        text):
    """
    Crea un archivo HTML con el contenido especificado.

    Args:
    nombre_archivo: Nombre del archivo HTML a crear (incluyendo la extensión .html).
    contenido_html: Cadena de texto con el código HTML a escribir en el archivo.
    """
    nombre_archivo = "index.html"
    html_1 = """
    <!DOCTYPE html>
    <html>
    <head>
    <title>compiled javascript</title>
    </head>
    <body>
    <script>
    """
    html_2 = """
        </script>
        </body>
        </html>
    """
    final_html = html_1 + text + html_2
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(final_html)

def start_console():
    user_input = ""
    while(True):
        user_input = input("write path")
        if(user_input == ""):
            break
        compile_file(user_input)
        Btpy.clean_console()

def compile_file(path):
    array = leer_archivos_js(path)
    array = process_array(array)
    text = ""
    for e in array:
        text += e
    crear_archivo_html(text)
 
if __name__ == "__main__":
    start_console()


