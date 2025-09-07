

from btpy.Btpy import Btpy
import tkinter as tk
from Model import Model

class FrameIdentity:

    WIDTH_DESCRIPTION = 60

    def __init__(self, widget, model):
        self.model:Model = model
        self.frame = tk.Frame(
            widget
        )
        self.subframe = tk.Frame(
            self.frame
        )
        self.subframe.grid(
            column=0,
            row=0
        )
        self.__init_column_1()
        self.__init_column_2()
        self.__init_column_3()
        # ------------------------------
        # UPDATE DATA
        self.create_components()
        self.update_all_texts()
        self.add_listeners()
        

    def __init_column_3(self):
        
        # -----------------------------
        # PHILOSOPHY
        self.philosophy_cbox = Btpy.ComboBox(
            self.subframe, "Philosophy"
        )
        self.philosophy_cbox.grid(0, 2, "ew")
        # -----------------------------
        # WEAPON
        self.weapon_cbox = Btpy.ComboBox(
            self.subframe, "Weapon"
        )
        self.weapon_cbox.grid(1, 2, "ew")
        # -----------------------------
        # RACES
        self.races_cbox = Btpy.ComboBox(
            self.subframe, "Races"
        )
        self.races_cbox.grid(2, 2, "ew")
        # -----------------------------
        # HOBBY
        self.hobby_cbox = Btpy.ComboBox(
            self.subframe, "Hobby"
        )
        self.hobby_cbox.grid(3, 2, "ew")
        # -----------------------------
        # HATED
        self.rejections_cbox = Btpy.ComboBox(
            self.subframe, "Rejections"
        )
        self.rejections_cbox.grid(
            4, 2, "ew")
        # ------------------------------
        # AGE RANGE
        self.age_range_cbox = Btpy.ComboBox(
            self.subframe, "Age range"
        )
        self.age_range_cbox.grid(
            5, 2, "ew")
        # -----------------------------
        # YEARS OLD
        self.years_old_textf = Btpy.TextField(
            self.subframe, "Years old"
        )
        self.years_old_textf.grid(
            6, 2, "ew")
        # -----------------------------

    def __init_column_2(self):
        self.btn_random_name = Btpy.Button(
            self.subframe, "randomize"
        )
        self.btn_random_name.grid(
            0, 1, "ew")
        self.btn_random_lastname = Btpy.Button(
            self.subframe, "randomize"
        )
        self.btn_random_lastname\
            .grid(1, 1, "ew")
        # -------------------------------
        # ORIGIN COUNTRY RANDOM
        self.btn_origin_country = Btpy.Button(
            self.subframe, "randomize"
        )
        self.btn_origin_country.grid(
            4, 1, "ew")
        # -------------------------------
        # BACK STORY RANDOM
        self.btn_back_story = Btpy.Button(
            self.subframe, "randomize"
        )
        self.btn_back_story.grid(
            5, 1, "ew")
        # -------------------------------
        # YOUNG STORY RANDOM
        self.btn_young_story = Btpy.Button(
            self.subframe, "randomize"
        )
        self.btn_young_story.grid(
            6, 1, "ew")
        # -------------------------------
        # END STORY RANDOM
        self.btn_end_story = Btpy.Button(
            self.subframe, "randomize"
        )
        self.btn_end_story.grid(
            7, 1, "ew")

    def __init_column_1(self):
        # ----------------------------
        # LABEL DESCRIPTION
        self.label_desc = Btpy.Label(
            self.frame, ""
        )
        self.label_desc.widget.grid(
            column=0,
            row=1
        )
        # ------------------------------
        # NAME
        self.name_label = Btpy.TextField(
            self.subframe, "name"
        )
        self.name_label.grid(
            0, 0, "ew")
        
        # ------------------------------
        # LASTNAME  
        self.lastname_label = Btpy.TextField(
            self.subframe, "lastname"
        )
        self.lastname_label.grid(1, 0, "ew")
        
        # ------------------------------
        # GENDER
        self.gender_cbox = Btpy.ComboBox(
            self.subframe, "Gender"
        )
        self.gender_cbox.grid(2, 0, "ew")
        # ------------------------------
        # CULTURE NAME
        self.culture_name_cbox = Btpy.ComboBox(
            self.subframe, "Culture name"
        )
        self.culture_name_cbox.grid(3, 0, "ew")
        # -----------------------------
        # ORIGIN COUNTRY
        self.origin_country_cbox = Btpy.ComboBox(
            self.subframe, "Origin country"
        )
        self.origin_country_cbox.grid(4, 0, "ew")
        
        # -------------------------------
        # BACK STORY
        self.back_story_cbox = Btpy.ComboBox(
            self.subframe, "back story"
        )
        self.back_story_cbox.grid(5, 0, "ew")
        # -----------------------------
        # YOUNG STORY
        self.young_story_cbox = Btpy.ComboBox(
            self.subframe, "young story"
        )
        self.young_story_cbox.grid(
            6, 0, "ew")
        # -----------------------------
        # END STORY
        self.end_story_cbox = Btpy.ComboBox(
            self.subframe, "end story"
        )
        self.end_story_cbox.grid(
           7, 0, "ew")
        # -----------------------------
        # PROFESSION
        self.profession_cbox = Btpy.ComboBox(
            self.subframe, "Profession"
        )
        self.profession_cbox.grid(
            8, 0, "ew"
        )

    def pack(self):
        self.frame.pack()

    def add_listeners(self):
        self.btn_random_name.add_listener(
            self.randomize_name
        )
        self.btn_random_lastname.add_listener(
            self.randomize_lastname
        )
        self.gender_cbox.add_change_listener(
            self.update_gender
        )
        self.gender_cbox.add_change_listener(
            self.update_gender
        )
        self.origin_country_cbox.add_change_listener(
            self.update_origin_country
        )
        self.back_story_cbox.add_change_listener(
            self.update_back_story
        )
        self.young_story_cbox.add_change_listener(
            self.update_young_story
        )
        self.end_story_cbox.add_change_listener(
            self.update_end_story
        )
        self.culture_name_cbox.add_change_listener(
            self.update_culture_name
        )
        self.philosophy_cbox.add_change_listener(
            self.update_philosophy
        )
        self.profession_cbox.add_change_listener(
            self.update_profession
        )
        self.races_cbox.add_change_listener(
            self.update_races
        )
        self.hobby_cbox.add_change_listener(
            self.update_hobby
        )
        self.rejections_cbox.add_change_listener(
            self.update_rejections
        )
        self.weapon_cbox.add_change_listener(
            self.update_weapon
        )
        self.age_range_cbox.add_change_listener(
            self.update_age_range
        )
        self.btn_origin_country.add_listener(
            self.randomize_origin_country
        )
        self.btn_back_story.add_listener(
            self.randomize_back_story
        )
        self.btn_young_story.add_listener(
            self.randomize_young_story
        )
        self.btn_end_story.add_listener(
            self.randomize_end_story
        )
        
    def randomize_origin_country(self):
        k = self.model\
            .randomize_origin_country()
        self.origin_country_cbox\
            .set_value(k)
        self.update_origin_country_desc()

    def randomize_back_story(self):
        k = self.model\
            .randomize_back_story()
        self.back_story_cbox\
            .set_value(k)
        self.update_back_story_desc()

    def randomize_young_story(self):
        k = self.model\
            .randomize_young_story()
        self.young_story_cbox\
            .set_value(k)
        self.update_young_story_desc()

    def update_gender(self):
        k = self.gender_cbox.get_value()
        self.model.character\
            .gender_key = k

    def update_age_range(self):
        k = self.age_range_cbox.get_value()
        self.model.character\
            .age_range_key = k
        self.randomize_years_old()

    def update_origin_country(self):
        k = self.origin_country_cbox.get_value()
        self.model.character\
            .origin_country_key = k
        self.update_origin_country_desc()

    def update_back_story(self):
        k = self.back_story_cbox.get_value()
        self.model.character\
            .back_story_key = k
        self.update_back_story_desc()

    def update_culture_name(self):
        k = self.culture_name_cbox.get_value()
        self.model.culture_key = k

    def update_young_story(self):
        k = self.young_story_cbox.get_value()
        self.model.character\
            .young_story_key = k
        self.update_young_story_desc()

    def update_end_story(self):
        k = self.end_story_cbox.get_value()
        self.model.character\
            .end_story_key = k
        self.update_end_story_desc()

    def update_philosophy(self):
        k = self.philosophy_cbox.get_value()
        self.model.character\
            .philosophy_key = k
        
    def update_weapon(self):
        k = self.weapon_cbox.get_value()
        self.model.character\
            .weapon_key = k
        
    def update_profession(self):
        k = self.profession_cbox.get_value()
        self.model.character\
            .profession_key = k
        
    def update_races(self):
        k = self.races_cbox.get_value()
        self.model.character\
            .races_key = k
        
    def update_hobby(self):
        k = self.hobby_cbox.get_value()
        self.model.character\
            .hobby_key = k
    
    def update_rejections(self):
        k = self.rejections_cbox.get_value()
        self.model.character\
            .rejections_key = k

    def randomize_name(self):
        name = Btpy.random_name(
            self.model.culture_key,
            self.model.character\
                .gender_key
        )
        self.model.character.name = name
        self.name_label.set_value(name)

    def randomize_lastname(self):
        lastname = Btpy.random_lastname(
            self.model.culture_key
        )
        self.model.character\
            .lastname = lastname
        self.lastname_label.set_value(
            lastname
        )

    def randomize_years_old(self):
        years = self.model\
            .randomize_years_old()
        self.years_old_textf.set_value(
            years
        )
        self.model.character\
            .years_old = years
        
    def randomize_end_story(self):
        years = self.model\
            .randomize_end_story()
        self.end_story_cbox.set_value(
            years
        )
        self.update_end_story_desc()

    def update_origin_country_desc(self):
        k = self.model.character\
            .origin_country_key
        desc = self.model\
            .origin_country_desc_ttr\
                .translate_key(k)
        self.print_label_description(
            desc
        )

    def update_end_story_desc(self):
        k = self.model.character\
            .end_story_key
        desc = self.model\
            .end_story_desc_ttr\
                .translate_key(k)
        self.print_label_description(
            desc
        )

    def update_young_story_desc(self):
        k = self.model.character\
            .young_story_key
        desc = self.model\
            .young_story_translate\
                .translate_key(k)
        self.print_label_description(
            desc
        )

    def print_label_description(self,
            TEXT:str):
        text = TEXT.replace("\n", "")
        text = Btpy.sort_text(text, 
            FrameIdentity.WIDTH_DESCRIPTION
        )
        self.label_desc.set_title(text)


    def update_back_story_desc(self):
        k = self.model.character\
            .back_story_key
        desc = self.model\
            .back_story_translate\
                .translate_key(k)
        self.print_label_description(
            desc
        )

    def create_components(self):
        self.gender_cbox.set_components(
            self.model.get_gender_keys()
        )
        self.age_range_cbox.set_components(
            self.model.get_age_range_keys()
        )
        self.origin_country_cbox.set_components(
            self.model.get_origin_country_keys()
        )
        self.back_story_cbox.set_components(
            self.model.get_back_story_keys()
        )
        self.young_story_cbox.set_components(
            self.model.get_young_story_keys()
        )
        list_ = self.model.get_end_story_keys()
        self.end_story_cbox.set_components(
            list_
        )
        list_ = self.model.get_culture_name_keys()
        self.culture_name_cbox.set_components(
            list_
        )
        list_ = self.model.get_philosophy_keys()
        self.philosophy_cbox.set_components(
            list_
        )
        list_ = self.model\
            .profession_translate.get_keys()
        self.profession_cbox.set_components(
            list_
        )
        list_ = self.model\
            .weapon_translator.get_keys()
        self.weapon_cbox.set_components(
            list_
        )
        list_ = self.model\
            .races_translate.get_keys()
        self.races_cbox.set_components(
            list_
        )
        list_ = self.model\
            .hobby_translate.get_keys()
        self.hobby_cbox.set_components(
            list_
        )
        list_ = self.model\
            .rejections_translator.get_keys()
        self.rejections_cbox.set_components(
            list_
        )


    def update_all_texts(self):
        
        self.gender_cbox.set_content(
            self.model.get_gender_text_list()
        )
        
        self.age_range_cbox.set_content(
            self.model.get_age_range_text_list()
        )
        
        self.origin_country_cbox.set_content(
            self.model.get_origin_country_text_list()
        )
        
        self.back_story_cbox.set_content(
            self.model.get_back_story_text_list()
        )
        
        self.young_story_cbox.set_content(
            self.model.get_young_story_text_list()
        )
        
        list_ = self.model.get_end_story_text_list()
        self.end_story_cbox.set_content(
            list_
        )
        
        
        list_ = self.model.get_philosophy_text_list()
        self.philosophy_cbox.set_content(
            list_
        )
        
        list_ = self.model\
            .weapon_translator.get_text_list()
        self.weapon_cbox.set_content(
            list_
        )
        
        list_ = self.model\
            .profession_translate.get_text_list()
        self.profession_cbox.set_content(
            list_
        )
        
        list_ = self.model\
            .races_translate.get_text_list()
        self.races_cbox.set_content(
            list_
        )
        
        list_ = self.model\
            .hobby_translate.get_text_list()
        self.hobby_cbox.set_content(
            list_
        )
        
        list_ = self.model\
            .rejections_translator.get_text_list()
        self.rejections_cbox.set_content(
            list_
        )

    def load_character_dict(self, DICT):
        self.name_label.set_value(
            DICT["NAME"]
        )
        self.lastname_label.set_value(
            DICT["LASTNAME"]
        )