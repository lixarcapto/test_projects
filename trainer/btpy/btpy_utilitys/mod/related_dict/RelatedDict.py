
from .RelatedNode import RelatedNode

class RelatedDict:

    """
        Esta clase es un diccionario especial que permite
        busquedas de claves relacionadas. Su estructura
        es un diccionario de nodos que contienen claves.

        Para usarlo debes asignar con set una clave
        multiple separada con dos puntos :, y un dato.
        pueden modificarse los datos con set(key, dato)
        y obtener el dato con get(key)

        TODO:
        * fusionar las relaciones altas.
        * crear un comparador de relaciones entre
        claves de nodos.
    """

    def __init__(self, similar_percent = 70):
        self.__similar_percent = similar_percent
        self.__node_array = []

    def delete(self, key):
        self.__node_array[key].destroy()
        del(self.__node_array[key])

    def destroy(self):
        for k in self.__node_array:
            self.__node_array[k].destroy()
        self.__node_array.clear()

    def set(self, key, data):
        has_key = self.has_key(key)
        if(not has_key):
            node = RelatedNode(key, data)
            node.set_similar_percent(self.__similar_percent)
            self.__node_array.append(node)
        else:
            self.__update_node(key, data)

    def __update_node(self, key, data):
        if(not self.has_key(key)): return None
        node = None
        for i in range(len(self.__node_array)):
            node = self.__node_array[i]
            if (node.has_key(key)):
                node.set_data(data)
                self.__node_array[i] = node
                break

    def get(self, key):
        node = None
        for i in range(len(self.__node_array)):
            node = self.__node_array[i]
            if (node.has_key(key)):
                return node.get_data()
        return None

    def has_key(self, key):
        for node in self.__node_array:
            if node.has_key(key): return True
        return False
