

def matrix_bool_is_connect(matriz):
  """
  Verifica si todas las celdas con valor 1 en una matriz 2D forman un único
  camino continuo por adyacencia (horizontal, vertical o diagonal).

  Argumentos:
    matriz (list): Una matriz 2D de 0s y 1s.

  Retorna:
    bool: True si todas las celdas 1 están conectadas en un solo componente,
          False en caso contrario.
  """
  filas = len(matriz)
  if filas == 0:
    return True
  columnas = len(matriz[0])

  # 1. Encontrar el punto de partida (la primera celda con 1)
  inicio = None
  total_unos = 0
  for r in range(filas):
    for c in range(columnas):
      if matriz[r][c] == 1:
        total_unos += 1
        if inicio is None:
          inicio = (r, c)

  # Si no hay 1s o solo hay uno, se considera True
  if total_unos <= 1:
    return True

  # 2. Recorrer el camino usando DFS
  visitados = set()
  pila = [inicio]

  # Movimientos en 8 direcciones (horizontal, vertical, diagonal)
  direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

  while pila:
    fila_actual, col_actual = pila.pop()
    
    if (fila_actual, col_actual) not in visitados:
      visitados.add((fila_actual, col_actual))

      for dr, dc in direcciones:
        nueva_fila, nueva_col = fila_actual + dr, col_actual + dc

        # Verificar que la celda vecina sea válida y tenga valor 1
        if (0 <= nueva_fila < filas and
            0 <= nueva_col < columnas and
            matriz[nueva_fila][nueva_col] == 1 and
            (nueva_fila, nueva_col) not in visitados):
          pila.append((nueva_fila, nueva_col))
  
  # 3. Comparar el número de celdas visitadas con el total de 1s
  return len(visitados) == total_unos