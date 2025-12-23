


def get_grid_index(POINT, SIZE_CELD,
        ROWS, COLUMNS)->list[int]:
  """
  Identifica el índice de matriz 
  (fila, columna) de una coordenada 
  en una cuadrícula.
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