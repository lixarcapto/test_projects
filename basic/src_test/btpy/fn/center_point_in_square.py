


def center_point_in_square(
    punto:list[int], 
    esquina_superior_derecha:list[int], 
    esquina_inferior_izquierda:list[int]):
  """
   Centra un punto dentro de un 
   cuadrado representado por su 
   esquina superior derecha y esquina 
   inferior izquierda. 
  Args:
      punto: Tupla (x, y) que representa las coordenadas del punto a centrar.
      esquina_superior_derecha: Tupla (x, y) que representa la esquina superior derecha del cuadrado.
      esquina_inferior_izquierda: Tupla (x, y) que representa la esquina inferior izquierda del cuadrado.

  Returns:
      Tupla (x, y) que representa las coordenadas del punto centrado dentro del cuadrado.
  """

  # Calcular el centro del cuadrado.
  centro_x = (esquina_superior_derecha[0] + esquina_inferior_izquierda[0]) // 2
  centro_y = (esquina_superior_derecha[1] + esquina_inferior_izquierda[1]) // 2

  # Calcular el desplazamiento necesario para centrar el punto.
  desplazamiento_x = centro_x - punto[0]
  desplazamiento_y = centro_y - punto[1]

  # Aplicar el desplazamiento al punto para centrarlo.
  punto_centrado = (punto[0] + desplazamiento_x, punto[1] + desplazamiento_y)

  # Ajustar las coordenadas del punto centrado para que queden dentro del cuadrado 
  # considerando enteros.
  punto_centrado_ajustado = (
      max(min(punto_centrado[0], esquina_superior_derecha[0]), esquina_inferior_izquierda[0]),
      max(min(punto_centrado[1], esquina_superior_derecha[1]), esquina_inferior_izquierda[1])
  )
  return punto_centrado_ajustado