



from data_access.core.recipes_collection.RecipeEntity import RecipeEntity

class ToolWoodRecipe(RecipeEntity):

    def __init__(self):
        super().__init__()
        self.key = "tool-wood"
        self.requerimentList.addResource("global", "trunk-bunch", 1)
        self.productionList.addResource("global", "tool", 1)
        return
