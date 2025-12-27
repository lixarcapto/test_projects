

from Recipe import Recipe

class RecipeDict:

    def __init__(self):
        self.recipe_list = []
        self.create_recipes()

    def create_recipes(self):
        rp = Recipe()
        rp.product_dict = {
            "food":2
        }
        rp.raw_materials_dict = {
            "farmer":1
        }
        self.recipe_list.append(rp)