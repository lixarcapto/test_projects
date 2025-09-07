

"""
    Elimina las mayúsculas y tildes de un texto.
"""
# return text
def remove_capitals_and_accents(texto):
    texto_sin_mayusculas = texto.lower()
    tabla_tildes = {
      "á": "a",
      "é": "e",
      "í": "i",
      "ó": "o",
      "ú": "u",
    }
    for caracter in texto_sin_mayusculas:
      if caracter in tabla_tildes:
        texto_sin_mayusculas = texto_sin_mayusculas.replace(caracter, tabla_tildes[caracter])
    return texto_sin_mayusculas
