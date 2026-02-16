


def remove_last_string(string_original, 
                string_a_eliminar):
  """
  Elimina la última aparición de un 
  string dentro de otro string.
  """
  # Encuentra la última posición del substring_a_eliminar dentro del string_original.
  ultima_posicion = string_original\
    .rfind(string_a_eliminar)
  # Si el substring_a_eliminar está presente, elimina la parte del string original 
  # que va desde la última posición + la longitud del substring_a_eliminar hasta el final.
  if ultima_posicion != -1:
    return string_original[:ultima_posicion]
  else:
    # Si el substring_a_eliminar no 
    # está presente, devuelve el string 
    # original sin cambios.
    return string_original