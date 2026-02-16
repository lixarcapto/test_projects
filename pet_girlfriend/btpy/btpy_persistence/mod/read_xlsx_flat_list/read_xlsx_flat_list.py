



import openpyxl

def read_xlsx_flat_list(PATH_XLSX:str)\
        ->list[str]:
    """
    Lee un archivo Excel y retorna 
    una lista (array unidimensional) 
    con todos los elementos de todas 
    las columnas.
    """

    workbook = openpyxl.load_workbook(PATH_XLSX)
    sheet = workbook.active  # Seleccionamos la hoja activa por defecto

    array:list = []
    for row in sheet.iter_rows():
        for cell in row:
            array.append(cell.value)
    array = [e for e in array if not e== None]
    return array
