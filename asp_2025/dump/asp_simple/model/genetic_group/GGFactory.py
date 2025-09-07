

from .GeneticGroup import GeneticGroup
from persistence.Persistence import Persistence
from ..gen.Gen import Gen
from btpy.src.btpy.Btpy import Btpy
# TODO eliminar dependencia
from ..gen.appearance_const \
    import GENETIC_GROUP_TUPLE

class GGFactory:

    """
     Clase que almacena instancias de 
     grupos genéticos para consultar 
     sus datos. GG es un nombre para 
     geneticgroup.
    """

    def __init__(self):
        self.gg_dict:dict[GeneticGroup] = {}
        self.init_genetic_groups()

    def get(self, KEY:str)->GeneticGroup:
        """
        Obtiene el geneticgrup con el nombre
        indicado del diccionario.
        """
        return self.gg_dict[KEY]

    def add(self, NAME:str, 
            gg_dict:dict[str]):
        """
        Agrega un geneticgroup al diccionario.
        """
        gg = self.gg_dict_to_gg_object(
            NAME, gg_dict)
        self.gg_dict[gg.name] = gg

    def gg_dict_to_gg_object(self, 
            NAME:str, gg_dict:dict[str]):
        """
        Transforma un groupobject de 
        diccionario a un groupobject de 
        objeto.
        """
        gg = GeneticGroup(NAME)
        gg.add_eye_color(gg_dict["eye_color"])
        gg.add_eye_type(gg_dict["eye_type"])
        gg.add_hair_color(gg_dict["hair_color"])
        gg.add_hair_type(gg_dict["hair_type"])
        gg.add_maximum_size(gg_dict["maximum_size"])
        gg.add_skin_color(gg_dict["skin_color"])
        return gg

    def init_genetic_groups(self):
        gg_nested_dict = Persistence\
            .read_genetic_grups(
                GENETIC_GROUP_TUPLE
            )
        for k in gg_nested_dict:
            self.add(k, gg_nested_dict[k])

    def create_gen(self, gg_key:GeneticGroup)\
            ->Gen:
        """
        Crea un gen aleatorio usando el 
        grupo genetico indicado.
        """
        gg = self.get(gg_key)
        gen = Gen()
        r = Btpy.random_choice(
            gg.maximum_size_arr)
        gen.set_maximum_size(int(r))
        r = Btpy.random_choice(
            gg.skin_color_arr)
        gen.set_skin_color(r)
        r = Btpy.random_choice(
            gg.eye_color_arr)
        gen.set_eye_color(r)
        r = Btpy.random_choice(
            gg.eye_type_arr)
        gen.set_eye_type(r)
        r = Btpy.random_choice(
            gg.hair_type_arr)
        gen.set_hair_type(r)
        r = Btpy.random_choice(
            gg.hair_color_arr)
        gen.set_hair_color(r)
        return gen
        