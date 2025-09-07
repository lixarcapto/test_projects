



from data_model.core.recipe_collection.app.entities.NoneRecipe import NoneRecipe
from data_model.core.recipe_collection.app.entities.OakForestRecipe import OakForestRecipe

class RecipeCollection:

    def __init__(self):
        self.inner = dict()
        self.addRecipe(NoneRecipe())
        self.addRecipe(OakForestRecipe())
        return

    def addRecipe(self, recipe):
        self.inner[recipe.inner.getKeyname()] = recipe

    def getRecipe(self, recipeKey):
        return self.inner[recipeKey]
