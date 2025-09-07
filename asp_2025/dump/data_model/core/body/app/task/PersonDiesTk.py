

class PersonDiesTk:

    def inner(self, bodyProduct, causeOfDeath):
        bodyProduct.setIsDeath(True)
        bodyProduct._causeOfDeath = causeOfDeath
        return bodyProduct
