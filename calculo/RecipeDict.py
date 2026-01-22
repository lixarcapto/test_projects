

from Recipe import Recipe

class RecipeDict:

    def __init__(self):
        self.recipe_list = []
        self.create_recipes()

    def create_recipes(self):
        rp = Recipe()
        rp.product_dict = {
            "food":10
        }
        rp.raw_materials_dict = {
            "farmer":1,
            "vehicles":1
        }
        self.recipe_list.append(rp)
        # ----------------------------
        rp = Recipe()
        rp.product_dict = {
            "metal":2,
            "sand":2
        }
        rp.raw_materials_dict = {
            "miner":1
        }
        self.recipe_list.append(rp)
        # ----------------------------
        rp = Recipe()
        rp.product_dict = {
            "vehicles":5
        }
        rp.raw_materials_dict = {
            "metal":1,
            "oil":1
        }
        self.recipe_list.append(rp)
        # ----------------------------
        rp = Recipe()
        rp.product_dict = {
            "concrete":2
        }
        rp.raw_materials_dict = {
            "sand":1,
            "chemical":1
        }
        self.recipe_list.append(rp)
        # ----------------------------
        rp = Recipe()
        rp.product_dict = {
            "oil":2
        }
        rp.raw_materials_dict = {
            "driller":1,
            "chemical":1
        }
        self.recipe_list.append(rp)