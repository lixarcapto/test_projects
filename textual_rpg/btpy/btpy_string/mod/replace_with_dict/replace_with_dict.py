

def replace_with_dict(TEXT:str, 
        TRANSLATE_DICT:dict[str])->str:
    txt = TEXT
    for key in TRANSLATE_DICT:
        txt = txt.replace(key, 
            TRANSLATE_DICT[key])
    return txt