

from openpyxl import Workbook

def write_xlsx_flat_list(PATH:str, 
        LIST:list)-> None:
    """
    Function that creates an xlsx file 
    with a list where each cell of 
    the table is an element of the 
    list
    """
    if(not ".xlsx" in PATH):
        PATH += ".xlsx"
    # --------------------------------
    # 1. Crear un nuevo libro de trabajo (Workbook)
    wb = Workbook()
    sheet = wb.active
    sheet.title = "Datos"

    # 2. Recorrer la lista e insertar cada elemento en una celda
    # En este caso, los pondremos en la primera fila, recorriendo las columnas
    for indice, valor in enumerate(LIST, start=1):
        # row=1 (fila 1), column=indice (columna que avanza)
        sheet.cell(row=1, column=indice, value=valor)

    # 3. Guardar el archivo
    try:
        wb.save(PATH)
        print(f"Archivo '{PATH}' creado con éxito.")
    except Exception as e:
        print(f"Hubo un error al guardar el archivo: {e}")