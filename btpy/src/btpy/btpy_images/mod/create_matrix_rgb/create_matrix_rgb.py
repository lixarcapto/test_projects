


def create_matrix_rgb(filas, columnas):
  """
  Crea una matriz RGB utilizando listas anidadas en Python puro.

  Args:
    filas: Número de filas de la matriz.
    columnas: Número de columnas de la matriz.

  Returns:
    Una lista de listas que representa una matriz RGB, donde cada elemento
    interno es una lista de 3 valores (R, G, B) entre 0 y 255.
  """

  matriz_rgb = []
  for _ in range(filas):
    fila = []
    for _ in range(columnas):
      pixel = [0, 0, 0]  # Inicializamos el pixel a negro
      # Aquí puedes personalizar la generación de colores
      # Por ejemplo, para colores aleatorios:
      # pixel = [random.randint(0, 255) for _ in range(3)]
      fila.append(pixel)
    matriz_rgb.append(fila)

  return matriz_rgb