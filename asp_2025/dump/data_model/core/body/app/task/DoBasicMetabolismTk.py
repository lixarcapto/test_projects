


from data_model.core.body.app.task.CauseGeneralDamageTk import CauseGeneralDamageTk
from data_model.core.body.app.task.BecomeUnconsciousTk import BecomeUnconsciousTk
from data_model.core.body.app.task.PersonDiesTk import PersonDiesTk
from data_access.DataAccess import DataAccess

class DoBasicMetabolismTk:

    """
        Realiza el consumo de alimentos y otros metabolismos, cada uno
        debe estar separado en su metodo propio.
        Una funcion escaneara el estado del cuerpo desencadenando estados
        y emitiendo sensaciones interiores, estas tienen sus propia clave.
    """

    INNER_SENSATION_ARRAY = [
        "hambre",
        "sed",
        "picazon",
        "dolor de estomago",
        "dolor de cabeza",
        "dolor de intestino"
    ]

    def produceEnergy(self, bodyPDT):
        #producir alimentos
        if(not bodyPDT.systemMap["circulatory"].isWorking()):
            return bodyPDT
        if(bodyPDT._glucoseInBloodReserve >= 1):
            bodyPDT._glucoseInBloodReserve -= 1
            bodyPDT._bodyTemperature += 1
            bodyPDT._energyReserve = bodyPDT._redBloodCellsReserve
            bodyPDT._qiReserve += 10
        return bodyPDT

    def produceGlucose(self, bodyPDT):
        if(not bodyPDT.systemMap["middle_digestive"].isWorking()):
            return bodyPDT
        #producir glucosa
        if(bodyPDT._carbohydrateReserve >= 1):
            bodyPDT._carbohydrateReserve -= 1
            bodyPDT._glucoseInBloodReserve += 1
        elif(bodyPDT._fatReserve >= 1):
            bodyPDT._fatReserve -= 1
            bodyPDT._glucoseInBloodReserve += 1
        return bodyPDT

    def feedTheBody(self, bodyPDT):
        if(not bodyPDT.systemMap["nervous"].isWorking()):
            return bodyPDT
        if(bodyPDT._glucoseInBloodReserve >= 1
        and bodyPDT._proteinReserve >= 1
        and bodyPDT._saltReserve >= 1
        and bodyPDT._waterReserve >= 1):
            bodyPDT._proteinReserve -= 1
            bodyPDT._saltReserve -= 1
            bodyPDT._waterReserve -= 1
            bodyPDT._glucoseInBloodReserve -= 1
            bodyPDT._whiteBloodCellsReserve += 1
            bodyPDT._redBloodCellsReserve += 1
            bodyPDT._stemCellsReserve += 1
            if(not bodyPDT._lackOfVitamin):
                bodyPDT._plateletsReserve += 1
            bodyPDT._bloodReserve += 10
        return bodyPDT

    def excretoryFunction(self, bodyPDT):
        #excretorFunction
        if(bodyPDT._excretorySystemState == 3):
            bodyPDT._urineAccumulation = 0
        elif(bodyPDT._excretorySystemState == 2
        and bodyPDT._urineAccumulation >= 8):
            bodyPDT._urineAccumulation -= 8
        elif(bodyPDT._excretorySystemState == 3
        and bodyPDT._urineAccumulation >= 5):
            bodyPDT._urineAccumulation -= 5
        #lowerDigestiveFunction
        if(bodyPDT._lowerDigestiveSystemState == 3):
            bodyPDT._wasteAccumulation = 0
        elif(bodyPDT._lowerDigestiveSystemState == 2
        and bodyPDT._wasteAccumulation >= 8):
            bodyPDT._wasteAccumulation -= 8
        elif(bodyPDT._lowerDigestiveSystemState == 3
        and bodyPDT._wasteAccumulation >= 5):
            bodyPDT._wasteAccumulation -= 5
        return bodyPDT

    def applySicknessEffect(self, bodyPDT):
        personValues = DataAccess().createValuesSupplier().getPersonValuesData()
        causeGeneralDamage = CauseGeneralDamageTk()
        becomeUnconscious = BecomeUnconsciousTk()
        personDies = PersonDiesTk()
        #
        #conume vitaminas
        if(bodyPDT._vitaminReserve == 0):
            bodyPDT._lackOfVitamin = True
        #consume minerales
        if(bodyPDT._mineralReserve == 0):
            bodyPDT._lackOfMineral = True
        if(bodyPDT._waterReserve == 0):
            bodyPDT._itIsThirsty = True
        if(bodyPDT._carbohydrateReserve == 0):
            bodyPDT._itIsHungry = True
        if(bodyPDT._glucoseInBloodReserve == 0):
            bodyPDT._areStarving = True
        if(bodyPDT._isPregnant):
            bodyPDT._pregnantTime += 1
        if(bodyPDT._isDeath):
            bodyPDT._deadDays += 1
        if(bodyPDT._itIsHungry):
            None
        if(bodyPDT._heartRate >= bodyPDT._HEART_RATE_MAXIMUM
        or bodyPDT._heartRate <= bodyPDT._HEART_RATE_MINUM):
            bodyPDT._hasACardiacArrest = True
        if(bodyPDT._bloodReserve <= personValues.BLOOD_TO_COMA):
            bodyPDT._isInACome = True
            bodyPDT._isBleeding = True
            bodyPDT = becomeUnconscious.inner(bodyPDT)
        #daño por hambre extrema
        if(bodyPDT._areStarving):
            bodyPDT = causeGeneralDamage.inner(bodyPDT)
        #causas de muerte
        if(bodyPDT._isBleeding):
            bodyPDT = personDies.inner(bodyPDT, "paro cardiaco")
            bodyPDT = causeGeneralDamage.inner(bodyPDT)
        """
        if(bodyPDT._nervousSystemState == 0):
            bodyPDT = personDies.inner(bodyPDT, "daño nervioso")
            bodyPDT = causeGeneralDamage.inner(bodyPDT)
        """
        #cuando el cerebro esta dañado causa estado daño cerebral
        if(bodyPDT.systemMap["brain"].getState() < 2):
            bodyPDT = personDies.inner(bodyPDT, "daño cerebral")
            bodyPDT = causeGeneralDamage.inner(bodyPDT)
        if(not bodyPDT.systemMap["respiratory"].isWorking()):
            bodyPDT = personDies.inner(bodyPDT, "fallo respiratorio")
            bodyPDT = causeGeneralDamage.inner(bodyPDT)
        if(bodyPDT._endocrineSystemState == 0):
            None
        if(not bodyPDT.systemMap["brain"].isWorking()):
            print("brain not work")
            bodyPDT.setIsDeath(True)
        return bodyPDT

    def distributeBloodToTheBody(self, bodyPDT):
        if(bodyPDT._hasACardiacArrest
        or not bodyPDT.systemMap["circulatory"].isWorking()):
            return bodyPDT
        #reduce infecciones con globulos blancos
        if(bodyPDT._infectionLevel > 0
        and bodyPDT._whiteBloodCellsReserve > 1):
            bodyPDT._infectionLevel -= 1
            bodyPDT._whiteBloodCellsReserve -= 1
        #cierra heridas con plaquetas
        if(bodyPDT._openWoundLevel > 0
        and bodyPDT._plateletsReserve > 1):
            bodyPDT._openWoundLevel -= 1
            bodyPDT._plateletsReserve -= 1
        #reduce toxinas usando hepatocitos
        if(bodyPDT._toxinsLevel > 0
        and bodyPDT._hepatocytesReserve > 1):
            bodyPDT._hepatocytesReserve -= 1
            bodyPDT._toxinsLevel -= 1
        #regenera los organos usando celulas madre
        for e in bodyPDT.systemMap.keys():
            system = bodyPDT.systemMap[e]
            if(system.getState() < system.getLimitState()
            and bodyPDT._stemCellsReserve > 1):
                system.setState(system.getState() + 1)
                bodyPDT._stemCellsReserve -= 1
            bodyPDT.systemMap[e] = system
        return bodyPDT


    def inner(self, bodyPDT):
        #
        bodyPDT = self.produceGlucose(bodyPDT)
        bodyPDT = self.excretoryFunction(bodyPDT)
        bodyPDT = self.produceEnergy(bodyPDT)
        bodyPDT = self.distributeBloodToTheBody(bodyPDT)
        bodyPDT = self.feedTheBody(bodyPDT)
        bodyPDT = self.applySicknessEffect(bodyPDT)
        return bodyPDT
