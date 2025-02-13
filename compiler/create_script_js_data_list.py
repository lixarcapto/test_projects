

from ScriptDataJs import ScriptDataJs
from btpy_lib.btpy.src.btpy.Btpy import Btpy
from has_between import*

"""

"""
def string_is_it_a_class(string_js):
    if(" class " in string_js):
       return True
    return False

"""
Este metodo retorna un dict con dos listas; 
la class_list contiene dict con datos de 
clases de cada archivo js
y la no_class_list contiene solo string
de cada archivo js.
Tipos de archivos: script, class
"""
def create_script_js_data_list(str_js_list):
    dict_result = {
        "class_list":[],
        "no_class_list":[]
    }
    string_js = ""
    is_class = False
    for i in range(len(str_js_list)):
        string_js = str_js_list[i]
        is_class = string_is_it_a_class(
            string_js)
        if(not is_class):
            data_class = ScriptDataJs()
            data_class.string_js = string_js
            data_class.file_type = "script"
            dict_result["no_class_list"]\
                .append(data_class)
        elif(is_class):
            data_class = new_scriptdata_class(
                string_js)
            dict_result["class_list"].append(
                data_class)
    return dict_result

def new_scriptdata_class(str_js):
    dad_class = Btpy.get_between(str_js, 
                "extends ", "{")
    class_name = Btpy.get_between(str_js, 
            "class ", " ")
    # crea una data class --------------
    data_class = ScriptDataJs()
    data_class.extends_key = dad_class\
        .strip()
    data_class.string_js = str_js
    data_class.file_type = "class"
    data_class.class_name = class_name\
        .strip()
    return data_class