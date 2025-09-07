
from .combine_genes import*

def create_genes_zygote(citizen_data,
        dad_citizen):
    """
    Funcion que combina la genetica del 
    padre y la madre para crear un nuevo
    objeto genetico hijo. Para que funcione
    el primer objeto debe ser la madre.
    """
    if(not citizen_data.get_gender_key() \
            == "female"):
        return None
    genes_zygote = combine_genes(
        dad_citizen.data.genes_self,
        citizen_data.genes_self,
        dad_citizen.data.genes_mom,
        dad_citizen.data.genes_dad,
        citizen_data.genes_mom,
        citizen_data.genes_dad
    )
    return genes_zygote