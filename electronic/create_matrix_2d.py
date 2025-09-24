


def create_matriz_2d(
    filas, columnas, 
    valor_inicial=None):
  """
  Genera una matriz 2D (lista de listas) con el tamaño especificado.

  Argumentos:
    filas (int): El número de filas que tendrá la matriz.
    columnas (int): El número de columnas que tendrá la matriz.
    valor_inicial (any, opcional): El valor con el que se inicializarán todas las celdas. 
                                 Por defecto es None.

  Retorna:
    list: Una matriz 2D (lista anidada) del tamaño dado, inicializada con el 
          valor_inicial.
  """
  matriz = [[valor_inicial for _ in range(columnas)] for _ in range(filas)]
  return matriz