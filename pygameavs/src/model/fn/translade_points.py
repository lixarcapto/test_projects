


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