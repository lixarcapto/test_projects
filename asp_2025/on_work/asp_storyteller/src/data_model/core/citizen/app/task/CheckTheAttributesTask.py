


class CheckTheAttributesTask:

    """
        Revisa si las condiciones de atributos maximos y minimos
        de un trigger se cumplen. Si se cumplen retorna True y
        sino False.
    """
    def inner(self, citizenPack, citizenTrigger):
        if(len(citizenTrigger.maximumAttributeConditionArray) > 0):
            for e in citizenTrigger.maximumAttributeConditionArray:
                if(not self.inner.barMap[e["key"]] <= e["value"]):
                    return False
        if(len(citizenTrigger.minimumAttributeConditionArray) > 0):
            for e in citizenTrigger.minimumAttributeConditionArray:
                if(not self.inner.barMap[e["key"]] >= e["value"]):
                    return False
        return True
