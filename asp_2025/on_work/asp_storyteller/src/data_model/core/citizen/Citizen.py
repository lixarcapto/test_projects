


from data_model.core.citizen.app.CitizenPack import CitizenPack
from data_model.core.citizen_trigger.app.entities.CollectionCitizenTrigger import CollectionCitizenTrigger
from basic.Basic import Basic
#task
from data_model.core.citizen.app.task.ApplyRaceTraitsTask import ApplyRaceTraitsTask
from data_model.core.citizen.app.task.WritePresentationTask import WritePresentationTask
from data_model.core.citizen.app.task.HasComplementaryProductTask import HasComplementaryProductTask
from data_model.core.citizen.app.task.CheckTheAttributesTask import CheckTheAttributesTask

class Citizen:

    def __init__(self):
        self.inner = CitizenPack()
        self.inner.addTraits()
        self.inner.addNeedsBars()
        return

    def clearNotifications(self):
        self.inner.notificationArray.clear()

    def advanceOneDay(self, market, dateWritted):
        market = self.checkTriggers(market)
        self.inner.age.advanceOneDay()
        return market

    def applyRaceTraits(self, race):
        self.inner = ApplyRaceTraitsTask().inner(self.inner, race)

    def writePresentation(self):
        return WritePresentationTask().inner(self.inner)

    def writeUpdate(self):
        text = ""
        text += str(self.inner.age.inner.getActualAge())
        text += self.writePresentation()
        text += " "
        barValue = 0
        for e in self.inner.notificationArray:
            text +=  e["category"] + " " + e["key"] + " by " + e["cause"]
        self.clearNotifications()
        return text

    """
        Retorna el numero del complentary product seleccionado,
        si no existen mas retorna -1
    """
    def hasComplementaryProduct(self, citizenTrigger, market):
        return HasComplementaryProductTask().inner(self.inner,
        citizenTrigger, market)

    def checkTheAttributes(self, citizenTrigger):
        return CheckTheAttributesTask().inner(self.inner,
        citizenTrigger)

    def consumeComplementaryProduct(self, market, citizenTrigger, compProductSelected):
        compProductConditionArray = citizenTrigger.complementaryProductConditionArray
        complementaryProduct = compProductConditionArray[compProductSelected]
        for goods in complementaryProduct.goodsArray:
            market.consumeProduct(goods["key"], goods["quantity"])
        for services in complementaryProduct.servicesArray:
            market.hasProduct(services["key"], services["quantity"])
        return market

    def applyAttributeEffects(self, citizenTrigger):
        for e in citizenTrigger.attributeEffectsArray:
            self.inner.barMap[e["key"]] += e["value"]

    def addNotification(self, key, category, cause):
        map = dict()
        map["key"] = key
        map["category"] = category
        map["cause"] = cause
        self.inner.notificationArray.append(map)

    """
        * Busca cada trigger que tenga activado el ciudadano
        * Revisa si se desencadena el trigger con productos del mercado
        * Si se desencadena el trigger consume los productos y aplica
        modificadores
        * retorna el mercado modificado
    """
    def checkTriggers(self, market):
        collectionCitizenTrigger = CollectionCitizenTrigger()
        citizenTrigger = None
        canSatisfy = False
        complementaryProductSelected = 0
        imposibleProductCounter = 0
        complementaryProduct = None
        foundNeedKey = True
        for key in collectionCitizenTrigger.inner.keys():
            if(key == "hungry"):
                print("************ hungry")
            citizenTrigger = collectionCitizenTrigger.inner[key]
            canSatisfy = False
            # comprueba las condiciones
            # comprueba los atributos maximos y minimos
            canSatisfy = self.checkTheAttributes(citizenTrigger)
            if(not canSatisfy):
                return market
            # comprueba los complementary product requeridos
            if(0 < len(citizenTrigger.complementaryProductConditionArray)):
                complementaryProductSelected = self.hasComplementaryProduct(
                citizenTrigger, market)
                if(complementaryProductSelected == -1):
                    return market
                market = self.consumeComplementaryProduct(market, citizenTrigger,
                complementaryProductSelected)
            # consume los complementary product
            self.applyAttributeEffects(citizenTrigger)
            #añade notificaciones
            n = complementaryProductSelected
            compProductKey = citizenTrigger.complementaryProductConditionArray[n].keyName
            self.addNotification(
            citizenTrigger._keyName,
            citizenTrigger._category,
            compProductKey
            )
            return market
