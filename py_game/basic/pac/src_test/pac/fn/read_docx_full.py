


from ..out_deps import Document

"""
    Funcion que carga un archivo ".docx" como texto almacenando
    sus saltos de linea y espacios.
"""
def read_docx_full(ruta_archivo:str)->str:
    documento = Document(ruta_archivo)
    texto_plano = ""
    for parrafo in documento.paragraphs:
      texto_plano += parrafo.text
      texto_plano += "\n"  
      # Salto de de linea al final de 
      # cada parrafo
    return texto_plano
