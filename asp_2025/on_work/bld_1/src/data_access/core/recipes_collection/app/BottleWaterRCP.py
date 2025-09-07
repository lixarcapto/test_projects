



from data_access.core.recipes_collection.RecipeEntity import RecipeEntity

class BottleWaterRCP(RecipeEntity):

    def __init__(self):
        super().__init__()
        self.key = "bottle_water"
        self.extractResources = True
        self.resourceExtractionList.addResource("resource", "aquifer-basin", 1)
        self.requerimentList.addResource("global", "vessel", 5)
        self.productionList.addResource("global", "water", 5)
        return
