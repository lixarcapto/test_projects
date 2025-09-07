



from data_access.core.recipes_collection.RecipeEntity import RecipeEntity

class TrunksRecipe(RecipeEntity):

    def __init__(self):
        super().__init__()
        self.key = "trunk"
        self.extractResources = True
        self.resourceExtractionList.addResource("resource", "maple-forest", 1)
        self.resourceExtractionList.addResource("resource", "pine-forest", 1)
        #self.requerimentList.addResource("global", "tool", 1)
        self.productionList.addResource("global", "trunk-bunch", 3)
        return
