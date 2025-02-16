



def crear_archivo_html( 
        path, text):
    """
    Crea un archivo HTML con el contenido especificado.

    Args:
    nombre_archivo: Nombre del archivo HTML a crear (incluyendo la extensión .html).
    contenido_html: Cadena de texto con el código HTML a escribir en el archivo.
    """
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
    print("esto recibe el open", path)
    with open(path, 'w') as archivo:
        archivo.write(final_html)