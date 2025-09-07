


class ComplementaryProduct:

    def __init__(self):
        self.keyName = ""
        self.goodsArray = []
        self.servicesArray = []
        return

    def addGoods(self, keyName, quantity):
        map = dict()
        map["key"] = keyName
        map["quantity"] = quantity
        self.goodsArray.append(map)

    def addServices(self, keyName, quantity):
        map = dict()
        map["key"] = keyName
        map["quantity"] = quantity
        self.servicesArray.append(map)
