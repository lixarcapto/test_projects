

from ..dependences import openpyxl

"""
    funcion que cargue un archivo excel y lo convierta
    en un diccionario de arrays usando el primer
    elemento de cada fila como clave; e ignorando
    el primer elemento de cada fila; pero cargando
    todos los demas elementos de la fila en cada array.
    FIXME: Por alguna razon ignora la primera fila.
"""
# return string_array_dictionary
def load_an_excel_file_as_a_string_array_dictionary(\
        ruta_archivo):
    # Abrir el archivo Excel
    try:
      libro = openpyxl.load_workbook(ruta_archivo)
    except IOError:
      raise IOError("No se pudo abrir el archivo Excel")
    # Obtener la hoja de trabajo activa
    hoja = libro.active
    # Diccionario para almacenar los datos
    diccionario_arrays = {}
    # Recorrer las filas de la hoja de trabajo
    for fila in range(2, hoja.max_row + 1):
      # Obtener el valor de la primera columna
      clave = hoja.cell(row=fila, column=1).value
      # Si la clave no está vacía, agregarla al diccionario
      if clave:
        diccionario_arrays[clave] = []
        # Recorrer las demás columnas
        for columna in range(2, hoja.max_column + 1):
          # Obtener el valor de la celda
          valor = hoja.cell(row=fila, column=columna).value
          # Si el valor no está vacío, agregarlo al array
          if valor:
            diccionario_arrays[clave].append(valor)
    return diccionario_arrays
