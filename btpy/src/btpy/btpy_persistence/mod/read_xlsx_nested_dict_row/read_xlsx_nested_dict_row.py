




import openpyxl


def read_xlsx_nested_dict_row(
        PATH_XLSX:str)\
        ->dict[dict]:
    """
    Reads an Excel file into a dictionary 
    of dictionaries, using the first 
    element of each row as the key for 
    each dictionary and subsequent 
    elements as dictionary values 
    with keys corresponding to row 
    names and cell values as their 
    elements.
    """
    EXTENSION = ".xlsx"
    if(not EXTENSION in PATH_XLSX):
        PATH_XLSX += EXTENSION
    try:
        # Load the Excel workbook
        wb = openpyxl.load_workbook(PATH_XLSX)
        sheet = wb.active
        # Initialize the data dictionary
        data_dict = {}
        # Get the header row (row 1)
        header_row = sheet[1]
        # Iterate through rows in the Excel 
        # sheet (skip header)
        for row in sheet.iter_rows(min_row=2):
            key = row[0].value  
            # Get the first cell value as 
            # the key
            # Initialize a dictionary for 
            # the current row
            row_dict = {}  
            # Skip the first cell (key) 
            # since it's already used as 
            # the dictionary key
            row_cells = row[1:]
            # Iterate through header cells 
            # and corresponding row cells 
            # (excluding first cell)
            for header_cell, row_cell in zip(header_row[1:], row_cells):
                row_name = header_cell.value  
                # Get the header cell value 
                # (row name)
                cell_value = row_cell.value  
                # Get the corresponding row 
                # cell value
                # Add the key-value pair to 
                # the row dictionary
                row_dict[row_name] = cell_value
            # Add the row dictionary to the 
            # data dictionary under the key
            data_dict[key] = row_dict
        return data_dict
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return {}
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return {}