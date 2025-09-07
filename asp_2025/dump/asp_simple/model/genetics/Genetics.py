

from ..gen.Gen import Gen
from ..genetic_group.GGFactory import GGFactory
from btpy.src.btpy.Btpy import Btpy

class Genetics:

    """
    Clase que agrupa todos los modulos
    relacionados a la genetica de los
    personajes.
    """

    GG_FACTORY = GGFactory()

    def __init__(self):
        self.father_gen = None
        self.mother_gen = None
        self.own_gen = None

    def randomize_ancestors(self, 
            ggroup_key:str):
        # randomize genes
        self.mother_gen = self.GG_FACTORY\
            .create_gen(ggroup_key)
        self.father_gen = self.GG_FACTORY\
            .create_gen(ggroup_key)
        
    def mix_genes(self):
        """
        Mescla los genes del padre y la madre
        para crear los genes del hijo
        """
        c:Gen = Gen()
        a:Gen = self.mother_gen
        b:Gen = self.father_gen
        # maximum_size
        result = Btpy.random_choice(
            [a.get_maximum_size(), 
             b.get_maximum_size()]
        )
        c.set_maximum_size(result)
        #self.__skin_color:str = ""
        result = Btpy.random_choice(
            [a.get_skin_color(), 
             b.get_skin_color()]
        )
        c.set_skin_color(result)
        #self.__eye_color:str = ""
        result = Btpy.random_choice(
            [a.get_eye_color(), 
             b.get_eye_color()]
        )
        c.set_eye_color(result)
        #self.__eye_type:str = ""
        result = Btpy.random_choice(
            [a.get_eye_type(), 
             b.get_eye_type()]
        )
        c.set_eye_type(result)
        #self.__hair_type:str = ""
        result = Btpy.random_choice(
            [a.get_hair_type(), 
             b.get_hair_type()]
        )
        c.set_hair_type(result)
        #self.__hair_color:str = ""
        result = Btpy.random_choice(
            [a.get_hair_color(), 
             b.get_hair_color()]
        )
        c.set_hair_color(result)
        self.mother_gen = a
        self.father_gen = b
        self.own_gen = c