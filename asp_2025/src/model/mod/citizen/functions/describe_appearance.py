

from ..citizen_constants import*
from ..CitizenData import CitizenData

def descripe_appearance(data:CitizenData)\
            ->str:
        personal = data\
            .get_personal_pronoun()
        possesive = data\
            .get_possessive_pronoun()
        txt = ""
        txt += personal + " had a " 
        txt += data.get_regional_group_key()
        txt += " appearance, her eyes were " 
        txt +=  data.get_eye_type_key()
        txt += " shaped "
        txt +=  data.get_eye_color_key()
        txt += " " + get_eye_color_detail(
             data) + ", "
        txt += possesive + " nose was big " 
        txt += data.get_nose_type_key()
        txt += f", {possesive} hair was "
        txt +=  f"{data.get_hair_type_key()} "
        txt +=  f"{data.get_hair_color_key()} "
        txt += get_hair_color_detail(data)
        txt += ", wearing a "
        txt += data.get_hairstyle_key()
        txt += " hairstyle, and had an " 
        txt += data.get_height_actual_key()
        txt += " height, "
        txt += "your skin is " + data\
            .get_skin_color_key() 
        if(data.get_is_freckled()):
            txt += " with freckles on "
            txt += possesive + " face"
        txt += ", "
        txt += personal + " was carrying a "
        txt += CARRIED_OBJECT_BY_PROFESSION\
            [data.get_profession_key()]
        txt += f" in {possesive} hands. "
        if(data.get_is_pregnant()):
            txt += f"She seems to be pregnant, "
        if(data.get_is_a_mother()):
            txt += "She is a mother accompanied by" 
            txt += possesive + "children: \n"
            for child in data.child_in_care_list:
                 txt += child.write()
        txt += "\n"
        return txt

def get_eye_color_detail(data)->str:
    n = data.get_eye_color_number()
    detail = EYE_COLOR_DETAIL_TUPLE[n]
    return detail

def get_hair_color_detail(data)->str:
    n = data.get_hair_color_number()
    detail = HAIR_COLOR_DETAIL_TUPLE[n]
    return detail