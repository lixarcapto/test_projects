


from ..CharacterData import CharacterData
from .write_name import*
from .write_appearance import*

def write_presentation( data:CharacterData)\
        ->str:
    txt = "" + write_appearance(data) + " " \
    + data.get_salute() + " " \
    + "my name is " \
    + write_name(data) + " " \
    + f"i am a {data.age_time.write_age()} "\
    + data.get_age_range()
    return txt