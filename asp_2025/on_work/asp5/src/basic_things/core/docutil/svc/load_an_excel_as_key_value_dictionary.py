


from ..dependences import openpyxl

"""
    Funcion que carga un archivo excel como un diccionario
    de textos string en par clave-valor.
    FIXME: Ignora la primera fila de la tabla.
"""
# return string_map
def load_an_excel_as_key_value_dictionary(ruta_archivo):
    # Abrir el archivo Excel
    libro = openpyxl.load_workbook(ruta_archivo)
    # Obtener la hoja de cálculo activa
    hoja = libro.active
    # Crear un diccionario para almacenar los datos
    diccionario = {}
    # Recorrer las filas de la hoja de cálculo
    for fila in hoja.iter_rows(min_row=2):
      # Obtener la clave y el valor de la fila
      clave = fila[0].value
      valor = fila[1].value
      # Agregar la clave y el valor al diccionario
      diccionario[clave] = valor
    # Devolver el diccionario
    return diccionario
