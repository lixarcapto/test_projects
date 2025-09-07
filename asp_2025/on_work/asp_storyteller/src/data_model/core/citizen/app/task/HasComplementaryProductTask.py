


class HasComplementaryProductTask:

    """
        Retorna el numero del complentary product seleccionado,
        si no existen mas retorna -1
    """
    def inner(self, citizenPack, citizenTrigger, market):
        insufficientProducts = 0
        compProductCounter = 0
        numberCompProducts = len(citizenTrigger.complementaryProductConditionArray)
        for compProduct in citizenTrigger.complementaryProductConditionArray:
            for goods in compProduct.goodsArray:
                if(not market.hasProduct(goods["key"], goods["quantity"])):
                    insufficientProducts += 1
                    break
            for services in compProduct.servicesArray:
                if(not market.hasProduct(servicesArray["key"], servicesArray["quantity"])):
                    insufficientProducts += 1
                    break
            if(insufficientProducts == 0
            and numberCompProducts != compProductCounter):
                return compProductCounter
            compProductCounter += 1
            if(numberCompProducts == compProductCounter):
                return -1
            insufficientProducts = 0
        return compProductCounter
