

from ..dependences import docx
from ..dependences import os

"""
    Funcion que almacena en un archivo docx el texto
    enviado.
"""
# not return
def save_text_inside_a_word_file(route, text):
    format = ".docx"
    if(not format in route):
        route += format
    document = docx.Document()
    paragraph = document.add_paragraph(text)
    # Set paragraph style (optional)
    paragraph.style = "Normal"
    # Add additional formatting or elements as needed
    document.save(route + ".docx")
