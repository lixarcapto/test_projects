


from ....btpy_random.mod.random_choice.random_choice import*
from ..read_excel_dict.read_excel_dict import*

CACHE_NAMES_DICT = {}
NAME_MALE_XLSX = "name_male_data.xlsx"
NAME_FEMALE_XLSX = "name_female_data.xlsx"
resource_path = "./btpy/res"

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
        gender = random_choice(
            ["male", "female"])
        # carga un cache con los nombres
        name = ""
        names_list = []
        if(CACHE_NAMES_DICT == {}):
            male_dict = read_excel_dict(
                resource_path \
                + "/" + NAME_MALE_XLSX)
            female_dict = read_excel_dict(
                resource_path \
                + "/" + NAME_FEMALE_XLSX)
        names_dict = None
        if(gender == "male"):
            names_dict = male_dict
        elif(gender == "female"):
            names_dict = female_dict
        # adapta la clave cultura faltante
        if(culture == ""):
            names_list = random_choice(
                names_dict)
        else:
            names_list = names_dict[culture]
        # genera nombre aleatorio
        name =  random_choice(names_list)
        return name