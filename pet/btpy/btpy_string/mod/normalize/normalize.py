


TILDE_TABLE = {
      "á": "a",
      "é": "e",
      "í": "i",
      "ó": "o",
      "ú": "u"
    }

def normalize(text: str) -> str:
    """
    Funcion que elimina las mayúsculas, 
    espacios extra y tildes de un texto.
    """
    global TILDE_TABLE
    #
    lower_text = text.lower().strip()
    for char in lower_text:
      if char in TILDE_TABLE:
        lower_text = lower_text.replace(
             char, 
             TILDE_TABLE[char]
        )
    return lower_text