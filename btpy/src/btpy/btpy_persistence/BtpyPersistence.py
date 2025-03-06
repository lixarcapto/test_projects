

from .in_deps import*
from ..btpy_maths.BtpyMaths import BtpyMaths

class BtpyPersistence(BtpyMaths):

    NAME_FEMALE_PATH = "./btpy/res/name_female_data.xlsx"
    NAME_MALE_PATH = "./btpy/res/name_male_data.xlsx"
    LASTNAMES_PATH = "./btpy/res/lastname_data.xlsx"
    WORLD_MAP_PATH = "./btpy/res/map_world.json"
    PROFESSION_PATH = "./btpy/res/profession_data.xlsx"
    GeoAdress = GeoAdress
    CharacterProfile = CharacterProfile
    REGIONS_DICT_PATH:str \
        = "./btpy/res/regions_by_country.xlsx"
    REGIONS_DICT:dict = {}
    COUNTRY_DICT_PATH:str \
        = "./btpy/res/country_dict.xlsx"
    COUNTRY_DICT:dict = {}
    COUNTRY_PROPERTIES_PATH \
        = "./btpy/res/culture_properties.json"
    COUNTRY_PROPERTIES:dict = {}

    def set_name_male_path(PATH):
        """
        Modifica la ruta a la tabla
        XLSX de nombres masculinos.
        """
        BtpyPersistence.NAME_MALE_PATH \
            = PATH
        
    def set_name_female_path(PATH):
        """
        Modifica la ruta a la tabla
        XLSX de nombres femeninos.
        """
        BtpyPersistence.NAME_FEMALE_PATH \
            = PATH
        
    def set_lastname_path(PATH):
        """
        Modifica la ruta a la tabla
        XLSX de apellidos.
        """
        BtpyPersistence.LASTNAMES_PATH \
            = PATH
        
    def set_world_map_path(PATH):
        """
        Modifica la ruta a la tabla
        XLSX de apellidos.
        """
        BtpyPersistence.WORLD_MAP_PATH \
            = PATH
        
    def set_region_dict_path(PATH:str):
        BtpyPersistence.REGIONS_DICT_PATH \
            = PATH
        
    def set_country_dict_path(PATH:str):
        BtpyPersistence.COUNTRY_DICT_PATH \
            = PATH
        
    def set_profession_path(PATH):
        BtpyPersistence.PROFESSION_PATH \
            = PATH

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
    
    def random_name(culture = "",
                    gender = "")->str:
        """
        Función que genera un nombre 
        aleatorio según la cultura y el 
        género especificado. 
        Los generos son:
        * "female"
        * "male"

        Las culturas son:
        * "russian" 
        * "american" 
        * "english"
        * "arab"
        * "french"
        * "afrikan"
        * "nordic"
        * "indian"
        * "spanish"
        * "turkish"
        * "chinese"
        * "japanese"
        * "polinesian"
        * "italic"
        * "slavic"
        """
        return random_name(
            read_excel_dict,
            BtpyPersistence.NAME_MALE_PATH,
            BtpyPersistence.NAME_FEMALE_PATH,
            culture,
            gender
        )
    
    def random_lastname(
            CULTURE : str = "")-> str:
        """
        Función que genera un apellido
        aleatorio segun la cultura
        determinada.
        Las culturas son:
        * "russian" 
        * "american" 
        * "english"
        * "arab"
        * "french"
        * "afrikan"
        * "nordic"
        * "indian"
        * "spanish"
        * "turkish"
        * "chinese"
        * "japanese"
        * "polinesian"
        * "italic"
        * "slavic"
        """
        return random_lastname(
          read_excel_dict,
          BtpyPersistence.LASTNAMES_PATH,
          CULTURE
        )

    def get_region_dict()->dict:
        return BtpyPersistence\
            .REGIONS_DICT
    
    def random_full_name(
                names_number:int,
                lastnames_number:int,
                culture = "", 
                gender = ""):
        """
        Crea un nombre aleatorio en el
        formato latino; es decir con dos
        nombres y dos apellidos.
        Los generos son:
        * "female"
        * "male"

        Las culturas son:
        * "russian" 
        * "american" 
        * "english"
        * "arab"
        * "french"
        * "afrikan"
        * "nordic"
        * "indian"
        * "spanish"
        * "turkish"
        * "chinese"
        * "japanese"
        * "polinesian"
        * "italic"
        * "slavic"
        """
        return random_full_name(
            read_excel_dict,
            BtpyPersistence.NAME_MALE_PATH,
            BtpyPersistence.NAME_FEMALE_PATH,
            BtpyPersistence.LASTNAMES_PATH,
            names_number,
            lastnames_number,
            culture,
            gender
        )
    
    def create_dict_list_excel(data:dict[list], 
        filename:str)->None:
        """
        Stores a dictionary of arrays in an 
        Excel file.
        """
        return create_dict_list_excel(data, 
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
    
    def random_country(continent:str = "")\
            ->str:
        """
        Función que generan nombres de 
     países aleatorios en ingles según 
     el continente indicado; las claves de
     continente son:
    north_america,
    europe,
    africa,
    south_america,
    central_asia,
    middle_east,
    south_asia,
    far_asia,
    oceania.
        """
        BtpyPersistence\
            .__load_country_dict()
        country_dict = BtpyPersistence\
            .COUNTRY_DICT
        import random
        country_list = []
        if(continent == ""):
            continent = random.choice(
                list(country_dict.keys()))
        country_list = country_dict\
            [continent]
        return random.choice(country_list)
    
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
        seguido de la segunda celda como un 
        par clave valor y así sucesivamente 
        con todas las celdas.
        """
        return read_excel_as_key_value(PATH)
    
    def read_excel_dict_list(path:str,
            name_list:list[str])\
                ->dict[dict]:
        """
        Funcion que lee todos los archivos
        XLSX con los nombres enviados y 
        retorna un dict anidado con los 
        datos.
        """
        return read_excel_dict_list(
            path, name_list)
    
    def read_excel_list(PATH:str)->list[str]:
        """
        Lee un archivo Excel y retorna 
        una lista (array unidimensional) 
        con todos los elementos de todas 
        las columnas.
        """
        return read_excel_list(PATH)
    
    def get_root()->str:
        """
        Funcion que obtiene la ruta 
        root(raiz) desde la que se 
        ejecuta la funcion 
        de inicio(main) de la aplicacion.
        """
        return get_root()
    
    def read_json_object(PATH:str)->dict:
        return read_json_object(PATH)
    
    def random_geo_adress(
            country_key:str = ""):
        geo_adress = GeoAdress()
        geo_adress.country = country_key
        if(country_key == ""):
            geo_adress.country \
            = BtpyPersistence\
                .random_country()
        geo_adress.region = BtpyPersistence\
            .random_region(
                geo_adress.country)
        return geo_adress
    
    def what_continent_from(continent = "")\
                ->str:
        pass
    
    def what_region_from(region)->str:
        for k in BtpyPersistence\
                    .REGIONS_DICT:
            if(region in BtpyPersistence\
                    .REGIONS_DICT[k]):
                return k
        return ""
    
    def random_profession(
            development_level:str)->str:
        """
        development level must be:
        * "primitive"
        * "medieval" 
        * "victorian" 
        * "digital"
        """
        return random_profession(
            BtpyPersistence.read_excel_dict,
            BtpyPersistence.PROFESSION_PATH,
            development_level
        )
    
    def random_region(country_key:str = ""):
        BtpyPersistence.__load_regions_dict()
        region_dict = BtpyPersistence\
            .get_region_dict()
        return random_region(
            region_dict, country_key)
    
    """
    Funcion que carga un cache de una 
    tabla de regiones para las funciones
    de persistencia.
    """
    def __load_regions_dict()-> None:
        if(BtpyPersistence.REGIONS_DICT 
                == {}):
            BtpyPersistence.REGIONS_DICT \
                = read_excel_dict(
                    BtpyPersistence\
                    .REGIONS_DICT_PATH
            )

    def __load_country_dict()->None:
        if(BtpyPersistence.COUNTRY_DICT 
                == {}):
            BtpyPersistence.COUNTRY_DICT \
                = read_excel_dict(
                    BtpyPersistence\
                    .COUNTRY_DICT_PATH
            )

    def __load_culture_properties()->None:
        if(BtpyPersistence.COUNTRY_PROPERTIES 
                == {}):
            BtpyPersistence.COUNTRY_PROPERTIES \
                = read_json_object(
                    BtpyPersistence\
                    .COUNTRY_PROPERTIES_PATH
            )

    def random_country_by_culture(culture):
        BtpyPersistence\
            .__load_culture_properties()
        country_prop = BtpyPersistence\
            .COUNTRY_PROPERTIES
        country_arr = country_prop[culture]\
            ["country_array"]
        return random.choice(country_arr)

    def random_profile(culture):
        profile = CharacterProfile(
            culture)
        profile.name = BtpyPersistence\
            .random_name(
                culture, 
                profile.gender
            )
        profile.lastname = BtpyPersistence\
            .random_lastname(culture)
        profile.profession = BtpyPersistence\
            .random_profession("digital")
        country = BtpyPersistence\
            .random_country_by_culture(culture)
        profile.geo_adress = BtpyPersistence\
            .random_geo_adress(country)
        return profile