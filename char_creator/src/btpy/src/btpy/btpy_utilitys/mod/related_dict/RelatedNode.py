

from ....btpy_string.mod.compare_string import*

class RelatedNode:

    """
        Clase nodo para el diccionario de relaciones.
    """

    def __init__(self, keys, data):
        self.__data = data
        self.__similar_percent = 0
        self.__key_related_array = self\
            .divide_keys(keys)

    # ACCESORS ------------------------------------------

    def set_similar_percent(self, percent):
        self.__similar_percent = percent

    def divide_keys(self, string):
        return string.split(":")

    # return dinamic
    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def add_key(self, key):
        if(not type("") == key):
            raise Exception("Error: isnt string " + str(key))
        if("" == key):
            raise Exception("Error: void string")
        self.__key_related_array.append(key)

    """
        Funcion que consula si el nodo
        tiene una key relacionada a la
        key enviada.
    """
    # return bool
    def has_key(self, key_searched):
        if(self.has_exactly_key(key_searched)):
            return True
        if(self.has_similar_key(key_searched)):
            return True
        return False

    # return bool
    def has_exactly_key(self, key_searched):
        if (key_searched in self.__key_related_array):
            return True
        return False

    def has_similar_key(self, key_searched):
        percent = 0
        for key in self.__key_related_array:
            percent = compare_strings(key_searched,
                key)
            percent = round(percent)
            if(percent >= self.__similar_percent):
                return True
        return False

    def destroy(self):
        self.__data = None
        self.__key_related_array.clear()
