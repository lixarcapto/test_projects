



from data_model.core.work_activity.core.work.Work import Work
from data_model.core.work_activity.core.person_work.PersonWork import PersonWork

class WorkActivity:

    WORK_AREAS_TEXT = [
        #Primaria
        "pesca",
        "tala",
        "caza",
        "ganaderia",
        "agricultura",
        "recoleccion",
        "mineria",
        "irrigacion"
        #secundaria
        "serreria",
        "textil",
        "alimentos",
        "bebidas",
        "carniceria",
        "fundicion",
        "automotriz",
        "aeronautica",
        "armeria",
        "cria",
        "cocina",
        "alta tecnologia",
        "construccion",
        #terciaria
        "transporte",
        "politica",
        "oficina",
        "barberia",
        "medicina",
        "dentista",
        "limpieza",
        "piloto",
        "marinero",
        "ventas",
        "mensajeria",
        "erotismo",
        "policia",
        "seguridad de prision",
        "delincuencia",
        "cuidado",
        "almacenes"
    ]

    def __init__(self):
        self.work = Work()
        self.person = PersonWork(WorkActivity.WORK_AREAS_TEXT)
        self.person.randomize()
        return

    def advanceTurn(self):
        return

    def writeActivity(self):
        text = " el trabajo era "
        text += str(self.work.type) + " "
        text += "del sector " + str(self.work.sector) + " "
        text += " y el area " + WorkActivity.WORK_AREAS_TEXT[self.work.area] + " "
        text += " le faltaban " + str(self.work.missingProgress) + " horas "
        text += " podia aguantar " + str(self.person.energy) + " horas "
        text += " pero acordaron " + str(self.person.timeRemaining) + " horas mas "
        text += self.person.writePersonWork()
        return text
