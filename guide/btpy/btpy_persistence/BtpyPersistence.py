

from .in_deps import*
from ..btpy_maths.BtpyMaths import BtpyMaths

class BtpyPersistence(BtpyMaths):

    NAME_FEMALE_PATH = "./btpy/res/name_female_data.xlsx"
    NAME_MALE_PATH = "./btpy/res/name_male_data.xlsx"
    LASTNAMES_PATH = "./btpy/res/lastname_data.xlsx"

    # -----------------------------------

    # TXT --------------------------------
    
    def delete_txt(filename:str)->None:
        """
        Deletes the specified text file.
        @ by Gemini
        """
        delete_txt(filename)

    def write_txt(PATH:str, TEXT:str = "")\
            ->bool:
        """
        Escribe el texto proporcionado en 
        un archivo de texto en la ruta 
        especificada.
        Si el archivo ya existe, lo 
        sobreescribe.
        Returns:bool: True si el archivo se 
        escribió correctamente, False si 
        hubo un error.
        """
        write_txt(PATH, TEXT)

    def read_txt(file_path:str)->str:
        """
        Loads the entire text from 
        a text file as a string.
        """
        return read_txt(file_path)
    
    # -------------------------------------

    # RANDOM DATA -------------------------
    
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
        * "hebrew"
        """
        return random_name(
            read_xlsx_dict_list,
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
        * "hebrew"
        """
        return random_lastname(
          read_xlsx_dict_list,
          BtpyPersistence.LASTNAMES_PATH,
          CULTURE
        )
    
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
        * "hebrew"
        """
        return random_full_name(
            read_xlsx_dict_list,
            BtpyPersistence.NAME_MALE_PATH,
            BtpyPersistence.NAME_FEMALE_PATH,
            BtpyPersistence.LASTNAMES_PATH,
            names_number,
            lastnames_number,
            culture,
            gender
        )
    
    # ------------------------------------
    
    # SOUND -----------------------------

    def play_sound(route:str)->None:
        return play_sound(route)
    
    # ------------------------------------

    # DOCX -------------------------------
    
    def write_docx(route:str, text:str)\
            ->None:
        """
        Funcion que almacena en un archivo 
        docx el texto
        enviado.
        """
        write_docx(route, text)

    def read_docx(ruta_archivo:str)->str:
        """
        Funcion que carga un archivo 
        ".docx" como texto almacenando
        sus saltos de linea y espacios.
        """
        return read_docx(ruta_archivo)

    # ------------------------------------

    # IMAGES -----------------------------

    def read_animation_folder(PATH)\
            ->list[str]:
        """
        Funcion que lee obtiene las 
        rutas ordenadas en una lista de 
        cada frame de un animation folder
        formato; este formato consiste en
        carpetas de imagenes para crear
        una animacion que solo tienen de nombre
        el orden de dibujado como un entero 
        del 0 al 100
        """
        return read_animation_folder(PATH)
    
    def read_photoimage(route:str, size_x, 
        size_y)->PhotoImage:
        """
        Funcion que lee una imagen en la 
        direccion indicada y la carga como 
        un objeto PhotoImage de PIL
        """
        return read_photoimage(route, size_x, 
            size_y)
    
    def image_size(image_route:str)->dict:
        return image_size(image_route)
    
    # -------------------------------------
    
    # JSON --------------------------------

    def read_json_object(PATH:str)->dict:
        return read_json_object(PATH)
    
    # --------------------------------------
    
    # OPEN --------------------------------
    
    def load_word(DOCX_ROUTE:str)->None:
        """
        Función que obtiene la ruta 
        absoluta de un documento docx para  
        ejecutarlo en el programa Word 
        en windows.
        """
        return load_word(DOCX_ROUTE)
    
    # SYSTEM ----------------------------
    
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
    
    def get_root()->str:
        """
        Funcion que obtiene la ruta 
        root(raiz) desde la que se 
        ejecuta la funcion 
        de inicio(main) de la aplicacion.
        """
        return get_root()
    
    def get_files_into(PATH_FOLDER:str,
            EXTENSION:str = "")\
            ->list[str]:
        """
        Funcion que obtiene los nombres 
        completos de todos los archivos 
        dentro de una carpeta con su 
        extension. Si envia una extension
        entonces filtrara los nombres 
        que tengan esa extension
        automaticamente.
        By Gemini
        """
        return get_files_into(
            PATH_FOLDER, EXTENSION)
    
    def execute(script_path:str)->None:
        """
        Executes the given Python script.
        """
        return execute(script_path)
    
    # Check if the file exists using 
    # os.path.exists()
    def check_path(PATH:str, 
        FILE_EXTENSION:str = "")->bool:
        return check_path(
            PATH, 
            FILE_EXTENSION
        )

    # PATHS ----------------------------
    
    """
    Funcion que carga un cache de una 
    tabla de regiones para las funciones
    de persistencia.
    """
    def __load_regions_dict()-> None:
        if(BtpyPersistence.REGIONS_DICT 
                == {}):
            BtpyPersistence.REGIONS_DICT \
                = read_xlsx_dict_list(
                    BtpyPersistence\
                    .REGIONS_DICT_PATH
            )

    def __load_country_dict()->None:
        if(BtpyPersistence.COUNTRY_DICT 
                == {}):
            BtpyPersistence.COUNTRY_DICT \
                = read_xlsx_dict_list(
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
    
    # -----------------------------------

    # XLSX ------------------------------

    def read_xlsx_flat_dict(PATH_XLSX:str)\
            ->dict:
        """
        Función que lee todos los pares 
        clave valor que se encuentren en un 
        archivo Excel como un diccionario.   
        leerá cada primera celda de la fila 
        seguido de la segunda celda como un 
        par clave valor y así sucesivamente 
        con todas las celdas.
        """
        return read_xlsx_flat_dict(
            PATH_XLSX
        )
    
    
    def read_folder_xlsx_dict_list(
            path:str,
            name_list:list[str])\
                ->dict[dict]:
        """
        Funcion que lee todos los archivos
        XLSX con los nombres enviados y 
        retorna un dict anidado con los 
        datos.
        """
        return read_folder_xlsx_dict_list(
            path, name_list)
    
    def read_xlsx_flat_list(PATH_XLSX:str)\
            ->list[str]:
        """
        Lee un archivo Excel y retorna 
        una lista (array unidimensional) 
        con todos los elementos de todas 
        las columnas.
        """
        return read_xlsx_flat_list(
            PATH_XLSX)
    
    def read_xlsx_dict_list(PATH_XLSX:str)\
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
        return read_xlsx_dict_list(
            PATH_XLSX)
    
    def write_xlsx_dict_list(
            DICT_LIST:dict[list], 
            PATH:str)->None:
        """
        Stores a dictionary of arrays 
        in an Excel file.
        """
        return write_xlsx_dict_list(
            DICT_LIST, 
            PATH
        )
    
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
        return read_xlsx_nested_dict_row(
            PATH_XLSX
        )
    
    def write_xlsx_nested_dict_row(
            PATH_XLSX:str):
        """
        TODO
        """
        pass
    
    def read_xlsx_nested_dict_column(
            PATH_XLSX:str)\
            ->dict[dict]:
        """
        función de persistencia que lee un 
        archivo Excel como un diccionario 
        anidado en horizontal
        """
        return read_xlsx_nested_dict_column(
            PATH_XLSX
        )
    
    def write_xlsx_nested_dict_column(
            PATH_XLSX:str):
        """
        TODO
        """
        pass

    def write_json_object(
            PATH: str, 
            DICT: dict)-> bool:
        """
        Crea un archivo JSON y escribe en 
        él un diccionario de Python.
        Returns:
            bool: Retorna True si el archivo 
            se creó y escribió con éxito, 
            False en caso contrario.
        """
        return write_json_object(
            PATH,
            DICT
        )
    
    def create_folder(PATH: str) -> bool:
        """
        Crea una carpeta en la ruta 
        especificada.
        bool: True si la carpeta fue 
        creada (o ya existía), False si 
        hubo un error.
        """
        return create_folder(PATH)
    
    def write_xlsx_flat_dict(
            DICT: Dict[Any, Any], 
            PATH: str):
        return write_xlsx_flat_dict(
            DICT,
            PATH
        )


    # -----------------------------------