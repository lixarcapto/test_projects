



from data_access.core.recipes_collection.RecipeEntity import RecipeEntity

class MineSedimentaryDepositRCP(RecipeEntity):

    def __init__(self):
        super().__init__()
        self.key = "mine_sedimentary_deposit"
        self.extractResources = True
        self.resourceExtractionList.addResource("resource", "alluvial-deposit", 1)
        self.resourceExtractionList.addResource("resource", "alluvial-deposit", 1)
        #self.requerimentList.addResource("global", "tool", 1)
        self.productionList.addResource("global", "gold_nuggets", 1)
        self.productionList.addResource("global", "cassiterite", 1)
        self.productionList.addResource("global", "black_sand", 2)
        return
