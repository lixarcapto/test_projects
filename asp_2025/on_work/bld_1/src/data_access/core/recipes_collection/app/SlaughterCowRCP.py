



from data_access.core.recipes_collection.RecipeEntity import RecipeEntity

class SlaughterCowRCP(RecipeEntity):

    def __init__(self):
        super().__init__()
        self.key = "slaughter_cow"
        self.requerimentList.addResource("global", "cow", 1)
        self.productionList.addResource("global", "raw-skin-bag", 1)
        self.productionList.addResource("global", "cow-meat-bag", 1)
        self.productionList.addResource("global", "premium-meat", 1)
        self.productionList.addResource("global", "poor-meat-bag", 1)
        self.productionList.addResource("global", "gut-bag", 1)
        self.productionList.addResource("global", "genitals-bag", 1)
        self.productionList.addResource("global", "gizzard-bag", 1)
        self.productionList.addResource("global", "liver-bag", 1)
        self.productionList.addResource("global", "belly-bag", 1)
        return
