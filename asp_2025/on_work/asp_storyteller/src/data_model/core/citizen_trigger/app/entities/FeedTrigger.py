


from data_model.core.citizen_trigger.CitizenTrigger import CitizenTrigger

class FeedTrigger(CitizenTrigger):

    def __init__(self):
        super().__init__()
        self.setKeyName("feed")
        self._satisfactionKey = "fed_up"
        self._dissatisfactionKey = "hungry"
        compleProduct = self.createComplementaryProduct("chicken_meat")
        compleProduct.addGoods("chicken_meat", 1)
        self.addComplementaryProduct(compleProduct)
        compleProduct = self.createComplementaryProduct("cow_meat")
        compleProduct.addGoods("cow_meat", 1)
        self.addComplementaryProduct(compleProduct)
        self.addAttributeEffect("feed", 1, 0)
        self.setCategory("need")
