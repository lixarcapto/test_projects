



from data_access.core.recipes_collection.RecipeEntity import RecipeEntity

class CarveTrunkForBoardRCP(RecipeEntity):

    def __init__(self):
        super().__init__()
        self.key = "carve_trunk_for_board"
        self.requerimentList.addResource("global", "soft_trunk", 1)
        self.productionList.addResource("global", "soft_board", 3)
        return
