


def get_grid_index(POINT, SIZE_CELD,
        ROWS, COLUMNS):
  """
  Identifica el índice de matriz (fila, columna) de una coordenada en una cuadrícula.

  Argumentos:
    coord (tuple): Una tupla (x, y) que representa la coordenada.
    grid_data (dict): Un diccionario que contiene los datos de la cuadrícula:
                      - 'origin' (tuple): Coordenada (x, y) del origen de la cuadrícula.
                      - 'cell_size' (float): El tamaño de cada celda de la cuadrícula (lado del cuadrado).
                      - 'rows' (int): Número de filas en la cuadrícula.
                      - 'cols' (int): Número de columnas en la cuadrícula.

  Retorna:
    tuple: Una tupla (row, col) que representa el índice de la matriz.
           Si la coordenada está fuera de la cuadrícula, retorna (-1, -1).
  """
  x_coord, y_coord = POINT
  origin_x, origin_y = [0, 0]
  cell_size = SIZE_CELD
  rows = ROWS
  cols = COLUMNS

  # Calcular la fila y la columna
  row = int((y_coord - origin_y) / cell_size)
  col = int((x_coord - origin_x) / cell_size)

  # Verificar si la coordenada está dentro de los límites de la cuadrícula
  if 0 <= row < rows and 0 <= col < cols:
    return (row, col)
  else:
    return (-1, -1)