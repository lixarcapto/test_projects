


"""
    Funcion que separa los bebes que pueden caminar
    de sus madres, para ser personajes independientes.
"""
# return Person
def separate_the_baby(data):
    data.is_pregnant = False
    data.baby_can_walk = False
    person = data.baby_person
    data.baby_person = None
    return person
