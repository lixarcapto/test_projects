


class DoitRecipeTK:

    def inner(self, regionPDT):
        terrain = regionPDT.mapMatrix[locationY][locationX]
        canProduce = True
        if(terrain.inner.getRecipeCodeInt() == 0):
            return market
        if(terrain.inner.getResourceTypeInt() == 0):
            return market
        recipe = terrain.obtainRecipe()
        resourceTypeInt = terrain.inner.getResourceTypeInt()
        if(not market.haveTheProducts(recipe.requerimentList.INNER)):
            return market
        if(recipe.extractResources):
            result = recipe.resourceExtractionList.hasTheProduct(terrain.inner.getResourceTypeInt())
            quantityConsumed = recipe.resourceExtractionList.obtainQuantityProduct(resourceTypeInt)
            if(result
            and self.hasNearbyResource([locationY, locationX], resourceTypeInt,
            quantityConsumed)):
                self.extractNearbyResource([locationY, locationX], resourceTypeInt,
                quantityConsumed)
                quantityResult = terrain.inner.getResourceQuantityInt() - quantityConsumed
                terrain.inner.setResourceQuantityInt(quantityResult)
            else:
                canProduce = False
        if(canProduce):
            market.consumeProductMatrix(recipe.requerimentList.INNER)
            market.sumProductMatrix(recipe.productionList.INNER)
        regionPDT.mapMatrix[locationY][locationX] = terrain
        map = dict()
        map["regionPDT"] = regionPDT
        map["market"] = market
        return map
