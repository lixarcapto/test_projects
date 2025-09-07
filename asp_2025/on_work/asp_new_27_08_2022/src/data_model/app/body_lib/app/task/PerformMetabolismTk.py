

from data_model.app.body_lib.app.task.CauseGeneralDamageTk import CauseGeneralDamageTk
from data_model.app.body_lib.app.task.BecomeUnconsciousTk import BecomeUnconsciousTk
from data_model.app.body_lib.app.task.PersonDiesTk import PersonDiesTk
from data_access.DataAccess import DataAccess

class PerformMetabolismTk:

    def inner(self, bodyProduct):
        causeGeneralDamage = CauseGeneralDamageTk()
        becomeUnconscious = BecomeUnconsciousTk()
        personDies = PersonDiesTk()
        personValues = DataAccess().getBodyValuesData()
        if(bodyProduct.isPregnant):
            bodyProduct.pregnantTime += 1
        if(bodyProduct.isDeath):
            bodyProduct.deadDays += 1
        if(bodyProduct.carbohydrateReserve >= 1):
            bodyProduct.carbohydrateReserve -= 1
        elif(bodyProduct.fatReserve >= 1):
            bodyProduct.fatReserve -= 1
            bodyProduct.hasHunger = True
        else:
            bodyProduct = causeGeneralDamage.inner(bodyProduct)
            bodyProduct.hasHunger = True
        if(bodyProduct.amountOfBloodToDie <= personValues.BLOOD_TO_COMA):
            bodyProduct.isInACome = True
            bodyProduct = becomeUnconscious.inner(bodyProduct)
        #causas de muerte
        if(bodyProduct.circulatorySystemState == 0):
            bodyProduct = personDies.inner(bodyProduct, "paro cardiaco")
        if(bodyProduct.nervousSystemState == 0):
            bodyProduct = personDies.inner(bodyProduct, "daño nervioso")
        if(bodyProduct.brainState == 0):
            bodyProduct = personDies.inner(bodyProduct, "daño cerebral")
        if(bodyProduct.amountOfBloodToDie == personValues.BLOOD_MINIMUM_TO_LIVE):
            bodyProduct = personDies.inner(bodyProduct, "desangramiento")
        if(bodyProduct.respiratorySystemState == 0):
            bodyProduct = personDies.inner(bodyProduct, "fallo respiratorio")
        if(bodyProduct.endocrineSystemState == 0):
            None
        #excretorFunction
        if(bodyProduct.excretorySystemState == 3):
            bodyProduct.urineAccumulation = 0
        elif(bodyProduct.excretorySystemState == 2
        and bodyProduct.urineAccumulation >= 8):
            bodyProduct.urineAccumulation -= 8
        elif(bodyProduct.excretorySystemState == 3
        and bodyProduct.urineAccumulation >= 5):
            bodyProduct.urineAccumulation -= 5
        #lowerDigestiveFunction
        if(bodyProduct.lowerDigestiveSystemState == 3):
            bodyProduct.wasteAccumulation = 0
        elif(bodyProduct.lowerDigestiveSystemState == 2
        and bodyProduct.wasteAccumulation >= 8):
            bodyProduct.wasteAccumulation -= 8
        elif(bodyProduct.lowerDigestiveSystemState == 3
        and bodyProduct.wasteAccumulation >= 5):
            bodyProduct.wasteAccumulation -= 5
        if(bodyProduct.muscularSystemState == 0):
            bodyProduct = personDies.inner(bodyProduct, "daño muscular")
        return bodyProduct
