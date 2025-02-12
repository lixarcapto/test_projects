


class Three:

    def __init__(self):
        self.__dict = {}

    def print(self):
        print(self.__dict)

    def get_route(self, node_key):
        route = self.deep_seek(
            self.__dict, node_key, "", [])
        new_route = []
        for i in range(len(route)):
            if(not route[i] == ""):
                new_route.append(route[i])
        #new_route = new_route[::-1]
        return new_route

    def get_nodes(self, node_key):
        route_arr = self.get_route(node_key)
        print("route", route_arr)
        return self.get_recursive(self.__dict, 
            route_arr, node_key)

    def set_in_route_arr(self, route_arr, 
            node):
        self.set_recursive(self.__dict, 
            route_arr, node)

    def set_recursive(self, dict, route_arr,
            node, index = 0):
            k = route_arr[index]
            if(k in dict
            and index == len(route_arr) -1):
                dict[k][node] = {}
            else:
                index += 1
                self.set_recursive(
                    dict[k], 
                    route_arr,
                    node,
                    index
                )

    def get_recursive(self, dict, route_arr,
                node, index = 0):
            k = route_arr[index]
            if(k in dict
            and index == len(route_arr) -1):
                return dict[k]
            else:
                index += 1
                return self.get_recursive(
                    dict[k], 
                    route_arr,
                    node,
                    index
                )

    def set_in_node(self, 
            node, node_store = ""):
        if(node_store == ""):
            self.__dict[node] = {}
        elif(node_store in self.__dict):
            self.__dict[node_store]\
                [node] = {}
        else:
            route = self.get_route(
                node_store)
            print("route ", route)
            self.set_in_route_arr(route, 
                node)
            
    def deep_seek(self, dict_self, 
                  node_seek, actual_node, 
                  route_arr):
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
                route = self.deep_seek(v, node_seek, k, new_route_arr)
                if route:  # Si se encontró la ruta al nodo buscado
                    return route  
        return [] 

    def deep_seek_old(self, dict, 
            node_seek, actual_node, 
            route_arr):
        new_route_arr = route_arr
        if(not actual_node in new_route_arr):
            new_route_arr.append(actual_node)
        if(dict != {}):
            for k in dict:
                route_r = self.deep_seek(
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