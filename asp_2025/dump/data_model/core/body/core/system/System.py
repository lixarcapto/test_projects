



from data_access.DataAccess import DataAccess

class System:

    LIMIT_STATE = 4
    STATE_TEXT_ARRAY = [
        "estaba completamente perdido",
        "estaba destrozado",
        "tenia corte",
        "tenia un desgarro",
        "estaba completo"
    ]


    def __init__(self, type):
        """
            El estado es el numero de tejidos que contiene, se pierden por
            cortes y otros daños graves. El tejido sano
            indica el numero de tejidos que no recibieron daño leve, pero puede
            repararse progresivamente hasta el nivel de state.
            Los daños coporales pueden ser:
            > quemadura: causa daño a los tejidos, y perdida de tejidos e infeccion
            > perforante: causa herida abierta grave y tejido perdido
            > veneno: causa acumulacion de toxicos, estos causaran daño cuando alcanzen
            nivel critico
            > infection: causa daño progresivamente y aumenta con el tiempo, la infeccion
            es combatida por los globulos blancos del cuerpo o antibioticos
            > golpe: causa daño leve a los tejidos
            > corte: daño leve de tejido y herida abierta
        """
        self._type = type
        self._state = 4

#*** ACCESSORS ********************************************************************

    def getLimitState(self):
        return System.LIMIT_STATE

    def writeAppearance(self):
        translator = DataAccess().createTranslator()
        text = ""
        text += "" + translator.obtainOrganType(self._type)  + " "
        text += "" + System.STATE_TEXT_ARRAY[self.getState()]
        return text

    def getType(self):
        return self._type

    def setType(self, vint):
        self._type = vint

    def getState(self):
        return self._state

    def setState(self, vint):
        if(vint >= 0):
            self._state = vint
        else:
            self._state = 0

#*** MODIFIER *******************************************************************

    def isWorking(self):
        if(self.getState() > 0):
            return True
        return False

    def causeDamage(self, power):
            self.setState(self.getState() - power)
