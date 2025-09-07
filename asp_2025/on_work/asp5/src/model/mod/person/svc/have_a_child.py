


"""
    Funcion que crea un personaje bebe para
    el personaje actual, usando al personaje enviado
    como padre.
"""
def have_a_child(data, person):
    baby_person = Person()
    data.gen_own = self.data.gen_own \
        .creates_new_gen(person.data.gen_own)
    data.baby_person.inherit_the_genes(
        person.data.gen_father,
        person.data.gen_mother
    )
    data.time_pregnant = 12
    data.is_pregnant = True
    data.baby_person = baby_person
    return data
