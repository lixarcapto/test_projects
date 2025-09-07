


from btpy.Btpy import Btpy

class Persistence:

    RESOURCE_PATH:str = "./res/"
    DATA_MOD_PATH:str = "data_mods/"
    TEXTURE_PACK_PATH:str = "texture_pack/"
    MOD_NAME:str = "default"
    REGIONAL_GROUP_FOLDER:str \
        = "regional_gruop_xlsx/"
    RECIPE_FOLDER:str = "recipe_json/"
    PROFESSION_FOLDER\
        :str = "profession_json/"
    AGE_RANGE_FILE:str = "age_range"
    WORLD_CONST_FILE:str = "world_const"
    STRUCTURE_FOLDER:str = "struct_bp_json/"
    CULTURAL_GROUP_FOLDER:str \
        = "cultural_gruop_xlsx/"
    regional_group_key_list:list = []
    culture_key_list:list = []
    texture_pack_name = "default"
    CITIZEN_IMAGE_EXTENSION = ".png"

    def __init__(self):
        pass

    def get_mod_path()->str:
        """
        Retorna la ruta del mod de datos
        actualmente seleccionado.
        """
        return Persistence.RESOURCE_PATH\
            + Persistence.DATA_MOD_PATH\
            + Persistence.MOD_NAME\
            + "/"
    
    def get_texture_pack_path()->str:
        return Persistence.RESOURCE_PATH\
            + Persistence.TEXTURE_PACK_PATH\
            + Persistence.texture_pack_name\
            + "/"
        
    def get_regional_group_path()->str:
        path = Persistence.get_mod_path()
        path += Persistence\
            .REGIONAL_GROUP_FOLDER
        return path
        
    def get_regional_group_key_list():
        folder_path = Persistence\
            .get_regional_group_path()
        return Btpy.get_files_into(
            folder_path, 
            ".xlsx"
        )
    
    def get_profession_path()->str:
        path = Persistence.get_mod_path()
        return path + Persistence\
            .PROFESSION_FOLDER
    
    def get_cultural_group_path()->str:
        path = Persistence.get_mod_path()
        path += Persistence\
            .CULTURAL_GROUP_FOLDER
        return path
    
    def get_structure_path()->str:
        path = Persistence.get_mod_path()
        path += Persistence\
            .STRUCTURE_FOLDER
        return path
    
    def get_recipe_path()->str:
        path = Persistence.get_mod_path()
        path += Persistence\
            .RECIPE_FOLDER
        return path
    
    def get_names_cultural_group()->str:
        path = Persistence\
            .get_cultural_group_path()
        return Btpy.get_files_into(
            path, 
            ".xlsx"
        )
    
    def get_age_range_path()->str:
        path = Persistence.get_mod_path()
        path += Persistence.AGE_RANGE_FILE
        path += ".xlsx"
        return path

    def read_cultural_nested_dict():
        names_list = Persistence\
            .get_names_cultural_group()
        path_folder = Persistence\
            .get_cultural_group_path()
        nested_dict = {}
        path = ""
        k = ""
        for name in names_list:
            k = name.replace(".xlsx", "")
            path = path_folder \
                + k + ".xlsx"
            nested_dict[k] = Btpy\
                .read_xlsx_dict_list(
                    path
                )
        return nested_dict

    def read_regional_group_nested_dict()\
            ->dict[dict]:
        names_list = Persistence\
            .get_regional_group_key_list()
        path_folder = Persistence\
            .get_regional_group_path()
        nested_dict = {}
        path = ""
        k = ""
        for name in names_list:
            k = name.replace(".xlsx", "")
            path = path_folder \
                + k + ".xlsx"
            nested_dict[k] = Btpy\
                .read_xlsx_dict_list(
                    path
                )
        return nested_dict
    
    def read_age_range_dict():
        nested_dict = {}
        path = Persistence\
            .get_age_range_path()
        nested_dict = Btpy\
            .read_xlsx_nested_dict_row(path)
        v = None
        for k in nested_dict:
            v = Btpy.string_number_list_to_list(
                nested_dict[k]["range_list"]
            )
            nested_dict[k]["range_list"] \
                = v
            v = nested_dict[k]["fertility"]
            nested_dict[k]["fertility"] \
                = float(v)
            v = nested_dict[k]\
                ["death_probability"]
            nested_dict[k]\
                ["death_probability"]\
                    = float(v)
            v = nested_dict[k]\
                ["baldness_probability"]
            nested_dict[k]\
                ["baldness_probability"]\
                    = float(v)
            v = nested_dict[k]\
                ["gray_hair_probability"]
            nested_dict[k]\
                ["gray_hair_probability"]\
                    = float(v)
        return nested_dict
    
    def read_recipe_nested_dict()\
            ->dict:
        path_folder = Persistence\
            .get_recipe_path()
        recipe_list = Btpy.get_files_into(
            path_folder, 
            ".json")
        dict_ = {}
        path = ""
        k = ""
        for e in recipe_list:
            path = path_folder + e
            k = e.replace(".json", "")
            dict_[k] = Btpy\
                .read_json_object(path)
        return dict_
    
    def read_structure_nested_dict()\
            ->dict:
        path_folder = Persistence\
            .get_structure_path()
        recipe_list = Btpy.get_files_into(
            path_folder, 
            ".json")
        dict_ = {}
        path = ""
        k = ""
        for e in recipe_list:
            path = path_folder + e
            k = e.replace(".json", "")
            dict_[k] = Btpy\
                .read_json_object(path)
        return dict_
    
    def read_profession_nested_dict():
        path_folder = Persistence\
            .get_profession_path()
        recipe_list = Btpy.get_files_into(
            path_folder, 
            ".json")
        dict_ = {}
        path = ""
        k = ""
        for e in recipe_list:
            path = path_folder + e
            k = e.replace(".json", "")
            dict_[k] = Btpy\
                .read_json_object(path)
        return dict_
    
    def read_genetic_keys_dict()->dict:
        path = Persistence.get_mod_path()
        path += "genetic_keys.xlsx"
        return Btpy\
            .read_xlsx_dict_list(path)
    
    def read_world_const()->dict:
        path = Persistence.get_mod_path()\
        + Persistence.WORLD_CONST_FILE\
        + ".xlsx"
        return Btpy.read_xlsx_dict_list(
            path
        )