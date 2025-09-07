


from btpy.Btpy import Btpy

from persistence.Persistence import Persistence
from ...mod.date_asp.DateAsp import DateAsp
from ..genes.Genes import Genes
from .functions.combine_genes import*
from ..genes.genes_constant import*
from .mod.relationship.Relationship import Relationship
from .in_deps import*
from .random_probability_float import*
from ..passport.Passport import Passport

class Citizen:


    def __init__(self):
        self.data:CitizenData \
            = CitizenData()
        # CALLS ---------------------------
        self.__create_unique_number()
        self.__load_static_data()
        self.__init_objects()
        # ---------------------------------
            
    def __load_age_range_data(self):
        if(CitizenData.age_range_data_dict
                == None):
            CitizenData.age_range_data_dict \
                = Persistence\
                    .read_age_range_dict()
            CitizenData.age_range_list_dict\
                = self.get_age_range_list_dict()
            print(CitizenData.age_range_data_dict)

    def __load_static_data(self):
        self.__load_age_range_data()

    def __init_objects(self):
        self.data.genes_dad = Genes()
        self.data.genes_mom = Genes()
        self.data.genes_self = Genes()
        self.data.date_asp = DateAsp()
        self.data.relation = Relationship()

    # -------------------------------------
    # PUBLIC ACCESSORS --------------------
    
    def get_full_name(self)->str:
        return get_full_name(self.data)

    def get_is_inside(self)->bool:
        """
        Funcion que retorna verdadero
        si el ciudadano esta dentro de 
        casa o un edificio.
        """
        return self.data.get_is_inside()
    
    def set_actual_region_point(self,
            POINT:list[int]):
        self.data.set_actual_region_point(
            POINT)
    
    def get_actual_region_point(self)\
            ->list[int]:
        return self.data\
            .get_actual_region_point()

    def set_origin_region_point(self,
            POINT:list[int]):
        self.data.set_origin_region_point(
            POINT)

    def get_origin_region_point(self)\
            ->list[int]:
        return self.data\
            .get_origin_region_point()
    
    def get_eye_color_detail(self)->str:
        n = self.data.get_eye_color_number()
        detail = EYE_COLOR_DETAIL_TUPLE[n]
        return detail
    
    def get_hair_color_detail(self)->str:
        n = self.data.get_hair_color_number()
        detail = HAIR_COLOR_DETAIL_TUPLE[n]
        return detail
    
    def get_hair_color_number(self)->int:
        return HAIR_COLOR_K_TUPLE.index(
            self.hair_color_actual
        )
    
    def get_eye_color_number(self)->int:
        self.data.get_eye_color_key()
    
    def set_culture_key(self, CULTURE:str):
        self.data.set_culture_key(CULTURE)

    def get_culture_key(self)->str:
        return self.data.get_culture_key()
    
    def get_age_range_key(self)->str:
        return self.data.get_age_range_key()

    def set_age_range_key(self, KEY:str):
        self.data.set_age_range_key(KEY)
    
    def get_gender_key(self)->str:
        return self.data.get_gender_key()

    def set_gender_key(self, GENDER:str):
        self.data.set_gender_key(GENDER)

    def get_id_number(self)->int:
        return self.data.get_id_number()
    
    # ------------------------------------
    # GET LAYOUTS -------------------------

    def execute_probabilistic_events(self):
        self.data \
            = execute_probabilistic_events(
                self.data
            )

    def cause_character_death(self,
            CAUSE_DEATH_KEY:str)->None:
        self.data.set_is_dead(True)
        self.data.set_cause_death_key(
            CAUSE_DEATH_KEY
        )

    def get_player_path_layout(self)\
                ->list[str]:
        """
        Funcion que renderiza el ciudadano
        como una lista de claves de 
        imagenes para traducir en la 
        vista en rutas de imagenes 
        reales.
        """
        return get_player_path_layout(
            self.data
        )     

    # -------------------------------------
    
    def reset_needs(self)->None:
        self.data.set_have_food(False)
        self.data.set_have_water(False)
        self.data.set_have_house(False)
        self.data.set_have_clothes(False)
        self.data.set_have_transportation(
            False)
        self.data.set_have_jov(False)

    def get_passport(self)->Passport:
        ppt = Passport()
        ppt.culture_number = self\
            .data.get_culture_key()
        ppt.full_name = self.get_full_name()
        ppt.profession = self.data\
            .get_profession_key()
        ppt.id_number = self.data\
            .get_id_number()
        return ppt

    def produce_work(self, market):
        k_profession = self.data\
            .get_profession_key().upper()
        market.sum_product(
            k_profession, 1
        )
        return market
    
    def execute(self):
        self.cause_character_death(
            "unknown"
        )
    
    def consume_market(self, market)\
            ->any:
        market = self.produce_work(market)
        if(market.has_quantity("FOOD", 1)):
            market.sum_product("FOOD", -1)
            self.data.set_have_food(True)
        if(market.has_quantity("WATER", 1)):
            market.sum_product("WATER", -1)
            self.data.set_have_water(True)
        if(market.has_quantity("FABRICS", 1)):
            market.sum_product("FABRICS", -1)
            self.data.set_have_clothes(True)
        if(market.has_quantity("HOUSES", 1)):
            market.sum_product("HOUSES", -1)
            self.data.set_have_house(True)
        return market
    
    def update_vital_needs(self):
        if(not self.data.get_have_food()):
            self.data = cause_character_death(
                self.data,
                "starvation"
            )
        if(not self.data.get_have_water()):
            self.data = cause_character_death(
                self.data,
                "dehydration"
            )
    
    def get_age_range_nickname(self):
        """
        Funcion que identifica y retorna
        el nickname del rango de edad
        del personaje segun su genero.
        """
        return get_age_range_nickname(
            self.data
        )
    
    def write_presentation(self)->str:
        return write_presentation(
            self.data
        )
    
    def get_api_request(self)->str:
        return create_description_for_image_ai(
            self.data
        )
    
    def __descripe_appearance(self)->str:
        return descripe_appearance(
            self.data
        )

    def write(self)->str:
        text = ""
        text += self.write_biography()
        text += "\n"
        text += self.write_presentation()
        text += "\n"
        text += self.__descripe_appearance()
        text += "\n"
        text += self.describe_culture()
        text += "\n"
        text += "RELATIONS:\n\n"
        text += self.write_relations()
        text += "\n"
        return text
    

    
    def write_relations(self):
        txt = ""
        dict_ = self.data.relation\
            .get_relation_dict()
        for k in dict_:
            txt += " > "\
            + dict_[k].passport.write()\
            + ".\n"
        return txt
    
    def describe_culture(self):
        text = self.data\
            .get_personal_pronoun() + " "
        text += select_archetype_description(
            self.data
        )
        return text

    # -------------------------------------
    # PUBLIC MUTATTORS --------------------

    def create_genes_zygote(self,
            dad_citizen):
        return create_genes_zygote(
            self.data, 
            dad_citizen
        )

    def __reproduce(self, citizen_dad):
        self.data = reproduce(
            self.data, 
            citizen_dad,
            Citizen
        )

    def create_child(self, citizen_dad):
        return create_child(
            self.data, 
            citizen_dad,
            Citizen()
        )

    def give_birth(self):
        self.data.set_is_pregnant(False)
        self.data.set_is_giving_birth(False)
        self.data.set_is_a_mother(True)

    def time_to_let_go_children(self)\
            ->bool:
        """
        Si el child_in_care
        almacenado por un citizen 
        is_mother tiene el age_range_key
        como "teenager" retorna verdadero
        y si no retorna falso. Si el 
        citizen no is_mother retorna 
        falso tambien.
        """
        if(not self.data.get_is_a_mother()):
            return False
        age_range_key = self.data\
            .child_in_care_list[0]\
                .data.get_age_range_key()
        if(age_range_key == "teenager"):
            return True 
        return False

    def let_go_children(self):
        child_list = self.data\
            .child_in_care_list
        self.data.child_in_care_list = []
        self.data.set_is_a_mother(False)
        return child_list
    
    def __update_children_time(self, 
                market, is_pay_day,
                postcard):
        if(self.data.get_is_a_mother()):
            leng = len(self.data\
                .child_in_care_list)
            e = None
            for i in range(leng):
                e = self.data\
                    .child_in_care_list[i]
                market = e.advance_one_month(
                    market,
                    is_pay_day,
                    postcard
                )
                self.data\
                    .child_in_care_list[i]\
                        = e
        return market
            
    def __manifest_genetic_traits(self):
        self.data = manifest_genetic_traits(
            self.data)

    def apply_cultural_traits(self):
        self.apply_cultural_style()
        self.randomize_archetype()
        self.apply_cultural_mustache()
        self.apply_cultural_beard_style()

    def randomize_archetype(self):
        list_ = list(PERSONALITY_KEY_TUPLE)
        k = Btpy.random_choice(list_)
        self.data.set_archetype_key(k)

    def apply_cultural_style(self):
        self.data = apply_cultural_hair_style(
            self.data)

    def __update_hair(self):
        """
        Funcion que realiza una 
        actualizacion continua de la 
        apariencia y comportamientos 
        relacionados con el cabello.
        """
        self.apply_baldness()
        self.apply_gray_hair()
        self.__update_beard_style()

    def __update_beard_style(self):
        age_k = self.data.get_age_range_key()
        if(not age_k == "adult"
        and not age_k == "elderly"
        and not age_k == "dying"):
            return None
        beard_k = self.data\
            .get_beard_style_key()
        self.data.set_current_beard_style(
            beard_k
        )
        mustache_k = self.data\
            .get_makeup_key()
        self.data.set_current_makeup_key(
            mustache_k
        )

    def apply_cultural_mustache(self):
        gender = self.data.get_gender_key()
        item = self.data\
            .get_cultural_group_item()
        list_ = []
        if(gender == "female"):
            list_ = item\
                .get_makeup_female_list()
        elif(gender == "male"):
            list_ = item\
                .get_makeup_male_list()
        k_result = Btpy.random_choice(
            list_)
        self.data.set_makeup_key(
            k_result
        )

    def apply_cultural_beard_style(self):
        gender = self.data.get_gender_key()
        item = self.data\
            .get_cultural_group_item()
        list_ = []
        if(gender == "female"):
            list_ = item\
                .get_beard_style_female_list()
        elif(gender == "male"):
            list_ = item\
                .get_beard_style_male_list()
        k_result = Btpy.random_choice(
            list_)
        self.data.set_beard_style_key(
            k_result
        )

    def apply_baldness(self):
        # -------------------------------
        # detecta si tiene genes 
        # de calvicie manifestados
        has_bald_gens = self.data\
            .get_is_bald()
        # --------------------------------
        # Detecta si es hombre
        gender_k = self.data\
            .get_gender_key()
        is_male = (gender_k == "male")
        # -----------------------------
        # obtiene la probabilidad de 
        # calvicie.
        item_range = self.data\
            .get_age_range_item()
        baldness_prob = item_range\
            .get_baldness_probability()
        # -----------------------------
        # filtra si es mujer y si no
        # tiene genes de calvicie.
        if(not has_bald_gens): return None
        if(not is_male): return None
        # -------------------------------
        is_bald = random_probability_float(
            baldness_prob
        )
        self.data.set_hairstyle_key(
            "bald"
        )

    def apply_gray_hair(self):
        item_range = self.data\
            .get_age_range_item()
        gray_hair_prob = item_range\
            .get_gray_hair_probability()
        # si esta en el rango de edad
        # de gray_hair realiza una tirada
        # de azar.
        has_gray_hair \
            = random_probability_float(
                    gray_hair_prob
            )
        if(has_gray_hair):
            self.data.set_hair_color_key(
                "white")

    def __have_sex(self, citizen):
        gender_list:list = []
        gender_k = citizen.data\
            .get_gender_key()
        gender_list.append(gender_k)
        gender_k = self.data\
            .get_gender_key()
        gender_list.append(gender_k)
        if("female" in gender_list
        and "male" in gender_list):
            if(self.data.get_gender_key() 
                        != "female"):
                return citizen
            fertility = self.data\
                .get_age_range_item()\
                    .get_fertility()
            was_pregnant:bool\
                = random_probability_float(
                    fertility
                )
            if(was_pregnant):
                self.__reproduce(citizen)
        return citizen

    def socialize(self, citizen)->any:
        self.data.relation.set_relation(
            citizen.get_id_number(),
            "DISTANT",
            5,
            "NONE",
            citizen.get_passport()
        )
        citizen.data.relation.set_relation(
            self.get_id_number(),
            "DISTANT",
            5,
            "NONE",
            citizen.get_passport()
        )
        citizen = self.__have_sex(citizen)
        return citizen

    def update_pregnant_time(self):
        self.data = update_pregnant_time(
            self.data
        )

    def update_profession(self):
        age_range = self.data\
            .get_age_range_key()
        if(age_range in 
           ["adult", "elderly", "dying"]
        and self.data.get_profession_key() 
                    == "TRAINEE"):
            self.__randomize_profession()

    def buy_monthly_at_the_market(self, 
            market):
        is_pay_day = True
        market = self.consume_market(
            market
        )
        return market

    def advance_one_month(self, market,
            is_pay_day, postcard):
        self.data.actual_postcard\
            = postcard
        self.reset_needs()
        if(market != None):
            market = self\
                .buy_monthly_at_the_market(
                    market
                )
        for i in range(3):
            self.data.date_asp\
                .advance_one_day()
        self.update_height()
        self.update_age_range()    
        self.update_fertility()
        self.update_pregnant_time() 
        self.update_age_behaviors()
        self.__update_hair()
        self.update_profession()
        self.update_cultural_behaviors()
        self.execute_probabilistic_events()
        self.update_mood_points()
        self.update_vital_needs()
        self.update_biography()
        market = self\
            .__update_children_time(
                market,
                is_pay_day,
                postcard
        )
        return market
    
    def advance_one_day_for_childs(self,
            market, is_pay_day, postcard):
        market = self\
            .__update_children_time(
                market,
                is_pay_day,
                postcard
            )
        return market
    
    def update_cultural_behaviors(self):
        k = self.data.get_culture_key()
        gender = self.data\
            .get_gender_key()
        if(k == "desert_guards"
        and gender == "female"):
            self.data.set_hide_hair(True)
        else:
            self.data.set_hide_hair(False)

    def get_height_actual_key(self):
        self.data.get_height_actual_key()
    
    def get_height_maximum_key(self):
        self.data.genes_self\
            .get_height_maximum_key()
    
    def set_height_maximum_key(self, 
                KEY:str):
        self.data.genes_self\
            .set_height_maximum_key()
        
    def get_eye_color_key(self):
        return self.genes_self\
            .get_eye_color_key()
    
    def get_eye_type_key(self):
        return self.data.get_eye_type_key()
    
    def get_skin_color_key(self):
        return self.data\
            .get_skin_color_key()
    
    def get_hair_type_key(self):
        return self.genes_self\
            .data.get_hair_type_key()
    
    def get_hair_color_key(self):
        return self.data\
            .get_hair_color_key()
    
    def get_age_range_list_dict(self)->dict:
        """
        Esta funcion obtiene un diccionario
        reducido solo con los rangos de 
        cada rango de edad; sirve para 
        detectar el rango de edad mas 
        facil.
        """
        new_dict = {}
        for k in CitizenData\
                .age_range_data_dict:
            new_dict[k] = CitizenData\
                .age_range_data_dict[k][
                    "range_list"
                ]
        return new_dict

    def update_age_range(self):
        self.data = update_age_range(
            self.data
        )

    def update_age_behaviors(self):
        self.data = update_age_behaviors(
            self.data
        )

    def update_fertility(self):
        self.data = update_fertility(
            self.data
        )
        
    def update_height(self):
        self.data = update_height(
            self.data
        )
            
    """
    TODO: actualizar a partir de aqui.
    """

    def randomize_legendary(self, 
            CULTURE_KEY:str,
            GENDER:str,
            postcard):
        """
        Esta funcion crea un personaje
        aleatorio legendario; estos son
        personajes que son los primeros
        del mapa y nesesitan una 
        generacion aleatoria diferente
        ya que no funcionan mediante 
        herencia.
        """
        self.data.set_culture_key(
            CULTURE_KEY)
        self.data.set_is_legendary(True)
        self.__randomize_regional_group()
        self.data.set_gender_key(GENDER)
        self.data = randomize_names(
            self.data
        )
        self.data.origin_postcard\
            = postcard
        self.data.actual_postcard\
            = postcard
        self.__randomize_age_range()
        self.__randomize_genes()
        self.__manifest_genetic_traits()
        self.apply_cultural_traits()
        self.update_biography()

    def __randomize_age_range(self):
        """
        Randomiza una edad entre el 
        rango de años de un adult.
        """
        range_list = self.data\
            .age_range_depot\
                .get_age_range("adult")\
                    .get_range_list()
        years = Btpy.rand_range(range_list)
        self.data.date_asp.set_year(years)
        self.update_age_range()

    def __randomize_regional_group(self):
        self.data = randomize_regional_group(
            self.data
        )

    def __randomize_genes(self):
       self.data = randomize_genes(
           self.data
        )

    def __randomize_profession(self):
        self.data = randomize_profession(
            self.data
        )

    def __randomize_gender(self):
        self.data = randomize_gender(
            self.data
        )

    def get_key_names(self):
        return self.data.get_key_names()
    
    def update_mood_points(self):
        points = 0
        if(self.data.get_have_food()):
            points += 1
        if(self.data.get_have_water()):
            points += 1
        self.data.set_mood_points(points)
        percent = Btpy.percent_from_part(
            self.data.get_mood_points(),
            CitizenData.MOOD_POINTS_MAX
        )
        key = Btpy.whats_range(
            MOOD_DICT_RANGE,
            percent
        )
        self.data.set_mood_value_key(
            key[0])
    
    # --------------------------------------
    # GENERADORES DE CLAVES

    # --------------------------------------
    # RANDOMIZAR BIOGRAFIA

    def write_biography(self):
        personal = self.data\
            .get_personal_pronoun()
        possesive = self.data\
            .get_possessive_pronoun()
        terrain_k = self.data\
                .origin_postcard\
                    .terrain_type_key
        txt = ""\
        + personal + " lived "\
        + possesive + " early years "\
        + self.get_activity_text() + " "\
        + "in " + terrain_k
        return txt
    
    def get_activity_text(self):
        k = self.data\
            .childrens_activities_code
        return CHILDRENS_ACTIVITIES_DICT[k]

    def update_biography(self):
        if(not self.data\
                .childhood_overcome):
            self.data\
                .childhood_overcome = True
            terrain_k = self.data\
                .origin_postcard\
                    .terrain_type_key
            list_ = TERRAIN_TYPE_ACTIVITIES_DICT\
                [terrain_k]
            activity_k = Btpy.random_choice(
                list_
            )
            self.data.childrens_activities_code\
                = activity_k

    # --------------------------------------
    # PRIVATE ------------------------------

    def __create_unique_number(self):
        id_ = CitizenData\
            .last_unique_number
        self.data.set_id_number(id_)
        CitizenData.last_unique_number += 1
