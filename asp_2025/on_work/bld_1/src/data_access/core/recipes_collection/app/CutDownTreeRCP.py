



from data_access.core.recipes_collection.RecipeEntity import RecipeEntity

class CutDownTreeRCP(RecipeEntity):

    def __init__(self):
        super().__init__()
        self.key = "cut_down_tree"
        self.extractResources = True
        self.resourceExtractionList.addResource("resource", "maple-forest", 1)
        self.resourceExtractionList.addResource("resource", "forest-pine", 1)
        self.resourceExtractionList.addResource("resource", "oak-forest", 1)
        self.resourceExtractionList.addResource("resource", "beech-forest", 1)
        self.resourceExtractionList.addResource("resource", "willow-forest", 1)
        #self.requerimentList.addResource("global", "tool", 1)
        self.productionList.addResource("global", "soft_trunk", 3)
        return
