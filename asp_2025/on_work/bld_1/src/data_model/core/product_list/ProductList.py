

from data_access.DataAccess import DataAccess

class ProductList:

    def __init__(self):
        self.productArray = []
        return

    def addProduct(self, location, productKey, quantity):
        array = [None] * 3
        array[0] = location
        array[1] = DataAccess().getKeysData().getMarketGlobalIndex(productKey)
        array[2] = quantity
        self.productArray.append(array)
