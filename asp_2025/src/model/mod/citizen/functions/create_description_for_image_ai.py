

from ..CitizenData import CitizenData
from ..citizen_constants import*
from .get_age_range_nickname import*

def create_description_for_image_ai(
        citizen_data:CitizenData):
    """
    Esta funcion que crea una
    descripcion diseñada para
    enviarla a una API de IA
    para generar una imagen
    o textos usando como parametro
    el personaje.
    """
    dt = citizen_data
    txt = ""
    txt += dt.get_culture_key() + " "
    txt += get_age_range_nickname(dt) + " "
    txt += dt.get_profession_key() + " "
    txt += " carrying a "
    txt += CARRIED_OBJECT_BY_PROFESSION\
        [dt.get_profession_key()]
    txt += ", with "
    txt += dt.get_skin_color_key()+ " "
    txt += "skin, "
    txt += dt.get_hair_type_key() + " "
    txt += dt.get_hair_color_key() + " "
    txt += "hair, "
    txt += dt.get_eye_type_key() + " "
    txt += dt.get_eye_color_key() + " "
    txt += "eyes, and "
    txt += dt.get_height_actual_key() + " "
    txt += "height."
    return txt
