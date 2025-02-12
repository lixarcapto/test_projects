
from btpy_lib.btpy.src.btpy.Btpy import Btpy

def remove_import_from(text):
    r = ""
    r = Btpy.remove_between(text,
            "import", "}")
    r = Btpy.remove_between(r,
            "from \"", "\";")
    r = Btpy.remove_between(r,
            "from \"", "\"\n\n")
    r = Btpy.remove_between(r,
            "from \"", "\" ")
    r = r\
        .replace("export ", "")
    return r

def remove_comments(text):
    r = text
    while("/*" in r):
        r = Btpy.remove_between(r,
                "/*", "*/")
    while("//" in r):
        r = Btpy.remove_between(r,
            "//", " ")
        r = Btpy.remove_between(r,
            "//", "\n\n")
    return r