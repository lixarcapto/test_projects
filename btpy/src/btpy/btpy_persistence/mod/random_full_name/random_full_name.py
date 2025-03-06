


from ..random_lastname.random_lastname import*
from ..random_name.random_name import*

CACHE_CULTURES_LIST:list = []

def random_full_name(
                read_excel_dict,
                PATH_NAME_MALE_XLSX,
                PATH_NAME_FEMALE_XLSX, 
                LASTNAMES_PATH,
                names_number,
                lastnames_number,
                culture = "", 
                gender = ""
                ):
        """
        Crea un nombre aleatorio completo; 
        es decir con nombres y apellidos.
        La cantidad de nombres y apellidos
        se indica al inicio del metodo.
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
        global CACHE_CULTURES_LIST
        if(CACHE_CULTURES_LIST == []):
            dict_r = read_excel_dict(
                     LASTNAMES_PATH)
            CACHE_CULTURES_LIST\
                = list(dict_r.keys())
        if(gender == ""):
            gender = random.choice(
                ["female", "male"])
        if(culture == ""):
            culture = random.choice(
                CACHE_CULTURES_LIST
            )
        name = ""
        for i in range(names_number):
            name += random_name(
                read_excel_dict,
                PATH_NAME_MALE_XLSX,
                PATH_NAME_FEMALE_XLSX,
                culture, 
                gender
            )
        for i in range(lastnames_number):
            name += " " + random_lastname(
                read_excel_dict,
                LASTNAMES_PATH,
                culture
            )
        return name

