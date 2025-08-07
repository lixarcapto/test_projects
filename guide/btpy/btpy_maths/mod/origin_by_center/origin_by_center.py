



def origin_by_center(point:list[int], 
      size_x:int, size_y:int)->list[int]:
  """
  Encuentra el punto de origen 
  (esquina superior izquierda) 
  de un rectángulo.
  """
  # Calculamos las coordenadas del 
  # origen restando la mitad de las 
  # dimensiones al centro
  x_origen = point[0] - (size_x // 2)
  y_origen = point[1] - (size_y // 2)
  return [x_origen, y_origen]