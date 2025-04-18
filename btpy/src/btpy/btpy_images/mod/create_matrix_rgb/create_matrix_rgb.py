


def create_matrix_rgb(filas, columnas):
  """
  Crea una matriz RGB utilizando listas 
  anidadas en Python puro.
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