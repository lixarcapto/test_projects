


def translade_points(lista_puntos, 
    origen_x, origen_y, ancho, alto):
  """
  Traslada una lista de puntos a 
  un nuevo espacio rectangular.
  """
  lista_puntos_trasladada = []
  for punto in lista_puntos:
    x, y = punto
    # Trasladamos el punto restando 
    # las coordenadas del origen
    x_nuevo = x - origen_x
    y_nuevo = y - origen_y
    lista_puntos_trasladada.append(
        (x_nuevo, y_nuevo))
  return lista_puntos_trasladada

def translade_points_old(lista_puntos, 
    origen_x, origen_y, ancho, alto):
  """
  Traslada una lista de puntos a un nuevo espacio rectangular.

  Args:
    lista_puntos: Una lista de tuplas (x, y) representando los puntos.
    origen_x: Coordenada x del punto de origen del nuevo espacio.
    origen_y: Coordenada y del punto de origen del nuevo espacio.
    ancho: Ancho del nuevo espacio.
    alto: Alto del nuevo espacio.

  Returns:
    Una nueva lista de tuplas (x_nuevo, y_nuevo) representando los puntos trasladados.
  """

  lista_puntos_trasladada = []
  for punto in lista_puntos:
    x, y = punto
    # Verificamos si el punto está dentro del nuevo espacio
    if origen_x <= x < origen_x + ancho and origen_y <= y < origen_y + alto:
      # Trasladamos el punto restando las coordenadas del origen
      x_nuevo = x - origen_x
      y_nuevo = y - origen_y
      lista_puntos_trasladada.append((x_nuevo, y_nuevo))
    else:
      print("El punto", punto, "está fuera del nuevo espacio.")
  return lista_puntos_trasladada