


import docx

# return map_of_map
def read_docx_with_titles(\
        ROUTE:str)->dict:
    """
    Función que lee un archivo Word, busca 
    letras cursivas negritas y almacena 
    el texto siguiente en un diccionario,
    ignorando las negritas no cursivas.
    Retorna un diccionario donde las 
    claves son las líneas de texto con 
    letras cursivas negritas y los 
    valores son el texto siguiente hasta 
    la siguiente letra cursiva negrita, 
    ignorando las negritas no cursivas.
    """
    documento = docx.Document(ROUTE)
    diccionario = {}
    clave_actual = None
    for parrafo in documento.paragraphs:
      for corrida in parrafo.runs:
        # **Formato Word para is_bold e is_italic:**
        if corrida.font.bold and corrida.font.italic:  # Letra cursiva negrita
          clave_actual = corrida.text
          diccionario[clave_actual] = ""
        elif corrida.font.bold:  # Negrita no cursiva
          continue
        else:  # Texto normal o cursiva no negrita
          diccionario[clave_actual] += corrida.text
    return diccionario
