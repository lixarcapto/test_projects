


from Recipe import Recipe

class RecipeCollection:

    def __init__(self):
        self.recipe_map = {}

    def add_recipe(self, recipe):
        self.recipe_map[recipe.name] = recipe
