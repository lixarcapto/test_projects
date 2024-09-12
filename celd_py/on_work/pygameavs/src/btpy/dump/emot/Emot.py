

from ....btpy_maths.mod.sum_in_range.sum_in_range import*

# para basic thing
def max_dict(diccionario):
    """Calcula el valor máximo en un diccionario.

    Args:
        diccionario: El diccionario a evaluar.

    Returns:
        El valor máximo encontrado en el diccionario.
    """

    maximo = None
    for valor in diccionario.values():
        if maximo is None or valor > maximo:
            maximo = valor
    for k in diccionario:
        if(diccionario[k] == maximo):
            return k
    return ""

class Emot:

    LIMIT = 10
    # limite a los estados
    MID = 5
    # mitad de limit

    def __init__(self) -> None:
        self.__states_dict = {
            "sadness":0,
            "joy":0,
            "disgust":0,
            "fear":0,
            "love":0,
            "shame":0
        }
        self.memory_dict = {
            "pain":["fear", 2],
            "absurd":["joy", 2]
        }

    def get_state(self):
        return self.calcule_mayor_state()
    
    def advance_time(self):
        self.reduce_states()

    def sum_state(self, state_key, value = 1):
        e = self.__states_dict[state_key]
        e = sum_in_range(e, value, 
                     [0, Emot.LIMIT])
        self.__states_dict[state_key] = e

    def listen(self, key_list:list[str]):
        if("learn" in key_list):
            self.learn(key_list)

    def learn(self, key_list):
        i = key_list.index("learn")
        # busca la clave siguiente
        new_memory_key = key_list[i + 1]
        associate_key = key_list[i + 2]
        # busca el valor de asosiado
        memory_arr = self\
            .memory_dict[associate_key]
        key_remember = memory_arr[0]
        value = memory_arr[1]
        self.memory_dict[new_memory_key]\
         = [key_remember, value]
            
    
    def reduce_states(self):
        e = None
        for k in self.__states_dict:
            e = self.__states_dict[k]
            if e >= 1: e -= 1
            self.__states_dict[k] = e

    def calcule_mayor_state(self):
        all_are_minors = self\
            .__are_all_minors()
        if(all_are_minors):
            return "bored"
        # si no todos son menores
        key = max_dict(self.__states_dict)
        return key
        
    """
    verifica si todos son menores
    """
    def __are_all_minors(self):
        e = None
        for k in self.__states_dict:
            e = self.__states_dict[k]
            if(not e <= Emot.MID):
                return False
        return True
        
    


