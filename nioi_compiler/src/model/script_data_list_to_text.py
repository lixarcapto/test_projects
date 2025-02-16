


def script_data_list_to_text(
            script_data_list)->str:
    txt:str = ""
    for script_data in script_data_list:
        txt += script_data.string_js
    return txt