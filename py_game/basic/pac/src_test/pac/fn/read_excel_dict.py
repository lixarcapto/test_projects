


from ..out_deps import Basic, openpyxl

"""
Reads an Excel file into a dictionary 
of arrays, using the first cell of each 
row as keys and subsequent elements as 
array elements.
ARGS:
filename (str): The path to the Excel 
file to be read.
RETURN:
dict: A dictionary where keys are the 
first cells of rows and values are lists 
of subsequent elements in those rows.
"""
def read_excel_dict(filename:str)->dict[list]:
    Basic.valid_string(filename, 1, True)
    EXTENSION = ".xlsx"
    if(not EXTENSION in filename):
        filename += EXTENSION
    try:
        # Load the Excel workbook
        wb = openpyxl.load_workbook(filename)
        sheet = wb.active
        # Initialize the dictionary to store 
        # data
        data_dict = {}
        # Iterate through rows in the Excel 
        # sheet
        for row in sheet.iter_rows(min_row=2):  # Skip header row (row 1)
            key = row[0].value  # Get the 
            # first cell value as the key
            data_list = [cell.value for cell in row[1:]]  # Get subsequent cell values as the array
            # Add the key-value pair to 
            # the dictionary
            data_dict[key] = data_list
        return data_dict
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return {}
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return {}