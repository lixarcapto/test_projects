


class DecisionThree:

    def __init__(self) -> None:
        self.__actual_key = ""
        self.__first_key = ""
        self.__key_table:dict = {}
        self.__nodes_dict:dict[list] = {}

    def has_node(self, key):
        if(key in self.__nodes_dict):
            return True
        return False

    def __has_first_key(self):
        if(self.__first_key == ""):
            return False 
        return True
    
    def add_node(self, key:str,
            value, 
            links_arr:list[str] = []):
        if(not self.__has_first_key()):
            self.__actual_key = key
            self.__first_key = key
        self.__key_table[key] = value
        self.__nodes_dict[key] = links_arr

    def get_actual_value(self):
        return self.__key_table[\
            self.get_actual_key()]

    def get_actual_key(self)->str:
        return self.__actual_key
    
    def get_next_key(self)->list[str]:
        return self.__nodes_dict\
            [self.__actual_key]
    
    def has_next(self):
        key_list = self.__nodes_dict\
            [self.__actual_key]
        if(key_list == []): return False
        return True
    
    def reset(self):
        self.__actual_key = self.__first_key

    def set_actual_key(self, next_key):
        if(not self.has_node(next_key)):
            raise Exception(
                f"node {next_key} is not exist"
            )
        key_list = self.__nodes_dict\
            [self.__actual_key]
        self.__actual_key = next_key

    def get_key_by_index(self, index):
        key_list = self.__nodes_dict\
            [self.__actual_key]
        if(not index < len(key_list)
        or index < 0):
            raise Exception(
                f"index {index} is not valid"
            )
        return key_list[index]
    
    def has_next_index(self, INDEX)->bool:
        """
        Funcion que verifica si tiene el nodo
        actual tiene el indice indicado
        """
        key_list = self.__nodes_dict\
            [self.__actual_key]
        if(INDEX < 0
        or INDEX > len(key_list) -1):
            return False
        return True

    def set_key_by_index(self, index):
        key = self.get_key_by_index(index)
        self.set_actual_key(key)

