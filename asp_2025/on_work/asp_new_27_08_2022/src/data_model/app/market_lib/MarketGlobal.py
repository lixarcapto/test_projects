

from data_access.DataAccess import DataAccess

class MarketGlobal:

    def addGoods(self, goodsProduct):
        self.goodsMatrix[goodsProduct.typeCode].append(goodsProduct)

    def getGoods(self, typeCode):
        goods = None
        goodsArray = self.goodsMatrix[typeCode]
        if(len(goodsArray) > 0):
             goods = goodsArray[0]
             del(goodsArray[0])
             return goods

    def loadQuantityOfGoods(self, matrix):
        goods = None
        goodType = 0
        quantity = 0
        for i in range(len(matrix)):
            goodType = matrix[i][0]
            quantity = matrix[i][1]
            for f in range(quantity):
                goods = DataAccess()
                goods.typeCode = goodType
                goods.lifeTimeRemaining = 100
                self.addGoods(goods)

    def __init__(self):
        self.GOODS = DataAccess().getGoodsKeysData()
        self.GOODS_INFO = [
            [self.GOODS.COW_MEAT, 6],
            [self.GOODS.HORSE_MEAT, 5],
            [self.GOODS.CHICKEN_MEAT, 3]
        ]
        self.goodsMatrix = [[]] * self.GOODS.LIMIT
        n = 0
        for e in self.goodsMatrix:
            print("goodsMatrix: " + str(n) + " = " + str(e))
            n += 1
        self.loadQuantityOfGoods(self.GOODS_INFO)

    def hasGoods(self, typeCode):
        goods = None
        goodsArray = self.goodsMatrix[typeCode]
        if(len(goodsArray) > 0):
             goods = goodsArray[0]
             if(goods.typeCode == typeCode):
                 return True
        return False
