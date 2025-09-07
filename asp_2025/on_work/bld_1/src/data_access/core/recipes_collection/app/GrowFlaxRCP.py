



from data_access.core.recipes_collection.RecipeEntity import RecipeEntity

class GrowFlaxRCP(RecipeEntity):

    def __init__(self):
        super().__init__()
        self.key = "grow_flax"
        self.requerimentList.addResource("global", "basic_tool", 1)
        self.productionList.addResource("global", "straw", 1)
        self.productionList.addResource("global", "flax_fiber", 2)
        self.productionList.addResource("global", "flax_grain", 1)
        return
