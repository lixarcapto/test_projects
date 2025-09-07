

from ..dependences import Document

"""
    Funcion que carga un archivo ".docx" como texto almacenando
    sus saltos de linea y espacios.
"""
# return text
def load_a_docx_file_as_text_with_line_breaks(ruta_archivo):
    documento = Document(ruta_archivo)
    texto_plano = ""
    for parrafo in documento.paragraphs:
      texto_plano += parrafo.text
      texto_plano += "\n"  # Salto de línea al final de cada párrafo
    return texto_plano
