

import random
from .PersonConst import PersonConst
from ..relation_list.RelationList import RelationList
from .PersonData import PersonData
from ..gen.Gen import Gen
from data_base.DataBase import DataBase
from ..stats_sum.StatsSum import StatsSum
# fx
from .svc.calcule_beauty import*
from .svc.is_boring import*
from .svc.create_facial_expression import*
from .svc.describe_appearance import*
from .svc.advance_temporal_variables import*
from .svc.manifest_the_genes import*
from .svc.random_lastname import*
from .svc.randomize import*
from .svc.write_presentation import*
from .svc.have_a_child import*
from .svc.separate_the_baby import*
from .svc.take_decision import*
from .svc.create_stat_sum_beauty import*
from .svc.advance_states import*
from .svc.define_main_emotion import*
from .svc.create_stat_sum_beauty import*

class Person:

    """
        Añadir que las personas solo son visibles en el mismo
        distrito.
    """

    def __init__(self):
        self.data = PersonData()
        self.data.code = self.create_unique_code()
        self.data.gen_own = Gen()
        PersonData.PERSON_CONST = PersonConst
        self.data.relation_list = RelationList()
        PersonData.NAMES_MALE_MAP = DataBase.load_male_names()
        PersonData.NAMES_FEMALE_MAP = DataBase.load_female_names()
        PersonData.LASTNAMES_MAP = DataBase.load_lastnames()
        PersonData.NOBLE_LASTNAMES_MAP = DataBase \
            .load_noble_lastnames()
        PersonData.AGE_RANGE_LIMIT = len(PersonData \
            .PERSON_CONST.AGE_RANGE_ARRAY) -1
        if(PersonData.BEAUTY_STAT_SUM == None):
            PersonData.BEAUTY_STAT_SUM = self.create_stat_sum_beauty()

    def create_stat_sum_beauty(self):
        return create_stat_sum_beauty()

    def calcule_beauty(self):
        return calcule_beauty(self.data)

    """
        Funcion que calcula todos los stats y variables
        que se calculan cada turno.
    """
    def calcule_other_stats(self):
        # calcula belleza
        self.data.beauty = self.calcule_beauty()


    def progress_emotion(self):
        emotion_map = self.data.emotion_states_map
        for k in emotion_map:
            if emotion_map[k] > 0: emotion_map[k] += 1
        self.data.emotion_states_map = emotion_map

    """
        Funcion que analiza si las emociones son inferiores
        a la mitad para declarar al personaje como aburrido.
    """
    # return boolean
    def is_boring(self):
        return is_boring(self.data)

    """
        Funcion para sumar puntos a una emocion
    """
    def sum_emotion(self, key, quantity = 1):
        self.data.emotion_states_map[key] += quantity

    def create_facial_expression(self):
        self.data = create_facial_expression(self.data)

    def define_main_emotion(self):
        self.data = define_main_emotion(self.data)

    def advance_emotion_states(self):
        self.progress_emotion()
        self.define_main_emotion()
        self.create_facial_expression()

    """
        Funcion que reliza una relacion sexual entre
        el personaje enviado y este personaje.
    """
    def has_sex(self, person):
        self.data = has_sex(self.data, person)

    """
        Funcion que crea un personaje bebe para
        el personaje actual, usando al personaje enviado
        como padre.
    """
    def have_a_child(self, person):
        self.data = have_a_child(self.data, person)

    def relate(self, person, quantity, type):
        self.data.relation_list.relate(
            person,
            quantity,
            type
        )

    def calcule_similitudes(self, person):
        points = 0
        p = person
        if self.data.skin_color == p.data.skin_color: points += 1
        if(self.data.age_range == p.data.age_range):
            points += 1
        if self.data.gender != p.data.gender: points += 1
        # revisa si son familia
        if (self.data.relation_list.has_relation(person.data.code)):
            relation = self.data.relation_list \
                .get_relation(person.data.code)
            if(relation.type != "family"):
                points += 1
        return points

    """
        Funcion que genera un ciudadano semi-aleatorio
        en base a la cultura asignada.
    """
    def randomize(self):
        self.data = randomize(self.data)

    # return string
    def write_presentation(self):
        return write_presentation(self.data)

    """
        Funcion que describe como texto narrativo
        exclusivamente la apariancia del personaje.
    """
    # return string
    def describe_appearance(self):
        return describe_appearance(self.data)

    """
        Funcion que avansa un dia para las variables
        temporales del personaje.
    """
    def advance_temporal_variables(self):
        self.data = advance_temporal_variables(self.data)

    def advance_states(self):
        self.data = advance_states(self.data)

    """
        Funcion que avansa el tiempo un dia para
        el personaje.
    """
    def advance_time(self):
        self.advance_temporal_variables()
        self.advance_states()
        self.take_decision()
        self.advance_emotion_states()
        self.calcule_other_stats()



    """
        Funcion que toma una decision aleatoria
        para las actividades especiales de ese dia.
    """
    def take_decision(self):
        self.data = take_decision(self.data)

    """
        Funcion que separa los bebes que pueden caminar
        de sus madres, para ser personajes independientes.
    """
    # return Person
    def separate_the_baby(self):
        return separate_the_baby(self.data)

    # return int
    def create_unique_code(self):
        code = PersonData.UNIQUE_CODE
        PersonData.UNIQUE_CODE += 1
        return code
