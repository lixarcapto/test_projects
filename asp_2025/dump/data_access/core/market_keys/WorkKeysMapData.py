




from basic.Basic import Basic

class WorkKeysMapData:

    def __init__(self):
        array = [
            #Primaria
            "fishing",
            "forestry",
            "hunt",
            "cattle_raising",
            "farming",
            "harvest",
            "minning",
            "irrigation"
            #secundaria
            "sawmill",
            "textil",
            "food",
            "drink",
            "meat",
            "foundry",
            "automotive",
            "aeronautic",
            "armory",
            "breeding",
            "kitchen",
            "high_technology",
            "building",
            #terciaria
            "transport",
            "politic",
            "office",
            "barbershop",
            "medicine",
            "dentist",
            "cleaning",
            "pilot",
            "sailor",
            "sales",
            "messenger",
            "eroticism",
            "police",
            "prison_guard",
            "criminal",
            "care",
            "warehouses"
        ]
        self.INNER = Basic().convertArrayToMap(array)
        return
