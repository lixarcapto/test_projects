



from data_access.core.recipes_collection.RecipeEntity import RecipeEntity

class RaiseCowsRCP(RecipeEntity):

    def __init__(self):
        super().__init__()
        self.key = "raise_cows"
        self.requerimentList.addResource("global", "straw", 1)
        self.requerimentList.addResource("global", "water", 1)
        self.requerimentList.addResource("global", "basic_tool", 1)
        self.productionList.addResource("global", "cow", 2)
        return
