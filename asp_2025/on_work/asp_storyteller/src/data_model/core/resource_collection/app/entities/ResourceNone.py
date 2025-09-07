


from data_model.core.resource.Resource import Resource

class ResourceNone(Resource):

    def __init__(self):
        super().__init__()
        self.inner.setKeyname("none")
        self.inner.setMaterialKey("mineral")
        self.inner.setUseQuantityMaximum(100)
        self.inner.setUseQuantityMinimum(60)
        self.inner.setGrouthTime(7)
        self.inner.setGrouthQuantity(15)
        self.inner.setResourceClass("deposit")
        return
