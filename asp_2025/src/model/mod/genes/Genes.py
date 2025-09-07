

import random
from .genes_constant import*
from persistence.Persistence import Persistence
from .choose_probability import*
from btpy.Btpy import Btpy
from .GenesData import GenesData

from .functions.write_genes import*

class Genes:

    """
    Esta clase sirve para representar al
    conjunto de rasgos geneticos de los
    personajes que se heredan y mesclan
    entre si. Tambien contiene funciones 
    para la mescla de genes.
    """

    def __init__(self):
        self.data:GenesData = GenesData()
    
    def randomize(self):
        self.__randomize_eye_color()
        self.__randomize_eye_type()
        self.__randomize_hair_color()
        self.__randomize_hair_type()
        self.__randomize_skin_color()
        self.__randomize_height_maximum()
        self.__randomize_freckles()
        self.__randomize_albinism()
        self.__randomize_baldness()
        self.__randomize_mouth_type()
        self.__randomize_nose_type()
        self.__randomize_has_fertility()
    
    def get_regional_group_item(self):
        k = self.data\
            .get_regional_group_key()
        return self.data\
            .regional_group_depot\
                .get_item(k)

    def __randomize_height_maximum(self):
        it = self.get_regional_group_item()
        list_ = it.get_height_maximum_list()
        n = Btpy.random_choice(list_)
        self.data.set_height_maximum_key(n)

    def __randomize_freckles(self):
        it = self.get_regional_group_item()
        probability = it\
            .get_freckles_probability()
        has_freckcles = Btpy\
            .random_probability(
                int(probability)
            )
        if(has_freckcles):
            self.data.set_is_freckled(
                True
            )
        else:
            self.data.set_is_freckled(
                False
            )

    def __randomize_albinism(self):
        is_albino = Btpy\
            .random_probability(
                ALBINISM_PROBABILITY
            )
        self.data.set_is_albino(is_albino)

    def __randomize_baldness(self):
        it = self.get_regional_group_item()
        probability = it\
            .get_baldness_probability()
        is_bald = Btpy\
            .random_probability(
                int(probability)
            )
        if(is_bald):
            self.data.set_is_bald(True)
        else:
            self.data.set_is_bald(False)

    def __randomize_eye_color(self):
        it = self.get_regional_group_item()
        list_ = it.get_eye_color_list()
        n = Btpy.random_choice(list_)
        self.data.set_eye_color_key(n)
        
    def __randomize_skin_color(self):
        it = self.get_regional_group_item()
        list_ = it.get_skin_color_list()
        n = Btpy.random_choice(list_)
        self.data.set_skin_color_key(n)
        
    def __randomize_eye_type(self):
        it = self.get_regional_group_item()
        list_ = it.get_eye_type_list()
        n = Btpy.random_choice(list_)
        self.data.set_eye_type_key(n)
        
    def __randomize_hair_color(self):
        it = self.get_regional_group_item()
        list_ = it.get_hair_color_list()
        n = Btpy.random_choice(list_)
        self.data.set_hair_color_key(n)
        
    def __randomize_hair_type(self):
        it = self.get_regional_group_item()
        list_ = it.get_hair_type_list()
        n = Btpy.random_choice(list_)
        self.data.set_hair_type_key(n)

    def __randomize_nose_type(self):
        it = self.get_regional_group_item()
        list_ = it.get_nose_type_list()
        n = Btpy.random_choice(list_)
        self.data.set_nose_type_key(n)

    def __randomize_mouth_type(self):
        it = self.get_regional_group_item()
        list_ = it.get_mouth_type_list()
        n = Btpy.random_choice(list_)
        self.data.set_mouth_type_key(n)

    def __randomize_has_fertility(self):
        percent = INFERTILITY_PROBABILITY
        n = Btpy.random_probability(percent)
        self.data.set_has_infertility(n)
        
    def write(self):
        return write_genes(self.data)
    
    def __str__(self):
        return self.write()