

from ..dependences import Workbook

"""
    Funcion que almacena en un archivo Word los datos
    de un diccionario de arrays de string; usando la clave
    del diccionario como primer elemento de cada fila; y
    suma los elementos del array a la fila de clave.
"""
# Not return
def save_a_dictionary_of_string_arrays_in_an_excel(\
        diccionario,
        nombre_archivo
        ):
    """
    Convierte un diccionario de arrays de texto en un
    documento Excel de una hoja con las claves del
    diccionario como primera celda de cada lista y
    sus elementos en celdas separadas.
    Args:
      diccionario: Un diccionario donde las claves
      son strings y los valores son arrays de strings.
      nombre_archivo: El nombre del archivo Excel que
      se creará.
    Returns:
      None.
    """
    # Crear un nuevo libro de Excel
    wb = Workbook()
    # Crear una hoja de trabajo
    hoja = wb.active
    # Escribir las claves del diccionario como encabezados
    for i, clave in enumerate(diccionario.keys(), start=1):
      hoja.cell(row=1, column=i).value = clave
    # Obtener la fila máxima
    fila_max = max(len(valores) for valores in diccionario.values()) + 1
    # Escribir los valores de los arrays en la hoja
    for i, (clave, valores) in enumerate(diccionario.items(), start=2):
      # Escribir la clave en la primera celda de la fila
      hoja.cell(row=i, column=1).value = clave
      # Escribir los elementos del array en las siguientes celdas
      for j, valor in enumerate(valores, start=2):
        hoja.cell(row=i, column=j).value = valor
    """
    # Ajustar el ancho de las columnas
    for columna in hoja.columns:
      columna.auto_width = True
    """
    # Guardar el libro de Excel
    wb.save(nombre_archivo)
