



from data_access.core.recipes_collection.RecipeEntity import RecipeEntity

class Recipe11(RecipeEntity):

    def __init__(self):
        super().__init__()
        self.key = "bottle-water"
        self.extractResources = True
        self.resourceExtractionList.addResource("resource", "aquifer-basin", 1)
        self.requerimentList.addResource("global", "vessel", 5)
        self.productionList.addResource("global", "water-vessel", 5)
        return
