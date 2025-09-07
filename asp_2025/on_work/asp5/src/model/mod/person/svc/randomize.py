


from .random_name import*
from .random_lastname import*
from .randomize_appearance import*
from .randomize_age import*

"""
    Funcion que genera un ciudadano semi-aleatorio
    en base a la cultura asignada.
"""
def randomize(data):
    data.name = random_name(data)
    data.second_name = random_name(data)
    data.lastname = random_lastname(data)
    data.second_lastname = random_lastname(data)
    # randomiza la edad
    data.age_code = randomize_age(data)
    data = randomize_appearance(data)
    return data
