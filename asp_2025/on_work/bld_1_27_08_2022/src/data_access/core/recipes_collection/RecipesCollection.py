



from data_access.core.keys_data.KeysData import KeysData
from data_access.core.recipes_collection.app.TrunksRecipe import TrunksRecipe
from data_access.core.recipes_collection.app.BoardRecipe import BoardRecipe
from data_access.core.recipes_collection.app.ToolWoodRecipe import ToolWoodRecipe
from data_access.core.recipes_collection.app.MagmaticDepositRecipe import MagmaticDepositRecipe

class RecipesCollection:

    recipesKeysMap = KeysData().getRecipesKeysMap()

    def __init__(self):
        self.inner = dict()
        self.addRecipe(TrunksRecipe())
        self.addRecipe(BoardRecipe())
        self.addRecipe(ToolWoodRecipe())
        self.addRecipe(MagmaticDepositRecipe())
        return

    def existRecipe(self, key):
        return Basic().hasTheKey(recipesKeysMap, key)

    def getRecipeByKey(self, key):
        return self.inner[key]

    def getRecipeByCode(self, codeInt):
        for e in RecipesCollection.recipesKeysMap:
            print("recipe: " + e + " " + str(codeInt))
            if(RecipesCollection.recipesKeysMap[e] == codeInt):
                return self.inner[e]

    def addRecipe(self, recipe):
        self.inner[recipe.key] = recipe
