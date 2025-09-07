


import random

class CauseGeneralDamageTk:

    def inner(self, bodyProduct):
        value = 0
        for e in bodyProduct.systemMap.keys():
            value = random.randint(0, 1)
            bodyProduct.systemMap[e].causeDamage(value)
        return bodyProduct
