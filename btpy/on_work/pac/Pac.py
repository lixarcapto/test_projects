

from .in_deps import*
from btpy.Btpy import Btpy

class Pac:

    """
    Abreviación de acceso a la persistencia; 
    es un módulo que facilita funcionalidades
    relacionadas al acceso a la persistencia,
    como lectura de archivos y navegación.
    """

    CACHE_NAMES_DICT = {}
    ROUTE_NAME_MALE_XLSX = "pac/res/name_male_data.xlsx"
    ROUTE_NAME_FEMALE_XLSX = "pac/res/name_female_data.xlsx"

    def __init__(self) -> None:
        pass

    def clear_txt(file_path:str)->None:
        clear_txt(file_path)

    def execute(script_path:str)->None:
        execute(script_path)
    
    def read_txt(file_path:str)->str:
        return read_txt(file_path)

    def write_txt(file_path:str, text:str)\
        ->None:
        write_txt(file_path, text)

    def create_txt(filename:str, 
        content:str="")->None:
        return create_txt(filename, content)
    
    def delete_txt(filename:str)->None:
        delete_txt(filename)

    # return PhotoImage
    def read_photoimage(ruta_imagen:str):
        return read_photoimage(ruta_imagen)
    
    def read_excel_dict(filename:str)\
            ->dict[list]:
        return read_excel_dict(filename)
    
    def read_xlsx_nested(filename:str)\
            ->dict[dict]:
        return read_xlsx_nested(filename)
    
    def read_docx_full(ruta_archivo:str)->str:
        return read_docx_full(ruta_archivo)
    
    def create_docx(route:str, text:str)->None:
        return create_docx(route, text)
    
    def create_excel_dict(data:dict[list], 
        filename:str)->None:
        return create_excel_dict(data, 
                filename)
    
    def save_numpy_image_RGB_as_PNG(
        numpy_image_RGB, name:str)->None:
        save_numpy_image_RGB_as_PNG(
            numpy_image_RGB, name)
        
    def play_sound(route:str)->None:
        return play_sound(route)
    
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
        # adapta los params
        gender = Btpy.random_choice(
            ["male", "female"])
        # carga un cache con los nombres
        name = ""
        names_list = []
        if(Pac.CACHE_NAMES_DICT == {}):
            male_dict = Pac.read_excel_dict(
                Pac.ROUTE_NAME_MALE_XLSX)
            female_dict = Pac.read_excel_dict(
                Pac.ROUTE_NAME_FEMALE_XLSX)
        names_dict = None
        if(gender == "male"):
            names_dict = male_dict
        elif(gender == "female"):
            names_dict = female_dict
        # adapta la clave cultura faltante
        if(culture == ""):
            names_list = Btpy.random_choice(
                names_dict)
        else:
            names_list = names_dict[culture]
        # genera nombre aleatorio
        name =  Btpy.random_choice(names_list)
        return name
        
        

    


    