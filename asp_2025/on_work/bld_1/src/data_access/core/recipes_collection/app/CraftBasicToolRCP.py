



from data_access.core.recipes_collection.RecipeEntity import RecipeEntity

class CraftBasicToolRCP(RecipeEntity):

    def __init__(self):
        super().__init__()
        self.key = "craft_basic_tool"
        self.requerimentList.addResource("global", "soft_trunk", 1)
        self.productionList.addResource("global", "basic_tool", 1)
        return
