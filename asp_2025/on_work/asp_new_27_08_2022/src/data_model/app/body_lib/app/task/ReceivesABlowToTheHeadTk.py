

from basic.Basic import Basic


class ReceivesABlowToTheHeadTk:

    def inner(self, personProduct, forceInt):
        basic = Basic()
        if(forceInt >= 1):
            if(basic.obtainBooleanWithProbability(50)):
                if(personProduct.body.internalTissueHealth > 0):
                    personProduct.body.internalTissueHealth -= 1
            if(basic.obtainBooleanWithProbability(30)):
                if(personProduct.body.brainState > 0):
                    if(personProduct.body.internalTissueHealth > 0):
                        personProduct.body.brainState -= 1
        return personProduct
