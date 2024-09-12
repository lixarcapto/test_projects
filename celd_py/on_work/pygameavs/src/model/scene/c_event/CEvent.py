


class CEvent:

    def __init__(self, name) -> None:
        self.name = name
        self.effect_list = []
        self.condition_list = []

    """
     añade una función que verifica 
     si la condición es cierta para 
     el objeto tornando un dato boolean.
    """
    def add_check(self, function):
        self.condition_list.append(function)

    """
     añade una que recibe un objeto 
     para aplicar efectos y retorna 
     el objeto.
    """
    def add_effect(self, function):
        self.effect_list.append(function)

    """
     función que aplica todas las 
     funciones almacenadas de la lista 
     al objeto enviado y lo retorna.
    """
    def __apply_effect(self, gobject):
        gobject = None
        for effect in self.effect_list:
            gobject = effect(gobject)
        return gobject
    
    """
     Función que verifica si el 
     objeto enviado cumple todas 
     las condiciones de la lista.
    """
    def __check_conditions(self, gobject):
        meet_condition = None
        for check in self.effect_list:
            meet_condition = check(gobject)
            if(not meet_condition): return False
        return True
    
    """
     función que verifica si el objeto 
     enviado cumple las condiciones se 
     aplica efectos en consecuencia 
     para retornar el objeto.
    """
    def check_gobject(self, gobject):
        meet_condition = self\
            .__check_conditions(gobject)
        if(not meet_condition): 
            return gobject
        return self.__apply_effect(gobject)

