



from data_access.core.recipes_collection.RecipeEntity import RecipeEntity

class GrindWheatRCP(RecipeEntity):

    def __init__(self):
        super().__init__()
        self.key = "grind_wheat"
        self.requerimentList.addResource("global", "wheat_grain", 1)
        self.productionList.addResource("global", "flowr", 2)
        self.productionList.addResource("global", "bran", 2)
        self.productionList.addResource("global", "semolina", 1)
        self.productionList.addResource("global", "flake", 1)
        return
