


class CauseGeneralDamageTk:

    def inner(self, bodyProduct):
        if(bodyProduct.circulatorySystemState >= 1):
            bodyProduct.circulatorySystemState -= 1
        if(bodyProduct.higherDigestiveSystemState >= 1):
            bodyProduct.higherDigestiveSystemState -= 1
        if(bodyProduct.nervousSystemState >= 1):
            bodyProduct.nervousSystemState -= 1
        if(bodyProduct.brainState >= 1):
            bodyProduct.brainState -= 1
        if(bodyProduct.respiratorySystemState >= 1):
            bodyProduct.respiratorySystemState -= 1
        if(bodyProduct.endocrineSystemState >= 1):
            bodyProduct.endocrineSystemState -= 1
        if(bodyProduct.excretorySystemState >= 1):
            bodyProduct.excretorySystemState -= 1
        if(bodyProduct.lowerDigestiveSystemState >= 1):
            bodyProduct.lowerDigestiveSystemState -= 1
        if(bodyProduct.visionState >= 1):
            bodyProduct.visionState -= 1
        if(bodyProduct.legsState >= 1):
            bodyProduct.legsState -= 1
        if(bodyProduct.armState >= 1):
            bodyProduct.armState -= 1
        if(bodyProduct.auditionState >= 1):
            bodyProduct.auditionState -= 1
        if(bodyProduct.muscularSystemState >= 1):
            bodyProduct.muscularSystemState -= 1
        return bodyProduct
