

from data_model.core.recipe.Recipe import Recipe

class NoneRecipe(Recipe):

    def __init__(self):
        super().__init__()
        self.inner.setKeyname("none_recipe")
        return
