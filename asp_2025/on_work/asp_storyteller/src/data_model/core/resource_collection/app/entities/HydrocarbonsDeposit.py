


from data_model.core.resource.Resource import Resource

class HydrocarbonsDeposit(Resource):

    def __init__(self):
        super().__init__()
        self.inner.setKeyname("hydrocarbons_deposit")
        self.inner.setMaterialKey("oil")
        self.inner.setUseQuantityMaximum(100)
        self.inner.setUseQuantityMinimum(40)
        self.inner.setGrouthTime(7)
        self.inner.setGrouthQuantity(15)
        self.inner.setResourceClass("deposit")
        return
