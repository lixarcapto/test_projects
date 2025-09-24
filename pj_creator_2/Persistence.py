
from btpy.Btpy import Btpy

class Persistence:

    res_path:str = "./res/"
    xlsx_path:str = "xlsx/"

    def get_xlsx_path():
        return Persistence.res_path\
            + Persistence.xlsx_path

    def load_gender_translate():
        f_name = Persistence.get_xlsx_path() \
            + "gender_translate"\
            + ".xlsx"
        return \
            Btpy.read_xlsx_nested_dict_row(
                f_name
            )
    
    def load_age_range_translate():
        f_name = Persistence.get_xlsx_path() \
            + "age_range_translate"\
            + ".xlsx"
        return \
            Btpy.read_xlsx_nested_dict_row(
                f_name
            )
    
    def load_origin_country_translate():
        f_name = Persistence.get_xlsx_path() \
            + "origin_country_translate"\
            + ".xlsx"
        return \
            Btpy.read_xlsx_nested_dict_row(
                f_name
            )
    
    def load_orientation_translate():
        f_name = Persistence.get_xlsx_path() \
            + "orientation"\
            + ".xlsx"
        return \
            Btpy.read_xlsx_nested_dict_row(
                f_name
            )
    
    def load_back_story_translate():
        f_name = Persistence.get_xlsx_path() \
            + "back_story"\
            + ".xlsx"
        return \
            Btpy.read_xlsx_nested_dict_row(
                f_name
            )

    def load_young_story_translate():
        f_name = Persistence.get_xlsx_path() \
            + "young_story"\
            + ".xlsx"
        return \
            Btpy.read_xlsx_nested_dict_row(
                f_name
            )
    
    def load_end_story_translate():
        f_name = Persistence.get_xlsx_path() \
            + "end_story"\
            + ".xlsx"
        return \
            Btpy.read_xlsx_nested_dict_row(
                f_name
            )
    
    def load_philosophy_translate():
        f_name = Persistence.get_xlsx_path() \
            + "philosophy"\
            + ".xlsx"
        return \
            Btpy.read_xlsx_nested_dict_row(
                f_name
            )
    
    def load_races_translate():
        f_name = Persistence.get_xlsx_path() \
            + "races_translate"\
            + ".xlsx"
        return \
            Btpy.read_xlsx_nested_dict_row(
                f_name
            )
    
    def load_hobby_translate():
        f_name = Persistence.get_xlsx_path() \
            + "interest_translate"\
            + ".xlsx"
        return \
            Btpy.read_xlsx_nested_dict_row(
                f_name
            )
    
    def load_rejections_translate():
        f_name = Persistence.get_xlsx_path() \
            + "rejections_translate"\
            + ".xlsx"
        return \
            Btpy.read_xlsx_nested_dict_row(
                f_name
            )
    
    def load_weapon_translate():
        f_name = Persistence.get_xlsx_path() \
            + "weapon_translate"\
            + ".xlsx"
        return \
            Btpy.read_xlsx_nested_dict_row(
                f_name
            )
    
    def load_profession_translate():
        f_name = Persistence.get_xlsx_path() \
            + "profession"\
            + ".xlsx"
        return \
            Btpy.read_xlsx_nested_dict_row(
                f_name
            )
    
    def load_origin_country_desc():
        f_name = Persistence.get_xlsx_path() \
            + "origin_country_description"\
            + ".xlsx"
        return \
            Btpy.read_xlsx_nested_dict_row(
                f_name
            )
    
    def load_back_story_desc():
        f_name = Persistence.get_xlsx_path() \
            + "back_story_description"\
            + ".xlsx"
        return \
            Btpy.read_xlsx_nested_dict_row(
                f_name
            )
    
    def load_skill_translate():
        f_name = Persistence.get_xlsx_path() \
            + "skill_translate"\
            + ".xlsx"
        return \
            Btpy.read_xlsx_nested_dict_row(
                f_name
            )

    def load_young_story_desc():
        f_name = Persistence.get_xlsx_path() \
            + "young_story_description"\
            + ".xlsx"
        return \
            Btpy.read_xlsx_nested_dict_row(
                f_name
            )
    
    def load_traits_keys_translate():
        f_name = Persistence.get_xlsx_path() \
            + "traits_keys"\
            + ".xlsx"
        return \
            Btpy.read_xlsx_nested_dict_row(
                f_name
            )
    
    def load_age_range_dict():
        return Btpy.read_json_object(
            Persistence.res_path\
            + "json/" \
            + "age_range_dict.json"
        )
    
    def load_personality_tropes():
        dict_ = Btpy.read_xlsx_nested_dict_row(
            Persistence.get_xlsx_path()\
            + "personality_trope_data.xlsx"
        )
        return dict_
    
    def load_skin_dict():
        dict_ = Btpy.read_xlsx_nested_dict_row(
            Persistence.get_xlsx_path()\
            + "skin_translate.xlsx"
        )
        return dict_
    
    def load_traits_desc_dict():
        dict_ = Btpy.read_xlsx_nested_dict_row(
            Persistence.get_xlsx_path()\
            + "traits_description.xlsx"
        )
        return dict_
    
    def load_end_story_desc_translate():
        dict_ = Btpy.read_xlsx_nested_dict_row(
            Persistence.get_xlsx_path()\
            + "end_story_description.xlsx"
        )
        return dict_

    
