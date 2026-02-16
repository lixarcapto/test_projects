


def split_by_last_string(
    string_original:str, 
    subcadena:str)->list[str]:
  """
  Divide un string en dos partes 
  en base a la última aparición de 
  una subcadena y lo retorna como una lista.

  Args:
    string_original: El string original 
    que se dividirá.
    subcadena: La subcadena a 
    partir de la cual se dividirá el string.

  Returns:
    Una lista que contiene dos strings
    : la primera parte del string 
    original hasta la última aparición 
    de la subcadena, y la segunda parte 
    desde la última aparición de la 
    subcadena hasta el final del string.
  """
  # Busca la última aparición de la subcadena usando rfind().
  ultima_posicion = string_original.rfind(subcadena)

  # Si la subcadena no se encuentra, la segunda parte será el string original.
  if ultima_posicion == -1:
    partes = [string_original]
  else:
    # Si la subcadena se encuentra, la segunda parte es desde la última posición + la longitud de la subcadena.
    parte_posterior = string_original[ultima_posicion + len(subcadena):]
    parte_anterior = string_original[:ultima_posicion]
    partes = [parte_anterior, parte_posterior]
  return partes