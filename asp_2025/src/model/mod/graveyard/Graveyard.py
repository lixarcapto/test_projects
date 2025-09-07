

from .Epitaph import Epitaph

class Graveyard:

    """
    Esta clase representa a un cementerio
    de personajes; contiene registros de 
    personajes muertos llamados epitafios;
    estos epitafios contienen datos
    reducidos de los personajes.
    """

    epitaph_dict:dict = {}
    actual_epitaph:Epitaph = Epitaph()

    def has(ID):
        key_list = list(Graveyard\
            .epitaph_dict.keys())
        return str(ID) in key_list
    
    def write():
        txt = "\n"
        e = None
        for k in Graveyard.epitaph_dict:
            e = Graveyard.epitaph_dict[k]
            txt += e.write() + "\n"
        return txt

    def set_id(ID:str):
        Graveyard.actual_epitaph.id = ID

    def set_cause_death_key(KEY:str):
        Graveyard.actual_epitaph\
            .cause_death_key = KEY
        
    def set_specific_death(TEXT:str):
        Graveyard.actual_epitaph\
            .specific_death = TEXT
        
    def set_full_name(TEXT:str):
        Graveyard.actual_epitaph\
            .full_name = TEXT
        
    def set_culture_key(KEY:str):
        Graveyard.actual_epitaph\
            .culture_key = KEY
        
    def set_year(NUMBER:int):
        Graveyard.actual_epitaph\
            .years = NUMBER
        
    def save_epitaph():
        id_ = Graveyard.actual_epitaph.id
        Graveyard.epitaph_dict[str(id_)] \
            = Graveyard.actual_epitaph
        Graveyard.actual_epitaph\
            = Epitaph()

    def get(id_):
        return Graveyard.epitaph_dict\
            [str(id_)]