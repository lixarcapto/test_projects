

from basic.Basic import Basic
from data_model.core.body.app.task.ReceivesABlowToTheHeadTk import ReceivesABlowToTheHeadTk

class BecomeUnconsciousTk:

    def inner(self, personProduct):
        receiveABlowToTheHead = ReceivesABlowToTheHeadTk()
        basic = Basic()
        if(basic.obtainBooleanWithProbability(20)):
            personProduct = receiveABlowToTheHead.inner(personProduct, 1)
        personProduct.body.isUnconscious = True
        return personProduct
