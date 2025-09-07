

from ..CharacterData import CharacterData
from .get_age_range_gender import*

def write_appearance(data:CharacterData):
    txt = "is a "
    # asignar el articulo de genero
    txt += get_age_range_gender(
        data.get_gender(),
        data.get_age_range()
    )
    txt += ", has " \
    + data.get_hair_type()\
    + data.get_hair_color() + " hair, "\
    + data.get_eye_type()\
    + data.get_eye_color() + " eyes, "\
    + data.get_skin_color() + " skin, "\
    + "with " + data.get_age_range() + " "\
    + "looking, and a "\
    + data.get_actual_height_key() + " "\
    + "height"
    return txt