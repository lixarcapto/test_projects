


class Recipe:

    def __init__(self, RECIPE_DICT:dict):
        self.ingredient_dict\
            :dict[str, int] = {}
        self.product_dict\
            :dict[str, int] = {}
        self.sources_dict\
            :dict[str, int] = {}
        self.convert_recipe_dict(
            RECIPE_DICT
        )
        
    def convert_recipe_dict(self, DICT):
        self.product_dict = DICT["PRODUCT"]
        self.ingredient_dict \
            = DICT["INGREDIENT"]
        self.sources_dict = DICT["SOURCES"]

    def write(self)->str:
        return "{\n"\
        + f"ingredient: {self.ingredient_dict}\n"\
        + f"product: {self.product_dict}\n"\
        + f"sources: {self.sources_dict}\n"\
        + "}" 

    def __str__(self):
        return self.write()

    def get_ingredient_dict(self):
        return self.ingredient_dict
    
    def get_product_dict(self):
        return self.product_dict
    
    def get_sources_dict(self):
        return self.sources_dict