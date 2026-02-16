


import random

def random_str(SIZE:int, 
    STRING:str)->str:
  """
  Genera un texto aleatorio de la 
  longitud especificada utilizando 
  los caracteres proporcionados.
  """
  text = ""
  for _ in range(SIZE):
    text += random.choice(list(STRING))
  return text