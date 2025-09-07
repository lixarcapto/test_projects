



from data_access.core.recipes_collection.RecipeEntity import RecipeEntity

class ProduceAdobeRCP(RecipeEntity):

    def __init__(self):
        super().__init__()
        self.key = "produce_adobe"
        self.extractResources = True
        self.resourceExtractionList.addResource("resource", "silt", 1)
        self.requerimentList.addResource("global", "straw", 1)
        self.productionList.addResource("global", "adobe_brick", 3)
        return
