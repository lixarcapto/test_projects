


from data_model.core.resource.Resource import Resource

class ResourceForestOak(Resource):

    def __init__(self):
        super().__init__()
        self.inner.setKeyname("forest_oak")
        self.inner.setMaterialKey("wood")
        self.inner.setUseQuantityMaximum(600)
        self.inner.setUseQuantityMinimum(100)
        self.inner.setGrouthTime(30)
        self.inner.setGrouthQuantity(30)
        self.inner.setResourceClass("vegetable")
        return
