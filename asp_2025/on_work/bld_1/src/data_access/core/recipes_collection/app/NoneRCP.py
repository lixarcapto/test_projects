



from data_access.core.recipes_collection.RecipeEntity import RecipeEntity

class NoneRCP(RecipeEntity):

    def __init__(self):
        super().__init__()
        self.key = "none"
        self.requerimentList.addResource("global", "soft_trunk", 1)
        self.productionList.addResource("global", "soft_board", 3)
        return
