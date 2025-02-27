


from ..random_lastname.random_lastname import*
from ..random_name.random_name import*

CACHE_CULTURES_LIST:list = []

def random_full_name(
                read_excel_dict,
                PATH_NAME_MALE_XLSX,
                PATH_NAME_FEMALE_XLSX, 
                LASTNAMES_PATH,
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
        name += random_name(
             read_excel_dict,
             PATH_NAME_MALE_XLSX,
             PATH_NAME_FEMALE_XLSX,
             culture, 
             gender
        )
        name += " " + random_name(
             read_excel_dict,
             PATH_NAME_MALE_XLSX,
             PATH_NAME_FEMALE_XLSX,
             culture, 
             gender
        )
        name += " " + random_lastname(
             read_excel_dict,
             LASTNAMES_PATH,
             culture)
        name += " " + random_lastname(
             read_excel_dict,
             LASTNAMES_PATH,
             culture)
        return name

