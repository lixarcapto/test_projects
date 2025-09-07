

from data_model.core.market.core.product.Product import Product

class EatProductTk:

    def inner(self, bodyProduct, product):
        if(bodyProduct.higherDigestiveSystemState >= 1):
            if(product == Product.COW_MEAT):
                bodyProduct.proteinReserve += 2
                bodyProduct.fatReserve += 1
            if(product == Product.PIG_MEAT):
                bodyProduct.proteinReserve += 1
                bodyProduct.fatReserve += 2
            if(product == Product.CHICKEN_MEAT):
                bodyProduct.proteinReserve += 2
            if(product == Product.TURKEY_MEAT):
                bodyProduct.proteinReserve += 3
            if(product == Product.WILD_MEAT):
                bodyProduct.proteinReserve += 3
                bodyProduct.fatReserve += 1
            if(product == Product.EXOTIC_MEAT):
                bodyProduct.proteinReserve += 2
                bodyProduct.fatReserve += 2
        return personProduct
