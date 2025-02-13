
from btpy_lib.btpy.src.btpy.Btpy import Btpy


"""
Funcion que elimina las lineas de 
import from y export de cada texto
en el array enviado. Solo funciona si 
estan bien escritos.
SDJS significa script data javascript
XXX: hay un error aqui al modificar los
string.
"""
def remove_import_from_SDJS_list(
        SDJS_list):
    string_js = ""
    for i in range(len(SDJS_list)):
        string_js = SDJS_list[i].string_js
        string_js = __remove_import_from(
            string_js)
        string_js = __strip(string_js)
        SDJS_list[i].string_js = string_js
    return SDJS_list

def __remove_import_from(text):
    r = text
    while("import" in r):
        r = Btpy.remove_between(r,
            "import", "}")
        print("REMOVE IMPORT", r)
    while("from" in r):
        if(Btpy.has_between(r,
            "from \"", "\";")):
            r = Btpy.remove_between(r,
                "from \"", "\";")
        if(Btpy.has_between(r,
            "from \"", "\"\n\n")):
            r = Btpy.remove_between(r,
                "from \"", "\"\n\n")
        if(Btpy.has_between(r,
            "from \"", "\" ")):
            r = Btpy.remove_between(r,
                "from \"", "\" ")
        print("REMOVE FROM", r)
    while("export" in r):
        r = r.replace("export ", "")
        print("REMOVE EXPORT", r)
    return r

def __strip(text):
    return f"{text.strip()}\n "

