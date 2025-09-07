

class Three:

    def __init__(self):
        self.__dict = {}

    def write(self):
        return self.__dict
    
    def get_dict(self)->dict[dict[str]]:
        return self.__dict

    def __get_route(self, node_key:str)\
            ->list[str]:
        route = self.__deep_seek(
            self.__dict, node_key, "", [])
        new_route = []
        for i in range(len(route)):
            if(not route[i] == ""):
                new_route.append(route[i])
        #new_route = new_route[::-1]
        return new_route

    def get_nodes(self, node_key:str)\
            ->dict[dict]:
        route_arr = self.__get_route(node_key)
        print("route", route_arr)
        return self.__get_recursive(self.__dict, 
            route_arr, node_key)
    
    def create_keys_list(self)\
            ->list[str]:
        array = self.__recursive_seersh(
            self.__dict, [])
        return array

    def __recursive_seersh(self, diccionario, 
            key_list):
        for k, v in diccionario.items():
            key_list.append(k)
            if isinstance(v, dict):
                self.__recursive_seersh(
                    v, key_list)
        return key_list
    
    def __get_order_list_recursive(self, 
            diccionario, 
            camino=[]):
        """
        Realiza una búsqueda en profundidad 
        en un diccionario anidado y devuelve 
        una lista con las claves de los nodos, 
        desde los más profundos hasta los 
        más elevados.
        """
        resultados = []
        for clave, valor in diccionario.items():
            nuevo_camino = camino + [clave]
            if isinstance(valor, dict) and valor:  # Verificamos si es un diccionario no vacío
                resultados.extend(
                    self.__get_order_list_recursive(
                        valor, 
                        nuevo_camino
                    )
            )
            else:
                resultados.append(nuevo_camino)
        return resultados

    def __set_in_route_arr(self, 
            route_arr:list[str], node:str):
        self.__set_recursive(self.__dict, 
            route_arr, node)

    def __set_recursive(self, dict_send:dict, 
                route_arr:list[str], 
                node_key:str, 
                index:int = 0)\
                -> None:
            k = route_arr[index]
            if(k in dict_send
            and index == len(route_arr) -1):
                dict_send[k][node_key] = {}
            else:
                index += 1
                self.__set_recursive(
                    dict_send[k], 
                    route_arr,
                    node_key,
                    index
                )

    def __get_recursive(self, 
                dict_send:dict, 
                route_arr:list[str],
                node_key:str, 
                index:int = 0)\
                ->list[str]:
            k = route_arr[index]
            if(k in dict_send
            and index == len(route_arr) -1):
                return dict_send[k]
            else:
                index += 1
                return self.__get_recursive(
                    dict_send[k], 
                    route_arr,
                    node_key,
                    index
                )

    def set_in_node(self, 
            node_key:str, 
            node_store:str = "")->None:
        if(node_store == ""):
            self.__dict[node_key] = {}
        elif(node_store in self.__dict):
            self.__dict[node_store]\
                [node_key] = {}
        else:
            route = self.__get_route(
                node_store)
            print("route ", route)
            self.__set_in_route_arr(route, 
                node_key)
            
    def __deep_seek(self, 
            dict_self:dict, 
            node_seek:str, 
            actual_node:str, 
            route_arr:list[str])->None:
        """
        Encuentra la ruta hacia un nodo específico en un diccionario anidado.

        Args:
        dict: El diccionario a explorar.
        node_seek: El nombre del nodo que se desea encontrar.
        actual_node: El nombre del nodo actual en la ruta.
        route_arr: Una lista que almacena la ruta actual.

        Returns:
        Una lista con los nombres de los nodos que forman la ruta 
        al nodo buscado, o una lista vacía si el nodo no se encuentra.
        """
        new_route_arr = route_arr + [actual_node] 

        if node_seek == actual_node:  # Si encontramos el nodo buscado
            return new_route_arr 

        if isinstance(dict_self, dict):  
            # Corrección: Verificar 
            # si 'dict' es un diccionario
            for k, v in dict_self.items():
                route = self.__deep_seek(v, node_seek, k, new_route_arr)
                if route:  # Si se encontró la ruta al nodo buscado
                    return route  
        return [] 

    #not used
    def __deep_seek_old(self, dict, 
            node_seek, actual_node, 
            route_arr):
        new_route_arr = route_arr
        if(not actual_node in new_route_arr):
            new_route_arr.append(actual_node)
        if(dict != {}):
            for k in dict:
                route_r = self.__deep_seek(
                    dict[k], 
                    node_seek, 
                    k, 
                    new_route_arr
                )
                if(not node_seek in route_r):
                    return new_route_arr
                for e in route_r:
                    if(not e in new_route_arr):
                        new_route_arr\
                            .append(e)
        return new_route_arr