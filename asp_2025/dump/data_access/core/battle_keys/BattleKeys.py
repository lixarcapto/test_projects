



from basic.Basic import Basic

class BattleKeys:

    def __init__(self):
        return

    def getEffectTypeKeysMap(self):
        """
            los efectos applican el daño final al cuerpo y organismo,
            mientras que el daño es el tipo de ataque realizado que aplicara
            efectos si atraviesa las resistencias, utilizando diversos
            formatos para entrar al cuerpo. Cada ataque puede tener un efecto,
            y aplicara a una zona del cuerpo segun donde acierte, se divide en 13
            zonas:
            La armadura absorbe el primer golpe con una pequeña probabilidad
            de que la armadura falle y no funcione.
                - fallo arriba
                - fallo derecha
                - fallo izquierda
                - fallo abajo
                - face #no estan protegidos
                - cabeza
                - cuello #no estan protegidos
                - brazos
                - pecho
                - panza
                - cintura #no estan protegidos
                - cadera
                - piernas
        """
        array = [
            "poison",
            "gas",
            "blow", #aplastamiento
            "scratch", #perforante, cortante y rasguños
            "fire",
            "plage",
            "infection",
            "curse", #causado por magia
            "vital_wave", #causado por golpes de ki
            "fear", #causado por intimidacion
            "confusion", #causado pro inteligencia
            "distracted", #causado por atractivo
            "electric_shock",
            "cold_snap",
            "radioactive_blast",
            "blinding", #cegador
            "noisy", #ruidoso
            "microwave_blast",
            "burst",
            "hunger"
        ]
        return Basic().convertArrayToMap(array)

    def getDamageTypeKeysMap(self):
        array = [
            "cutting",
            "piercing",
            "dent",
            "push",
            "firearm", #velocidad de bala
            "liquid", #puede ser efecto fuego o veneno
            "gas",
            "magic",
            "fervor",
            "intimidating",
            "attractive",
            "plasma", #formato de electricidad y el qi
            "cold",
            "radioactive",
            "psychological",
            "light", #puede causar ceguera e ilumina zonas
            "noisy",
            "antitank",
            "microwave"
        ]
        return Basic().convertArrayToMap(array)
