


from docx import Document


def read_docx(ruta_archivo:str)->str:
    """
    Funcion que carga un archivo 
    ".docx" como texto almacenando
    sus saltos de linea y espacios.
    """
    documento = Document(ruta_archivo)
    texto_plano = ""
    for parrafo in documento.paragraphs:
      texto_plano += parrafo.text
      texto_plano += "\n"  
      # Salto de de linea al final de 
      # cada parrafo
    return texto_plano
