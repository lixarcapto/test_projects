


from btpy.Btpy import Btpy
from Persistence import Persistence
from Character import Character
from Translator import Translator
from traits_const import TRAITS_DICT

class Model:

    gender_translate = {}
    gender_keys = [
        "male",
        "female"
    ]
    lenguage_keys = [
        "english",
        "spanish",
        "portuguese"
    ]
    traits_dict:dict = TRAITS_DICT
    culture_name_keys = [
        "russian",
        "american", 
        "english",
        "arab",
        "french",
        "afrikan",
        "nordic",
        "indian",
        "spanish",
        "turkish",
        "chinese",
        "japanese",
        "polinesian",
        "italic",
        "slavic",
        "hebrew"
    ]
    age_range_translate = {}
    origin_country_translate = {}
    young_story_translate = {}
    back_story_translate = {}
    end_story_translate = {}
    philosophy_translate = {}
    weapon_translator = {}
    hobby_translate = {}
    races_translate = {}
    profession_translate = {}
    races_desc_translator = None
    origin_country_desc_ttr = {}
    end_story_desc_ttr = {}
    age_range_dict = {}
    traits_keys_ttr = None
    skill_translator = None
    exp_back_story_ttr = None
    exp_young_story_dict = None
    exp_origin_country_dict = None
    rejections_translator = {}
    personality_trope_dict = None
    skin_translator = {}
    hair_color_translator = {}
    hair_style_translator = {}
    traits_desc_translator = {}
    orientation_translator = {}

    def __init__(self):
        self.experiences_selected = ""
        self.lenguage_key = "english"
        self.culture_key:str = "english"
        self.load_data()
        self.character = Character()
        self.init_default_character()

    def set_lenguage_key(self, KEY:str):
        self.lenguage_key = KEY
        Translator.lenguage_key = KEY

    def randomize_years_old(self):
        key = self.character\
            .age_range_key
        range_ = Model.age_range_dict[key]
        return Btpy.rand_range(range_)

    
    # ---------------------------------
    # RANDOMIZER 

    def randomize_experiences(self):
        r_list = []
        list_ = self.exp_back_story_ttr\
            .get_keys()
        r_list = r_list + self\
            .random_choice_uniques(list_)
        return r_list
    
    def random_choice_uniques(self, 
            LIST):
        list_idx = Btpy.random_uniques(
            4,
            [0, len(LIST) -1]
        )
        list_r = []
        for idx in list_idx:
            list_r.append(LIST[idx])
        return list_r
    
    def randomize_origin_country(self):
        list_ = self\
            .get_origin_country_keys()
        e = Btpy.random_choice(list_)
        self.character\
            .origin_country_key = e
        return e
    
    def randomize_back_story(self):
        list_ = self\
            .get_back_story_keys()
        e = Btpy.random_choice(list_)
        self.character\
            .back_story_key = e
        return e
    
    def randomize_young_story(self):
        list_ = self\
            .get_young_story_keys()
        e = Btpy.random_choice(list_)
        self.character\
            .young_story_key = e
        return e
    
    def randomize_end_story(self):
        list_ = self\
            .get_end_story_keys()
        e = Btpy.random_choice(list_)
        self.character\
            .end_story_key = e
        return e
    
    def randomize_profession(self):
        list_ = self\
            .get_profession_keys()
        e = Btpy.random_choice(list_)
        self.character\
            .profession_key = e
        return e
    
    def randomize_philosophy(self):
        list_ = self\
            .get_philosophy_keys()
        e = Btpy.random_choice(list_)
        self.character\
            .philosophy_key = e
        return e
    
    # ---------------------------------

    def init_default_character(self):
        self.character\
            .gender_key = self\
                .get_gender_keys()[0]
        self.character\
            .age_range_key = self\
                .get_age_range_keys()[0]
        self.character\
            .origin_country_key\
                 = self.get_origin_country_keys()[0]
        self.character\
            .back_story_key = self.get_back_story_keys()[0]
        self.character\
            .young_story_key = self.get_young_story_keys()[0]
        self.character\
            .end_story_key = self.get_end_story_keys()[0]
        self.character\
            .philosophy_key = self.get_philosophy_keys()[0]
        self.character\
            .weapon_key = self.weapon_translator.get_keys()[0]
        self.character\
            .hobby_key = self.hobby_translate.get_keys()[0]
        self.character\
            .races_key = self.races_translate.get_keys()[0]
        self.character\
            .profession_key = self.profession_translate.get_keys()[0]
        self.character\
            .rejections_key = self.rejections_translator.get_keys()[0]
        self.culture_key = self.get_culture_name_keys()[0]

    def load_data(self):
        self.load_gender_translate()
        self.load_age_range_translate()
        self.load_origin_country_translate()
        self.load_young_story_translate()
        self.load_back_story_translate()
        self.load_end_story_translate()
        self.load_philosophy_translate()
        self.load_weapon_translate()
        self.load_origin_country_desc_tt()
        self.load_profession_translate()
        self.load_phrases_translate()
        self.load_races_translate()
        self.load_back_story_desc_tt()
        self.load_young_story_desc_tt()
        self.load_age_range_dict()
        self.load_traits_translator()
        self.load_skill_translate()
        self.load_lenguage_key()
        self.load_rejections_translator()
        self.load_personality_trope_dict()
        self.load_skin_translator()
        self.load_end_story_desc_tt()
        self.load_traits_desc_translator()
        self.load_orientation_translator()
        self.load_races_desc_translator()
        self.load_hair_color_translator()
        self.load_hair_style_translator()

    def save_lenguage_key(self):
        dict_ = {
            "LENGUAGE_KEY": self.lenguage_key
        }
        Btpy.write_json_object(
            "./config.json",
            dict_
        )

    # ---------------------------------------
    # LOAD DATA



    def load_lenguage_key(self):
        dict_ = Btpy.read_json_object(
            "./config.json"
        )
        self.lenguage_key\
            = dict_["LENGUAGE_KEY"]
        Translator.lenguage_key \
            = dict_["LENGUAGE_KEY"]

    def load_age_range_dict(self):
        dict_ = Persistence\
            .load_age_range_dict()
        Model.age_range_dict= dict_

    def load_traits_desc_translator(self):
        dict_ = Persistence\
            .load_traits_desc_dict()
        Model.traits_desc_translator \
            = Translator(dict_)
        
    def load_races_desc_translator(self):
        dict_ = Persistence\
            .load_races_description()
        Model.races_desc_translator \
            = Translator(dict_)

    def load_weapon_translate(self):
        dict_ = Persistence\
            .load_weapon_translate()
        Model.weapon_translator \
            = Translator(dict_)
        
    def load_skill_translate(self):
        dict_ = Persistence\
            .load_skill_translate()
        Model.skill_translator \
            = Translator(dict_)
        
    def load_traits_translator(self):
        dict_ = Persistence\
            .load_traits_keys_translate()
        Model.traits_keys_ttr \
            = Translator(dict_)
        
    def load_personality_trope_dict(self):
        dict_ = Persistence\
            .load_personality_tropes()
        Model.personality_trope_dict \
            = dict_
        
    def load_rejections_translator(self):
        dict_ = Persistence\
            .load_rejections_translate()
        Model.rejections_translator \
            = Translator(dict_)
        
    def load_skin_translator(self):
        dict_ = Persistence\
            .load_skin_dict()
        Model.skin_translator \
            = Translator(dict_)
        
    def load_hair_color_translator(self):
        dict_ = Persistence\
            .load_hair_color_dict()
        Model.hair_color_translator \
            = Translator(dict_)
        
    def load_hair_style_translator(self):
        dict_ = Persistence\
            .load_hair_style_dict()
        Model.hair_style_translator \
            = Translator(dict_)
        
    def load_orientation_translator(self):
        dict_ = Persistence\
            .load_orientation_translate()
        Model.orientation_translator \
            = Translator(dict_)
        
    def load_profession_translate(self):
        dict_ = Persistence\
            .load_profession_translate()
        Model.profession_translate \
            = Translator(dict_)
        
    def load_races_translate(self):
        dict_ = Persistence\
            .load_races_translate()
        Model.races_translate \
            = Translator(dict_)
        
    def load_phrases_translate(self):
        dict_ = Persistence\
            .load_hobby_translate()
        Model.hobby_translate \
            = Translator(dict_)
        
    def load_origin_country_desc_tt(self):
        dict_ = Persistence\
            .load_origin_country_desc()
        self.origin_country_desc_ttr \
            = Translator(dict_)
        
    def load_back_story_desc_tt(self):
        dict_ = Persistence\
            .load_back_story_desc()
        self.back_story_translate \
            = Translator(dict_)
        
    def load_young_story_desc_tt(self):
        dict_ = Persistence\
            .load_young_story_desc()
        self.young_story_translate \
            = Translator(dict_)
        
    def load_end_story_desc_tt(self):
        dict_ = Persistence\
            .load_end_story_desc_translate()
        self.end_story_desc_ttr \
            = Translator(dict_)

    def load_philosophy_translate(self):
        Model.philosophy_translate\
            = Persistence\
                .load_philosophy_translate()

    def load_gender_translate(self):
        Model.gender_translate\
            = Persistence\
                .load_gender_translate()

    def load_age_range_translate(self):
        Model.age_range_translate\
            = Persistence\
                .load_age_range_translate()

    def load_origin_country_translate(self):
        Model.origin_country_translate\
            = Persistence\
                .load_origin_country_translate()
        
    def load_back_story_translate(self):
        Model.back_story_translate\
            = Persistence\
                .load_back_story_translate()
        
    def load_young_story_translate(self):
        Model.young_story_translate\
            = Persistence\
                .load_young_story_translate()
        
    def load_end_story_translate(self):
        Model.end_story_translate\
            = Persistence\
                .load_end_story_translate()

    # ---------------------------------
    # GET KEYS
    
    def get_gender_keys(self):
        return Model.gender_keys
    
    def get_culture_name_keys(self):
        return Model.culture_name_keys
    
    def get_age_range_keys(self):
        return list(
                Model.age_range_translate\
                    .keys()
            )
    
    def get_origin_country_keys(self):
        return list(
                Model.origin_country_translate\
                    .keys()
            )
    
    def get_back_story_keys(self):
        return list(
                Model.back_story_translate\
                    .keys()
            )
    
    def get_young_story_keys(self):
        return list(
                Model.young_story_translate\
                    .keys()
            )
    
    def get_end_story_keys(self):
        return list(
                Model.end_story_translate\
                    .keys()
            )
    
    def get_philosophy_keys(self):
        return list(
                Model.philosophy_translate\
                    .keys()
            )
    
    def get_profession_keys(self):
        return list(
                Model.profession_translate\
                    .get_keys()
            )
    
    def get_weapon_keys(self):
        return list(
                Model.weapon_translator\
                    .keys()
            )
    
    def get_phrases_keys(self):
        return list(
                Model.hobby_translate\
                    .keys()
            )
    
    def get_races_keys(self):
        return list(
                Model.races_translate\
                    .keys()
            )
    
    def get_personality_tropes_keys(self):
        print(list(Model.personality_trope_dict.keys()))
        return list(Model.personality_trope_dict.keys())

    # -------------------------------------
    # TRANSLATE KEYS 
    
    def translate_gender_key(self, 
            KEY:str):
        return Model.gender_translate\
            [KEY][self.lenguage_key]
    
    def translate_age_range_key(self, 
            KEY:str):
        return Model.age_range_translate\
            [KEY][self.lenguage_key]
    
    def translate_origin_country_key(self, 
            KEY:str):
        return Model.origin_country_translate\
            [KEY][self.lenguage_key]
    
    def translate_back_story_key(self, 
            KEY:str):
        return Model.back_story_translate\
            [KEY][self.lenguage_key]
    
    def translate_young_story_key(self, 
            KEY:str):
        return Model.young_story_translate\
            [KEY][self.lenguage_key]
    
    def translate_end_story_key(self, 
            KEY:str):
        return Model.end_story_translate\
            [KEY][self.lenguage_key]
    
    def translate_philosophy_key(self, 
            KEY:str):
        return Model.philosophy_translate\
            [KEY][self.lenguage_key]
    
    def translate_weapon_key(self, 
            KEY:str):
        return Model.weapon_translator\
            .translate_key(KEY)
    
    def translate_races_key(self, 
            KEY:str):
        return Model.races_translate\
            .translate_key(KEY)
    
    def translate_phrases_key(self, 
            KEY:str):
        return Model.hobby_translate\
            [KEY][self.lenguage_key]
    
    def translate_profession_key(self, 
            KEY:str):
        return Model.profession_translate\
            .translate_key(KEY)
    
    def get_origin_country_desc_text(self):
        k = self.character\
            .origin_country_key
        return self\
            .origin_country_desc_ttr\
                .translate_key(k)
        
    def get_back_story_desc_text(self):
        k = self.character\
            .back_story_key
        return self\
            .back_story_translate\
                .translate_key(k)
    
    def get_end_story_desc_text(self):
        k = self.character\
            .end_story_key
        return self\
            .end_story_translate\
            [k][self.lenguage_key]
    
    def get_young_story_desc_text(self):
        k = self.character\
            .young_story_key
        return self\
            .young_story_translate\
                .translate_key(k)

    # ------------------------------------
    # GET TEXT LIST

    def get_age_range_text_list(self):
        list_ = []
        text = ""
        for k in Model.age_range_translate:
            text = Model.age_range_translate\
                    [k][self.lenguage_key]
            list_.append(text)
        return list_
    
    def get_gender_text_list(self):
        list_ = []
        text = ""
        for k in Model.gender_keys:
            text = self\
                .translate_gender_key(k)
            list_.append(text)
        return list_
    
    def get_origin_country_text_list(self):
        list_ = []
        text = ""
        for k in Model.origin_country_translate:
            text = self\
                .translate_origin_country_key(k)
            list_.append(text)
        return list_
    
    def get_back_story_text_list(self):
        list_ = []
        text = ""
        for k in Model.back_story_translate:
            text = self\
                .translate_back_story_key(k)
            list_.append(text)
        return list_
    
    def get_young_story_text_list(self):
        list_ = []
        text = ""
        for k in Model.young_story_translate:
            text = self\
                .translate_young_story_key(k)
            list_.append(text)
        return list_
    
    def get_end_story_text_list(self):
        list_ = []
        text = ""
        for k in Model.end_story_translate:
            text = self\
                .translate_end_story_key(k)
            list_.append(text)
        return list_
    
    def get_philosophy_text_list(self):
        list_ = []
        text = ""
        for k in Model.philosophy_translate:
            text = self\
                .translate_philosophy_key(k)
            list_.append(text)
        return list_
    
    # -------------------------------------

    def write_traits(self):
        dict_ = self.character\
            .traits_dict
        v = 0
        k_trait = ""
        trait_list = []
        for k in dict_:
            v = dict_[k]
            k_trait = Model.traits_dict\
                [k][str(v)]
            if(k_trait == ""): continue
            trait_list.append(k_trait)
        return Btpy.write_as_description(
                trait_list, "and"
            )
    
    def write_traits_descriptions(self):
        dict_ = self.character\
            .traits_dict
        v = 0
        k_trait = ""
        trait_list = []
        txt_desc = ""
        f_txt = ""
        for k in dict_:
            v = dict_[k]
            k_trait = Model.traits_dict\
                [k][str(v)]
            if(k_trait == ""): continue
            txt_desc = self\
                .traits_desc_translator\
                    .translate_key(k_trait)
            f_txt = f"{k_trait} : {txt_desc}"
            trait_list.append(f_txt)
        txt = Btpy.write_as_list(
            trait_list,
            ""
        )
        return txt
    
    def write_skills(self):
        list_ = self.character.skills_list
        return Btpy.write_as_description(
                list_, "and"
            )
    
    def write_experiences(self):
        list_ = self.character.experiences_list
        return Btpy.write_as_description(
                list_, "and"
            )

    def write_back_story(self):
        char = self.character
        k = char.back_story_key
        back_story = self\
            .translate_back_story_key(k)
        back_story_desc = self\
            .get_back_story_desc_text()
        return f"{back_story} ; "\
            + back_story_desc

    
    def write_young_story(self):
        char = self.character
        k = char.young_story_key
        young_story = self\
            .translate_young_story_key(k)
        young_story_desc = self\
            .get_young_story_desc_text()
        return f"{young_story} ; "\
            + young_story_desc
    
    def write_origin_country(self):
        char = self.character
        k = char.origin_country_key
        country_story = self\
            .translate_origin_country_key(k)
        country_story_desc = self\
            .get_origin_country_desc_text()
        return f"{country_story} ; "\
            + country_story_desc
    
    def write_end_story(self):
        char = self.character
        k = char.end_story_key
        country_story = self\
            .translate_end_story_key(k)
        country_story_desc = self\
            .get_end_story_desc_text()
        return f"{country_story} ; "\
            + country_story_desc
    
    def write_races(self):
        char = self.character
        races_k = char.races_key
        races_text = self\
            .translate_races_key(races_k)
        description = self.races_desc_translator\
            .translate_key(races_k)
        return f"{races_text} ; "\
            + description
    
    def write_appearance_desc(self):
        txt = ""
        txt += self.character.races_key + " "
        txt += self.character.gender_key + " "
        txt += "with "
        txt += self.character.skin_color + " " 
        txt += "skin, "
        txt += self.character.hair_color + " " 
        txt += "hair, "
        txt += self.character.hair_style + " "
        txt += "cut hair "
        return txt

    def write_character(self):
        char = self.character
        gender_tt = self.translate_gender_key(
            self.character.gender_key
        )
        age_range_tt = self.translate_age_range_key(
            self.character.age_range_key
        )
        weapon_tt = self.translate_weapon_key(
            char.weapon_key)
        race_tt = self.translate_races_key(
            char.races_key
        )
        hobby_tt = self.hobby_translate\
            .translate_key(char.hobby_key)
        rejections_key = self.rejections_translator\
            .translate_key(char.rejections_key)
        profession_key = self.translate_profession_key(
            char.profession_key)
        philosophy_key = self.translate_philosophy_key(
            char.philosophy_key)
        txt = ""
        txt += f"Name : {char.name}\n"
        txt += f"Lastname : {char.lastname}\n"
        txt += f"Gender : {gender_tt}\n"
        txt += f"Age range : {age_range_tt}\n"
        txt += f"Years old : {char.years_old}\n"
        txt += f"Origin country : {self.write_origin_country()}\n"
        txt += f"Back story : {self.write_back_story()}\n"
        txt += f"Young story : {self.write_young_story()}\n"
        txt += f"End story : {self.write_end_story()}\n"
        txt += f"Weapon : {weapon_tt}\n"
        txt += f"Races : {self.write_races()}\n"
        txt += f"Hobby : {hobby_tt}\n"
        txt += f"Rejections : {rejections_key}\n"
        txt += f"Profession : {profession_key}\n"
        txt += f"Philosophy : {philosophy_key}\n"
        txt += f"Traits : {self.write_traits()}\n"
        txt += f"Skills : {self.write_skills()}\n"
        txt += f"Traits definition: {self.write_traits_descriptions()}\n"
        txt += f"Appearance : {self.write_appearance_desc()}"
        return txt
    
    def get_pronoun(self):
        gender_k = self.character\
            .gender_key
        if(gender_k == "female"):
            return "she"
        return "he"
    
    def get_gender_alt(self):
        gender_k = self.character\
            .gender_key
        if(gender_k == "female"):
            return "woman"
        return "man"
    
    def write_full_name(self):
        return self.character.name\
            + "_" \
            + self.character.lastname
    
    def save_as_docx(self):
        txt = self.write_character()
        root_path = Btpy.find_main_path()
        name_file = self\
            .write_full_name()
        full_path = root_path\
            + "/saves/" \
            + name_file + ".docx"
        Btpy.write_docx(
            "./saves/" + name_file,
            txt
        )
        Btpy.open_docx(full_path)