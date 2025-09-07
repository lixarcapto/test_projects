

from ..dependences import openpyxl

"""
    Funcion que carga un archivo excel usando una ruta
    indicada como una matriz 2D de texto
"""
# return matrix2D_string
def load_excel_file_as_array(route):
     # Importa las librerías necesarias
     # Abre el archivo Excel
     libro = openpyxl.load_workbook(route)
     # Obtiene la hoja activa
     hoja = libro.active
     # Crea una lista para almacenar los datos
     matriz = []
     # Recorre las filas de la hoja
     for fila in hoja.iter_rows():
       # Crea una lista para almacenar los datos de la fila
       fila_datos = []
       # Recorre las celdas de la fila
       for celda in fila:
         # Agrega el valor de la celda a la lista
         fila_datos.append(celda.value)
       # Agrega la lista de datos de la fila a la matriz
       matriz.append(fila_datos)
     # Retorna la matriz
     return matriz
