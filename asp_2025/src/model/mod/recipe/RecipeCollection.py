

from .Recipe import Recipe
from persistence.Persistence import Persistence

class RecipeCollection:

    def __init__(self):
        self.recipe_dict:dict[Recipe] = {}
        self.load_json_recipes()

    def load_json_recipes(self):
        nested_dict = Persistence\
            .read_recipe_nested_dict()
        for k in nested_dict:
            self.add_recipe(
                k,
                nested_dict[k]
            )

    def get_recipe(self, KEY:str)->Recipe:
        return self.recipe_dict[KEY]

    def add_recipe(self, KEY:str, DICT):
        recipe = Recipe(DICT)
        self.recipe_dict[KEY] = recipe