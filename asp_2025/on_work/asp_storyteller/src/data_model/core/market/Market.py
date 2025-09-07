


from basic.Basic import Basic

class Market:

    def __init__(self):
        array = [
        "cow_meat",
        "chicken_meat",
        "white_fish",
        "blue_fish",
        "pig_meat",
        "softwood",
        "hardwood"
        ]
        self.productMap = Basic().createMapOfInt(array, 8)
        return

    def hasProduct(self, productKey, quantity):
        if(self.productMap[productKey] >= quantity):
            return True
        return False

    def consumeProduct(self, productKey, quantity):
        self.productMap[productKey] -= quantity
        print(productKey + ": " + str(self.productMap[productKey]))

    def writeMarketInformation(self):
        text = ""
        for e in self.productMap:
            text += e + ": " + str(self.productMap[e]) + "\n"
        return text
