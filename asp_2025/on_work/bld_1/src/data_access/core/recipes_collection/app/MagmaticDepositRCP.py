


from data_access.core.recipes_collection.RecipeEntity import RecipeEntity

class MagmaticDepositRCP(RecipeEntity):

    def __init__(self):
        super().__init__()
        self.key = "magmatic_deposit"
        self.extractResources = True
        self.resourceExtractionList.addResource("resource", "magmatic-deposit", 1)
        #self.requerimentList.addResource("global", "tool", 1)
        self.productionList.addResource("global", "chalcopyrite", 1)
        self.productionList.addResource("global", "semi-precious-stones-bag", 1)
        self.productionList.addResource("global", "pyrite", 3)
        return
