

class PersonDiesTk:

    def inner(self, bodyProduct, causeOfDeath):
        bodyProduct.isDeath = True
        bodyProduct.causeOfDeath = causeOfDeath
        return bodyProduct
