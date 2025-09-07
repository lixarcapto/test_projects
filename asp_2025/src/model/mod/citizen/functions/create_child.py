

from btpy.Btpy import Btpy
from .randomize_gender import*
from .manifest_genetic_traits import*
from .create_genes_zygote import*

def create_child(citizen_data, 
            citizen_dad,
            citizen_ref):
        child  = citizen_ref()
        # ----------------------------------
        # randomiza el genero
        child.data = randomize_gender(
            child.data)
        # ----------------------------------
        # definir la postal de origen

        postcard = citizen_dad.data\
            .actual_postcard
        child.data.origin_postcard\
            = postcard

        # ----------------------------------
        # randomiza la cultura
        culture_list = []
        culture_list.append(
            citizen_dad.data.get_culture_key())
        culture_list.append(
            citizen_data.get_culture_key())
        culture_k = Btpy.random_choice(
            culture_list
        )
        child.data.set_culture_key(
            culture_k)
        # ---------------------------------
        # randomiza el nombre
        mom_culture = citizen_data\
            .get_culture_key()
        names_k_mom = citizen_data\
            .get_key_names()
        dad_culture = citizen_dad\
            .data.get_culture_key()
        names_k_dad = citizen_dad\
            .get_key_names()
        # randomiza el primer nombre
        key_name = Btpy.random_name(
                names_k_dad,
                citizen_data.get_gender_key()
            )
        child.data.set_name(key_name)
        # randomiza segundo nombre
        key_name = Btpy.random_name(
                names_k_mom,
                citizen_data.get_gender_key()
            )
        child.data.set_second_name(
            key_name)
        # selecciona los apellidos
        lastname = citizen_data\
            .get_second_lastname()
        child.data.set_second_lastname(
            lastname
        )
        lastname = citizen_dad\
            .data.get_lastname()
        child.data.set_lastname(
            lastname
        )
        # ----------------------------------
        # randomiza la genetica 
        child.data.genes_self \
            = create_genes_zygote(
                citizen_data,
                citizen_dad
        )
        child.data.genes_dad = citizen_dad\
            .data.genes_self
        child.data.genes_mom = citizen_data\
            .genes_self
        # ---------------------------------
        group_k = citizen_dad.data\
            .get_regional_group_key()
        child.data.set_regional_group_key(
            group_k
        )
        # ---------------------------------
        # aplica correcciones de los 
        # rasgos
        child.data = manifest_genetic_traits(
                child.data)
        child.apply_cultural_traits()
        # ---------------------------------
        return child