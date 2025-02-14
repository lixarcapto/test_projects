



def point_in_space(punto:list[int], 
                   rango_x:list[int], 
                   rango_y:list[int])\
                    ->bool:
  """
  Analiza y verifica si un punto 
  en forma de lista se encuentra 
  dentro de los intervalos de los 
  ejes enviados en x e y.
  """
  # Desempaquetear las coordenadas del punto y los intervalos de los ejes.
  punto_x, punto_y = punto
  rango_x_min, rango_x_max = rango_x
  rango_y_min, rango_y_max = rango_y

  # Verificar si las coordenadas del punto están dentro de los intervalos de los ejes.
  esta_dentro_x = rango_x_min <= punto_x <= rango_x_max
  esta_dentro_y = rango_y_min <= punto_y <= rango_y_max

  # Si el punto está dentro de ambos intervalos, devolver True. En caso contrario, devolver False.
  if esta_dentro_x and esta_dentro_y:
    return True
  else:
    return False