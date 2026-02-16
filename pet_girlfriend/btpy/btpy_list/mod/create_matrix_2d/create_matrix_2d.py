


def create_matriz_2d(
    ROWS, COLUMNS, 
    VALUE=None)->list[list]:
  """
  Genera una matriz 2D (lista de listas) 
  con el tamaño especificado.
  """
  matriz = [[VALUE for _ in range(COLUMNS)] for _ in range(ROWS)]
  return matriz