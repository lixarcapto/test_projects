

from .have_a_child import*
import random

"""
    Funcion que reliza una relacion sexual entre
    el personaje enviado y este personaje.
"""
def has_sex(data, person):
    # contagia enfermedades sexuales
    if(person.data.has_ETS or data.has_ETS):
        person.data.has_ETS = True
        data.has_ETS = True
    # elige por probabilidad si queda embarazada
    if((data.gender == "female") \
    and (random.randint(0, 100) <= data.FERTILITY_PERCENT)):
        data = have_a_child(person)
    return data
