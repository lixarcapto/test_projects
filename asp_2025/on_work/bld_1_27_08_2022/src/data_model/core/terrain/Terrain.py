



from data_model.core.market.Market import Market
from data_access.DataAccess import DataAccess
from data_access.core.recipes_collection.RecipesCollection import RecipesCollection
from data_model.core.terrain.app.product.TerrainPDT import TerrainPDT

class Terrain:

    BUILDING_KEYS = DataAccess().getKeysData().getBuildingKeysMap()
    RECIPE_COLLECTION = RecipesCollection()

    def __init__(self):
        self.inner = TerrainPDT()
        return

    def canProduceRecipe(self, recipe, market):
        if(not recipe.canProduce()):
            return False
        return True

    def obtainRecipe(self):
        recipe = Terrain.RECIPE_COLLECTION.getRecipeByCode(self.inner.getRecipeCodeInt())
        return recipe

    def doitRecipe(self, market):
        recipe = self.obtainRecipe()
        if(not market.haveTheProducts(recipe.requerimentList.INNER)):
            return market
        if(recipe.extractResources):
            result = recipe.resourceExtractionList.hasTheProduct(self.inner.getResourceTypeInt())
            if(result):
                quantityConsumed = recipe.resourceExtractionList.obtainQuantityProduct(self.inner.getResourceTypeInt())
                quantityResult = self.inner.getResourceQuantityInt() - quantityConsumed
                self.inner.setResourceQuantityInt(quantityResult)
        market.consumeProductMatrix(recipe.requerimentList.INNER)
        market.sumProductMatrix(recipe.productionList.INNER)
        return market

    def advanceTime(self, market):
        if(self.inner.getBuildTypeInt() != 0):
            print("buildingType: " + str(self.inner.getBuildTypeInt()))
            market = self.doitRecipe(market)
        return market
