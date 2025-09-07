



"""
    Funcion que genera una cantidad indicada de numeros
    aleatorios en un rango; y retorna un array.
"""
# return int_array
def random_numbers_array_in_range(quantity, minimum, maximum):
    """
    Genera una cantidad de números aleatorios no repetidos en un rango de números determinados.
    Parámetros:
      cantidad (int): La cantidad de números aleatorios a generar.
      rango_minimo (int): El valor mínimo del rango de números.
      rango_maximo (int): El valor máximo del rango de números.

    Devuelve:
      Una lista con los números aleatorios generados.
    """
    # Validar los parámetros
    if not isinstance(quantity, int) or quantity <= 0:
      raise ValueError("La cantidad debe ser un número entero positivo")
    if not isinstance(minimum, int):
      raise ValueError("El rango mínimo debe ser un número entero")
    if not isinstance(maximum, int):
      raise ValueError("El rango máximo debe ser un número entero")
    if minimum >= maximum:
      raise ValueError("El rango mínimo debe ser menor que el rango máximo")
    # Generar una lista con todos los números del rango
    numeros_posibles = list(range(minimum, maximum + 1))
    # Barajar la lista para obtener números aleatorios
    random.shuffle(numeros_posibles)
    # Seleccionar la cantidad de números aleatorios necesarios
    numeros_aleatorios = numeros_posibles[:cantidad]
    return numeros_aleatorios
