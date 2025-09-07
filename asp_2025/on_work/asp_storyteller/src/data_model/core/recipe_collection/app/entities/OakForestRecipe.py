

from data_model.core.recipe.Recipe import Recipe

class OakForestRecipe(Recipe):

    def __init__(self):
        super().__init__()
        self.inner.setKeyname("oak_forest_recipe")
        self.inner.addExtractedResources("forest_oak", 1)
        self.inner.addGoodsKeyProduced("softwood", 1)
        return
