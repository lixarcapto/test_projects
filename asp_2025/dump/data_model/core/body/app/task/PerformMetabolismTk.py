

from data_model.core.body.app.task.CauseGeneralDamageTk import CauseGeneralDamageTk
from data_model.core.body.app.task.BecomeUnconsciousTk import BecomeUnconsciousTk
from data_model.core.body.app.task.PersonDiesTk import PersonDiesTk
from data_access.DataAccess import DataAccess

class PerformMetabolismTk:

    """
        Realiza el consumo de alimentos y otros metabolismos, cada uno
        debe estar separado en su metodo propio.
    """


    def produceEnergy(self, bodyPDT):
        #producir alimentos
        if(bodyPDT._glucoseInBloodReserve >= 1
        and bodyPDT._proteinReserve >= 1
        and bodyPDT._saltReserve >= 1
        and bodyPDT._waterReserve >= 1):
            bodyPDT._glucoseInBloodReserve -= 1
            bodyPDT._proteinReserve -= 1
            bodyPDT._saltReserve -= 1
            bodyPDT._waterReserve -= 1
            bodyPDT._bodyTemperature += 1
            bodyPDT._energyReserve += 1
            bodyPDT._qiReserve += 1
            #conume vitaminas
            if(bodyPDT._vitaminReserve >= 1):
                bodyPDT._vitaminReserve += 1
            else:
                bodyPDT._lackOfVitamin
            #consume minerales
            if(bodyPDT._mineralsReserve >= 1):
                bodyPDT._mineralsReserve += 1
            else:
                bodyPDT._lackOfMineral
        return bodyPDT

    def produceGlucose(self, bodyPDT):
        #producir glucosa
        if(bodyPDT._carbohydrateReserve >= 1):
            bodyPDT._carbohydrateReserve -= 1
            bodyPDT._glucoseInBloodReserve += 1
        elif(bodyPDT._fatReserve >= 1):
            bodyPDT._fatReserve -= 1
            bodyPDT._glucoseInBloodReserve += 1)
        else:
            bodyPDT._itIsHungry = True
        return bodyPDT

    def excretoryFunction(self, bodyPDT):
        #excretorFunction
        if(bodyPDT.excretorySystemState == 3):
            bodyPDT.urineAccumulation = 0
        elif(bodyPDT.excretorySystemState == 2
        and bodyPDT.urineAccumulation >= 8):
            bodyPDT.urineAccumulation -= 8
        elif(bodyPDT.excretorySystemState == 3
        and bodyPDT.urineAccumulation >= 5):
            bodyPDT.urineAccumulation -= 5
        #lowerDigestiveFunction
        if(bodyPDT.lowerDigestiveSystemState == 3):
            bodyPDT.wasteAccumulation = 0
        elif(bodyPDT.lowerDigestiveSystemState == 2
        and bodyPDT.wasteAccumulation >= 8):
            bodyPDT.wasteAccumulation -= 8
        elif(bodyPDT.lowerDigestiveSystemState == 3
        and bodyPDT.wasteAccumulation >= 5):
            bodyPDT.wasteAccumulation -= 5
        return bodyPDT

    def applySicknessEffect(self, bodyPDT):
        causeGeneralDamage = CauseGeneralDamageTk()
        becomeUnconscious = BecomeUnconsciousTk()
        personDies = PersonDiesTk()
        #
        if(bodyPDT._isPregnant):
            bodyPDT._pregnantTime += 1
        if(bodyPDT._isDeath):
            bodyPDT._deadDays += 1
        if(bodyPDT._itIsHungry):
            bodyPDT.causeGeneralDamage(causeGeneralDamage)
        if(bodyPDT.amountOfBloodToDie <= personValues.BLOOD_TO_COMA):
            bodyPDT.isInACome = True
            bodyPDT = becomeUnconscious.inner(bodyPDT)
        #causas de muerte
        if(bodyPDT.circulatorySystemState == 0):
            bodyPDT = personDies.inner(bodyPDT, "paro cardiaco")
        if(bodyPDT.nervousSystemState == 0):
            bodyPDT = personDies.inner(bodyPDT, "daño nervioso")
        if(bodyPDT.brainState == 0):
            bodyPDT = personDies.inner(bodyPDT, "daño cerebral")
        if(bodyPDT.amountOfBloodToDie == personValues.BLOOD_MINIMUM_TO_LIVE):
            bodyPDT = personDies.inner(bodyPDT, "desangramiento")
        if(bodyPDT.respiratorySystemState == 0):
            bodyPDT = personDies.inner(bodyPDT, "fallo respiratorio")
        if(bodyPDT.endocrineSystemState == 0):
            None

    def inner(self, bodyPDT):
        personValues = DataAccess().getBodyValuesData()
        #
        bodyPDT = self.produceGlucose(bodyPDT)
        bodyPDT = self.excretorFunction(bodyPDT)
        bodyPDT = self.produceEnergy(bodyPDT)
        bodyPDT = self.applySicknessEffect(bodyPDT)
        return bodyPDT
