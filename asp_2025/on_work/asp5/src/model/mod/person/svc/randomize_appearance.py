


from .manifest_the_genes import*
import random

"""
    Funcion que genera caracteristicas aleatorias
    para los ciudadanos iniciales.
"""
def randomize_appearance(data):
    data.age = 0
    data.gender = random \
        .choice(data.PERSON_CONST.GENDER_ARRAY)
    data.weight_code = random.randint(0,
        len(data.PERSON_CONST.WEIGHT_ARRAY) -1)
    data.actual_height_code = random.randint(0,
        len(data.PERSON_CONST.HEIGHT_ARRAY) -1)
    data.hair_style = random \
        .choice(data.PERSON_CONST.HAIR_STYLE_ARRAY)
    # randomiza sus genes y los manifiesta
    data.gen_own.randomize(data.gen_group)
    data = manifest_the_genes(data)
    return data
