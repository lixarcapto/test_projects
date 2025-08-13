

from btpy.Btpy import Btpy

def read_json_folder_as_dict(PATH:str)\
        ->dict[str, dict]:
    list_:list = Btpy.get_files_into(
            PATH,
            ".json"
        )
    nested_dict:dict = {}
    dict_:dict = {}
    key:str = ""
    for file_name in list_:
        dict_ = Btpy.read_json_object(
            PATH + file_name
        )
        key = file_name.replace(".json", "")\
            .upper()
        nested_dict[key] = dict_
    return nested_dict