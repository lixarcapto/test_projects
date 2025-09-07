



from data_access.core.recipes_collection.RecipeEntity import RecipeEntity

class GrowWheatFarmRCP(RecipeEntity):

    def __init__(self):
        super().__init__()
        self.key = "grow_wheat_farm"
        self.requerimentList.addResource("global", "basic_tool", 1)
        self.productionList.addResource("global", "straw", 2)
        self.productionList.addResource("global", "wheat_grain", 1)
        return
