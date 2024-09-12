


from ..random_lastname.random_lastname import*
from ..random_name.random_name import*

def random_full_name(gender, culture):
    txt = ""
    txt += random_name(gender, culture) + " "
    txt += random_name(gender, culture) + " "
    txt += random_lastname(culture) + " "
    txt += random_lastname(culture)
    return txt

