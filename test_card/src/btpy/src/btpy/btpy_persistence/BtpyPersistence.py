

from .in_deps import*
from ..btpy_maths.BtpyMaths import BtpyMaths

class BtpyPersistence(BtpyMaths):

    # Check if the file exists using 
    # os.path.exists()
    def check_path(route:str, extension:str):
        return check_path(route, extension)
    
    def image_size(image_route:str)->dict:
        return image_size(image_route)
    
    def execute(script_path:str)->None:
        """
        Executes the given Python script.
        """
        return execute(script_path)
    
    def play_sound(route:str)->None:
        return play_sound(route)
    
    def delete_txt(filename:str)->None:
        """
        Deletes the specified text file.
        @ by Gemini
        """
        delete_txt(filename)

    def write_txt(file_path:str, text:str)->None:
        """
        Assigns the given text to the 
        specified text file.
        """
        write_txt(file_path, text)

    def read_txt(file_path:str)->str:
        """
        Loads the entire text from 
        a text file as a string.
        """
        return read_txt(file_path)
    
    def create_txt(filename:str, 
        content:str="")->None:
        """
        Creates a new text file with 
        the specified filename and 
        optional content.
        """
        return create_txt(filename, content)
    
    def read_excel_dict(filename:str)\
            ->dict[list]:
        """
        Reads an Excel file into a dictionary 
        of arrays, using the first cell of 
        each row as keys and subsequent 
        elements as array elements.
        ARGS:
        filename (str): The path to the Excel 
        file to be read.
        RETURN:
        dict: A dictionary where keys are the 
        first cells of rows and values are 
        lists of subsequent elements in 
        those rows.
        """
        return read_excel_dict(filename)
    
    def read_nested_row_xlsx(filename:str)\
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
        return read_nested_row_xlsx(filename)
    
    def random_name(gender = "", 
            culture = ""):
        """
        Función que genera un nombre 
        aleatorio según la cultura y el 
        género especificado.
        culture_keys = ["russian", "american", 
        "english", 
        "arab", "french", "afrikan", 
        "nordic", "indian", "spanish", 
        "turkish", "chinese", "japanese", 
        "polinesian", "italic"]
        """
        return random_name(gender, culture)
    
    def random_lastname(culture = ""):
        """
        Función que genera un nombre 
        aleatorio según la cultura y el 
        género especificado.
        culture_keys = ["russian", "american", 
        "english", 
        "arab", "french", "afrikan", 
        "nordic", "indian", "spanish", 
        "turkish", "chinese", "japanese", 
        "polinesian", "italic"]
        """
        return random_lastname(culture)
    
    def random_full_name(gender, culture):
        return random_full_name(gender, 
            culture)
    
    def create_dict_list_xlsx(data:dict[list], 
        filename:str)->None:
        """
        Stores a dictionary of arrays in an 
        Excel file.
        """
        return create_dict_list_xlsx(data, 
            filename)
    
    def create_docx(route:str, text:str)\
            ->None:
        """
        Funcion que almacena en un archivo 
        docx el texto
        enviado.
        """
        create_docx(route, text)
    
    def read_docx_full(ruta_archivo:str)->str:
        """
        Funcion que carga un archivo 
        ".docx" como texto almacenando
        sus saltos de linea y espacios.
        """
        return read_docx_full(ruta_archivo)
    
    def read_photoimage(route:str, size_x, 
        size_y)->PhotoImage:
        """
        Funcion que lee una imagen en la 
        direccion indicada y la carga como 
        un objeto PhotoImage de PIL
        """
        return read_photoimage(route, size_x, 
            size_y)
    
    def random_country(region_key:str = "")\
            ->str:
        """
         Función que generan nombres de 
        países aleatorios en ingles según 
        el continente indicado
        """
        return random_country(region_key)
    
    def read_nested_column_xlsx(
            ROUTE:str)->dict:
        """
        función de persistencia que lee un 
        archivo Excel como un diccionario 
        anidado en horizontal
        """
        return read_nested_column_xlsx(ROUTE)
    
    def load_word(DOCX_ROUTE:str)->None:
        """
        Función que obtiene la ruta 
        absoluta de un documento docx para  
        ejecutarlo en el programa Word 
        en windows.
        """
        return load_word(DOCX_ROUTE)
    
    def seek_docx_file(ROUTE = "/")->str:
        """
        Abre un cuadro de diálogo para 
        seleccionar un archivo .docx y 
        devuelve la ruta.
        """
        return seek_docx_file(ROUTE)
    
    def seek_folder_route(ROUTE = "/")->str:
        """
        Abre un cuadro de diálogo para 
        seleccionar una carpeta.
        """
        return seek_folder_route(ROUTE)
    
    def read_excel_as_key_value(PATH, 
        sheet_name=None):
        """
        Función que lee todos los pares 
        clave valor que se encuentren en un 
        archivo Excel como un diccionario.   
        leerá cada primera celda de la fila 
        video de la segunda celda como un 
        par clave valor y así sucesivamente 
        con todas las celdas.
        """
        return read_excel_as_key_value(PATH)