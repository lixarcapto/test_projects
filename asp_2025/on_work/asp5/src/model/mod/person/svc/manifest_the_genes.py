


"""
    Funcion que aplica los datos en sus genes como
    caracteristicas fisicas.
"""
def manifest_the_genes(data):
    gen = data.gen_own
    data.eye_type = gen.eye_type
    data.skin_color = gen.skin_color
    data.maximum_height_code = gen.maximum_height_code
    data.hair_type = gen.hair_type
    data.hair_color = gen.hair_color
    data.eye_color = gen.eye_color
    data.is_bald = gen.is_bald
    data.has_frekkles = gen.has_frekkles
    return data
