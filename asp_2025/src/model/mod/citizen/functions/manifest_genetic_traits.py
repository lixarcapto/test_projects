

from .apply_genetic_traits import*

def manifest_genetic_traits(citizen_data):
    genes = citizen_data\
            .genes_self
    key = genes.data.get_regional_group_key()
    citizen_data.set_regional_group_key(
            key)
    n = genes.data.get_hair_color_number()
    citizen_data.set_hair_color_number(n)
    n = genes.data.get_hair_type_number()
    citizen_data.set_hair_type_number(n)
    n = genes.data.get_eye_color_number()
    citizen_data.set_eye_color_number(n)
    n = genes.data.get_eye_type_number()
    citizen_data.set_eye_type_number(n)
    n = genes.data.get_skin_color_number()
    citizen_data.set_skin_color_number(n)
    value = genes.data.get_is_bald()
    citizen_data.set_is_bald(value)
    n = genes.data.get_nose_type_number()
    citizen_data.set_nose_type_number(n)
    n = genes.data.get_mouth_type_number()
    citizen_data.set_mouth_type_number(n)
    value = genes.data.get_is_freckled()
    citizen_data.set_is_freckled(value)
    citizen_data = apply_genetic_traits(
        citizen_data)
    value = genes.data.get_has_infertility()
    citizen_data.set_has_infertility(value)
    return citizen_data