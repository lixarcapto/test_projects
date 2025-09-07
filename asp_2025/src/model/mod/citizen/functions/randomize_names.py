
from btpy.Btpy import Btpy

def randomize_names(data):
        culture_k = data\
            .get_culture_key()
        names_k = data.get_key_names()
        gender_k = data.get_gender_key()
        name = Btpy.random_name(
            names_k,
            gender_k
        )
        data.set_name(name)
        name = Btpy.random_name(
                names_k,
                gender_k
            )
        data.set_second_name(name)
        lastname = Btpy.random_lastname(
                names_k
            )
        data.set_lastname(lastname)
        lastname = Btpy.random_lastname(
                names_k
            )
        data.set_second_lastname(
            lastname)
        return data