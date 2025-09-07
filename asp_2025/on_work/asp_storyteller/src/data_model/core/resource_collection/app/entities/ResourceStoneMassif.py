


from data_model.core.resource.Resource import Resource

class ResourceStoneMassif(Resource):

    def __init__(self):
        super().__init__()
        self.inner.setKeyname("stone_massif")
        self.inner.setMaterialKey("mineral")
        self.inner.setUseQuantityMaximum(100)
        self.inner.setUseQuantityMinimum(70)
        self.inner.setGrouthTime(30)
        self.inner.setGrouthQuantity(30)
        self.inner.setResourceClass("deposit")
        return
