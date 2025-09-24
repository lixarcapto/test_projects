
def reset_energy(matriz):
  """
  Cambia todas las celdas con el valor 2 a 1 en una matriz 2D.

  Argumentos:
    matriz (list): Una matriz 2D de números.

  Retorna:
    list: La matriz modificada.
  """
  # Crear una copia de la matriz para no modificar la original directamente
  matriz_modificada = [fila[:] for fila in matriz]

  # Recorrer cada celda y cambiar el valor si es 2
  for i in range(len(matriz_modificada)):
    for j in range(len(matriz_modificada[0])):
      if matriz_modificada[i][j] == 2:
        matriz_modificada[i][j] = 1
  
  return matriz_modificada

def distribuite_energy(matriz):
  """
  Modifica una matriz 2D: las celdas con valor 1 conectadas a [0, 0] se cambian a 2,
  y las celdas con valor 2 que no están conectadas se cambian a 1.

  Argumentos:
    matriz (list): Una matriz 2D de números.

  Retorna:
    list: Una nueva matriz modificada.
  """
  if not matriz or not matriz[0]:
    return []

  filas = len(matriz)
  columnas = len(matriz[0])
  
  # Inicializar la nueva matriz con los valores de la matriz original
  nueva_matriz = [fila[:] for fila in matriz]

  pila = []
  visitados = set()
  
  # Si la celda de inicio [0, 0] es 1, la añadimos a la pila para empezar
  if matriz[0][0] == 1:
      pila.append((0, 0))
  else:
      # Si la celda [0,0] no es 1, no hay conectividad para el recorrido
      # Se recorre la matriz y los valores 2 se cambian a 1
      for r in range(filas):
          for c in range(columnas):
              if nueva_matriz[r][c] == 2:
                  nueva_matriz[r][c] = 1
      return nueva_matriz

  # Movimientos en 8 direcciones (horizontal, vertical, diagonal)
  direcciones = [
      (0, 1), (0, -1),
      (1, 0), (-1, 0),
      (1, 1), (1, -1),
      (-1, 1), (-1, -1)
  ]

  # Primer recorrido (DFS) para encontrar celdas conectadas a [0, 0]
  while pila:
    fila, columna = pila.pop()
    
    if (fila, columna) not in visitados:
      visitados.add((fila, columna))
      
      # Explorar vecinos
      for dr, dc in direcciones:
        nueva_fila, nueva_columna = fila + dr, columna + dc

        # Verificar que el vecino sea válido y tenga valor 1 en la matriz original
        if (0 <= nueva_fila < filas and
            0 <= nueva_columna < columnas and
            matriz[nueva_fila][nueva_columna] == 1 and
            (nueva_fila, nueva_columna) not in visitados):
          pila.append((nueva_fila, nueva_columna))

  # Segundo recorrido para modificar la matriz según los nodos visitados
  for r in range(filas):
      for c in range(columnas):
          if (r, c) in visitados and matriz[r][c] == 1:
              nueva_matriz[r][c] = 2
          elif (r,c) not in visitados and matriz[r][c] == 2:
              nueva_matriz[r][c] = 1

  return nueva_matriz