



from data_access.core.recipes_collection.RecipeEntity import RecipeEntity

class BoardRecipe(RecipeEntity):

    def __init__(self):
        super().__init__()
        self.key = "board"
        self.requerimentList.addResource("global", "trunk-bunch", 1)
        self.productionList.addResource("global", "board-bunch", 3)
        return
