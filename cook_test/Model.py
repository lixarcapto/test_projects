

from Persistence import Persistence
from btpy.Btpy import Btpy

class Model:

    def __init__(self):
        self.recipe_nested = Persistence\
            .load_nested_dict()
        self.ingredinet_data:dict\
            = Persistence\
                .load_ingredient_data()
        self.dish_data:dict = Persistence\
            .load_dish_data()
        self.waitress_phrases = Persistence\
            .load_waitress_phrases()
        self.waitress_name = "fernanda"
        self.dish_list = Persistence\
            .get_dish_list()
        self.money:float = 10
        self.benefit:float = 2
        self.key_recipe:str = ""
        self.recipe_dict:dict = {}
        self.ingredient_list:list = []
        self.client_k_recipe:str = ""
        self.waitress_phrase_created = ""
        self.ingredient_list = list(
            self.recipe_nested["default"]\
                .keys())
        
    def get_price(self, KEY:str):
        return float(self.ingredinet_data\
            [KEY]["price"])
        
    def sum_ingredient(self, KEY:str):
        price = self.get_price(KEY)
        if(not self.money >= price):
            return None
        self.money -= price
        if(KEY in self.recipe_dict):
            self.recipe_dict[KEY] += 1
        else:
            self.recipe_dict[KEY] = 1

    def randomize_waitress(self):
        keys = list(
            self.waitress_phrases.keys())
        self.waitress_name = Btpy\
            .random_choice(keys)

    def create_customer_order(self)->str:
        txt = ""
        phrase:str = ""
        phrase_list = self.waitress_phrases\
            [self.waitress_name]\
            ["give_order"]
        phrase = Btpy.random_choice(
            phrase_list
        )
        txt += self.waitress_name + " : "
        txt += "the client ordered a "
        txt += self.client_k_recipe
        txt += ",\n " + phrase
        return txt

    def get_ingredient_text(self)->list:
        text_list:list[str] = []
        for e in self.ingredient_list:
            text_list.append(
                f"{e}(-{self.get_price(e)})"
            )
        return text_list

    def randomize_recipe(self):
        keys = self.dish_list
        key = Btpy.random_choice(keys)
        self.client_k_recipe = key
        self.randomize_waitress()
        self.waitress_phrase_created\
            = self.create_customer_order()
    
    def recete_recipe(self):
        self.randomize_recipe()
        self.key_recipe = ""
        self.clean_kitchen()

    def clean_kitchen(self):
        self.recipe_dict = {}
        for k in self.ingredient_list:
            self.recipe_dict[k] = 0

    def identify_recipe(self):
        self.key_recipe = Btpy\
            .identify_dict_number(
                self.recipe_nested,
                self.recipe_dict
            )
        
    def get_benefit(self):
        """
        Funcion que obtiene el precio
        de la receta actualmente 
        identificada
        """
        k = self.key_recipe
        dict_ = self.dish_data[k]
        return dict_["price"]
    
    def launch_achievement_detector(self):
        if(self.key_recipe 
                == self.client_k_recipe):
            benefit = self.get_benefit()
            self.money += benefit
            self.randomize_recipe()
