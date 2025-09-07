


from data_model.core.resource.Resource import Resource

class ResourceForestCamp(Resource):

    def __init__(self):
        super().__init__()
        self.inner.setKeyname("forest_camp")
        self.inner.setMaterialKey("mineral")
        self.inner.setUseQuantityMaximum(100)
        self.inner.setUseQuantityMinimum(30)
        self.inner.addRecipeKeyEnabled("oak_forest_recipe")
        self.inner.setGrouthTime(70)
        self.inner.setGrouthQuantity(30)
        self.inner.setResourceClass("building")
        return
