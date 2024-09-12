

from btpy.src.btpy.Btpy import Btpy
from .AGE_EXPRESSION import*

class Model:

    TRAITS_ROUTE = "../res/tables/traits.xlsx"
    TRANSLATE_ROUTE = "../res/tables/translate.xlsx"

    def __init__(self) -> None:
        self.translate_dict = Btpy.read_horizontal_excel(
            Model.TRANSLATE_ROUTE)
        self.traits_dict = Btpy.read_excel_dict(
            Model.TRAITS_ROUTE
        )
        self.model_message = {}
        self.character_dict = {}

    def receive(self, view_message):
        char_dict = view_message[
            "character_dict"]
        self.character_dict = char_dict

    def request(self):
        self.model_message["OPTION_DICT"]\
         = self.traits_dict
        return self.model_message
    
    def write_character(self, char_dict):
        keys_list = self.get_translate_keys(
            char_dict)
        personality_description \
            = self.translate_keys(keys_list)
        final_text = "Personality Description:\n\n"
        final_text += personality_description
        Btpy.create_docx("character_data",
            final_text)
        Btpy.load_word("character_data.docx")
        return final_text
    
    def translate_keys(self, 
        KEYS_LIST:list[str]):
        txt = ""
        key = ""
        for e in KEYS_LIST:
            if(e == "come"):
                txt += ", "
                continue
            if(e == "point"):
                txt += ". "
                continue
            if(not e in self.translate_dict["spanish"]):
                txt += f"{e} "
                continue
            key = self.translate_dict["spanish"][e]
            txt += f"{key} "
        return txt
    
    def get_age(self, AGE_KEY):
        age_range_dict = {
            "child":[7, 12],
            "teenager":[13, 17],
            "youth":[18, 21],
            "adult":[21, 30],
            "middle-aged":[31, 50],
            "elderly":[51, 90]
        }
        result = Btpy.rand_range(
            age_range_dict[AGE_KEY]
        )
        return str(result)
    
    def get_sexuality_key(self, 
            GENDER_KEY, SEXUALITY_KEY):
        if(SEXUALITY_KEY == "homosexual"):
            if(GENDER_KEY == "female"):
                return "female"
            else:
                return "male"
        if(SEXUALITY_KEY == "heterosexual"):
            if(GENDER_KEY == "female"):
                return "male"
            else:
                return "female" 
        if(SEXUALITY_KEY == "bisexual"):  
            return "male_and_female"         
        
    
    def get_translate_keys(self, char_dict):
        d = char_dict
        translate_keys = [
            "name", " : ",
            self.get_age_expression(
                d["gender"],
                d["age"]
            ), 
            "age",
            self.get_age(char_dict["age"]),
            "years",  "\n",
            "interactivity", " : ",
            d["interactivity"], "\n",
            "abstraction", " : ",
            d["abstraction"], "\n",
            "intimacy", " : ",
            d["intimacy"],  "\n",
            "activity", " : ",
            d["activity"],  "\n",
            "emotional control", " : ",
            d["emotional control"], "\n",
            "prestige", " : ",
            d["prestige"],  "\n",
            "wealth", " : ",
            d["wealth"],  "\n",
            "positivism", " : ",
            d["positivism"], "\n",
            "beauty", " : ",
            d["beauty"], "\n",
            "intelligence", " : ",
            d["intelligence"], "\n",
            "perseverance", " : ",
            d["perseverance"],  "\n",
            "violence", " : ",
            d["violence"], "\n",
            "hygiene", " : ",
            d["hygiene"], "\n",
            "gender", " : ", 
            self.get_sexuality_key(
                d["gender"],
                d["sexuality"]),  "\n",
            "profession",  " : ",
            d["profession"], "\n",
        ]
        return translate_keys
    
    def get_age_expression(self, GENDER_KEY, 
            AGE_KEY):
        if(GENDER_KEY == "female"):
            return AGE_EXPRESSION_FEMALE[
                AGE_KEY]
        return AGE_EXPRESSION_MALE[AGE_KEY]