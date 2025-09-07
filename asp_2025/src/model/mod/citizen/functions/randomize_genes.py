

def randomize_genes(citizen_data):
    """
    Funcion que aleatoriza los genes
    del persona, primero randomiza los
    genes de los padres si es de tipo
    legendario; es decir un primer
    ciudadano creado, y despues
    los del personaje.
    """
    if(citizen_data.get_is_legendary()):
        k = citizen_data\
            .get_regional_group_key()
        citizen_data.genes_dad\
            .data.set_regional_group_key(k)
        citizen_data.genes_dad.randomize()
        k = citizen_data\
            .get_regional_group_key()
        citizen_data.genes_mom\
            .data.set_regional_group_key(k)
        citizen_data.genes_mom.randomize()
    citizen_data.genes_self.randomize()
    return citizen_data