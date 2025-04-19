


import openpyxl


def read_xlsx_dict_list(PATH_XLSX:str)\
        ->dict[list]:
    """
    Reads an Excel file into a dictionary 
    of arrays, using the first cell of 
    each row as keys and subsequent 
    elements as array elements.
    Return a dictionary where keys are the 
    first cells of rows and values are 
    lists of subsequent elements in 
    those rows.
    """
    EXTENSION = ".xlsx"
    if(not EXTENSION in PATH_XLSX):
        filename += EXTENSION
    try:
        return __read_excel_dict(PATH_XLSX)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return {}
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return {}
    
def __read_excel_dict(ROUTE):
    # Load the Excel workbook
    WB = openpyxl.load_workbook(ROUTE)
    SHEET = WB.active
    data_dict = {}
    # Iterate through rows in the Excel 
    # sheet
    key = ""
    data_list = []
    for row in SHEET.iter_rows(min_row=1):  # Skip header row (row 1)
        key = row[0].value
        data_list = __get_celds(row)
        data_dict[key] = data_list
    data_dict = __clean_none(data_dict)
    return data_dict

def __clean_none(DATA_DICT):
    result_dict = {}
    for k in DATA_DICT:
        result_dict[k] = list(filter(
            lambda e:e!=None, 
            DATA_DICT[k]
        ))
    return result_dict

def __get_celds(ROW:list)->list:
    return [cell.value for cell in ROW[1:]]