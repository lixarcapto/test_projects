



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