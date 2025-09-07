

from ..dependences import docx

"""
    Funcion que lee un documento .docx en la ruta
    enviada; y retorna el texto del documento.
"""
# return string
def load_a_docx_file_as_text(route):
    """
    Convierte un documento DOCX a texto.
    Args:
      ruta_archivo: La ruta del archivo DOCX a convertir.
    Returns:
      El texto del documento DOCX.
    """
    documento = docx.Document(ruta_archivo)
    parrafos = []
    for parrafo in documento.paragraphs:
      parrafos.append(parrafo.text)
    return " ".join(parrafos)
