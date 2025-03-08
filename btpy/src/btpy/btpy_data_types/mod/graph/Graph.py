


class Graph:

    """
    Clase que permite utilizar de forma
    facil y rapida grafos para usos
    generales.
    """

    def __init__(self)-> None:
        self.__last_code:int = 0
        self.__adj_list:dict[str, list] \
            = {}  
        self.__dict_values:dict[str, any] \
            = {}
        self.__translation_table\
            :dict[str, str] = {}
        
    # PUBLIC ACCESSORS ------------------------


        
    # PUBLIC MUTATORS --------------------------
        
    def clean(self)-> None:
        """
        Funcion que limpia todos los 
        datos del grafo.
        """
        self.__last_code = 0
        self.__adj_list = {}
        self.__dict_values = {}
        self.__translation_table = {}

    def get_value(self, KEY_VERTEX:str)->any:
        """
        Funcion que obtiene el valor
        de un nodo del grafo identificado
        con la clave enviada.
        """
        self.__valid_long_vertex(KEY_VERTEX)
        short_vertex:str = self\
            .__translate_key(KEY_VERTEX)
        return self.__dict_values\
            [short_vertex]

    def set_value(self, KEY_VERTEX:str, 
                VALUE:any)-> None:
        """
        Funcion que asigna un valor
        de un nodo al grafo identificado
        con la clave enviada.
        """
        self.__valid_long_vertex(KEY_VERTEX)
        short_vertex:str = self\
            .__translate_key(KEY_VERTEX)
        self.__dict_values[short_vertex] \
            = VALUE

    def add_node(self, 
            KEY:str, 
            VALUE:any = None
            )-> None:
        """
        Funcion que agrega un nuevo nodo
        al grafo identificandolo con la
        clave enviada como KEY parametro.
        Las claves usadas por el usuario
        no son las claves que usa la
        aplicacion para almacenar el 
        vertice; sino que esta usa
        una clave mas breve para reducir
        el consumo de memoria.
        """
        vertex = self.__get_unique_code()
        self.__translation_table[KEY] \
            = vertex
        self.__dict_values[vertex] \
            = VALUE
        self.__add_vertex(vertex)
        
    def remove_node(self, KEY:str)\
            -> None:
        """
        Funcion que elimina el nodo 
        identificado con la clave enviada.
        """
        self.__valid_long_vertex(KEY)
        vertex = self.__translate_key(KEY)
        # elimina los valores de cada
        # vertice
        del(self.__dict_values[vertex])
        # elimina todas las aristas 
        # asociadas a la clave
        self.__remove_edges(vertex)
        # elimina el vertice
        del(self.__adj_list[vertex])
        # elimina la clave de traduccion
        del(self.__translation_table[KEY])

    def has_node(self, KEY:str)\
            -> bool:
        return KEY in self\
            .__translation_table
    
    def get_neighbors_values(self, 
            KEY:str)-> list[str]:
        vertex = self.__translate_key(KEY)
        vertex_list = self\
            .__get_neighbors_short_vertex(vertex)
        values_list = []
        for vertex in vertex_list:
            values_list.append(
                self.__dict_values[vertex])
        return values_list
    
    def get_neighbors_keys(self, 
            KEY:str)-> list[str]:
        vertex = self.__translate_key(KEY)
        vertex_list = self\
            .__get_neighbors_short_vertex(vertex)
        key_list = self\
            .__translate_short_vertex_list(
                vertex_list)
        return key_list

    def get_deep_search_path(self,
            KEY_START : str, 
            KEY_END : str,
            )-> list[str]:
        vertex_start = self.__translate_key(
            KEY_START)
        vertex_end = self.__translate_key(
            KEY_END)
        vertex_path = self\
            .__get_deep_search_path(
                vertex_start,
                vertex_end
            )
        key_list = self.__translate_short_vertex_list(
            vertex_path)
        return key_list
    
    def add_neighbors_list(self, 
            KEY:str, 
            NEIGHBORS_LIST:list[str])\
            -> None:
        self.__valid_long_vertex(KEY)
        vertex = self.__translate_key(KEY)
        vertex_list = self.__translate_long_vertex_list(
            NEIGHBORS_LIST)
        for vertex_neighbor in vertex_list:
            self.__add_edge(vertex, 
                vertex_neighbor)
            
    def load_graph_dict(self,
            GRAPH_DICT
            :dict[str, list[str]],
            VALUES_DICT:dict[str, any])\
            -> None:
        """
        Esta funcion recibe como 
        GRAPH_DICT un diccionario
        de arrays string que representan
        las aristas; y VALUES dict que 
        es un diccionario de any type 
        que representa los valores de
        cada vertice.
        """
        for k in GRAPH_DICT:
            self.add_node(k, 
                VALUES_DICT[k])
        for k in GRAPH_DICT:
            self.add_neighbors_list(
                k, GRAPH_DICT[k]
            )

    # ----------------------------------------
    # PRIVATE -------------------------------

    def __get_unique_code(self)->str:
        """
        Funcion que crea un codigo
        unico para identificar a cada
        vertice del grafo.
        """
        code:str = str(self.__last_code)
        self.__last_code += 1
        return code

    def __translate_key(self, KEY:str)\
            ->str:
        """
        Funcion que traduce una clave
        larga elegida por el usuario a 
        una clave reducida elegida por
        la aplicacion.
        """
        return self\
            .__translation_table[KEY]

    def __translate_vertex(self, 
            VERTEX:str)\
            -> str:
        """
        Funcion que traduce una clave
        de vertice abreviada en una clave
        larga de vertice elegida por 
        el usuario.
        """
        v = None
        for k in self.__translation_table:
            v = self.__translation_table[k]
            if(v == VERTEX):
                return k
        return ""

    def __valid_long_vertex(self, 
            KEY:str)-> None:
        """
        Funcion que valida si la clave
        larga de un vertice es correcta;
        sino lanzara un error.
        """
        if(not isinstance(KEY, str)):
            raise Exception(f"<!>Error: The parameter KEY is not a string")
        if(not self.has_node(KEY)):
            raise Exception(f"<!>Error: The key sent in the KEY parameter does not exist")

    def __remove_edges(self, 
            SHORT_VERTEX:str)\
            -> None:
        """
        Funcion que elimina todas las
        aristas de un vertice determinado.
        """
        i:int = 0
        for k in self.__adj_list:
            if(SHORT_VERTEX in self.__adj_list[k]):
                i = self.__adj_list[k]\
                    .index(SHORT_VERTEX)
                del(self.__adj_list[k][i])
            
    def __translate_long_vertex_list(self, 
            LONG_VERTEX_LIST:list[str])\
            -> list[str]:
        """
        Funcion que traduce una lista
        de claves de vertices largas en
        una lista de claves de vertices
        cortas.
        """
        short_vertex:str = ""
        short_vertex_list:list[str] = []
        for long_vertex in LONG_VERTEX_LIST:
            short_vertex = self\
                .__translate_key(
                    long_vertex)
            short_vertex_list.append(
                short_vertex)
        return short_vertex_list

    def __add_vertex(self, SHORT_VERTEX:str)\
            -> None:
        if(SHORT_VERTEX not 
                in self.__adj_list):
            self.__adj_list[SHORT_VERTEX]\
                = []

    def __add_edge(self, VERTEX_1:str, 
                VERTEX_2:str)-> None:
        if VERTEX_1 in self.__adj_list \
        and VERTEX_2 in self.__adj_list:
            if(VERTEX_2 not \
               in self.__adj_list[VERTEX_1]):
                self.__adj_list[VERTEX_1] \
                    .append(VERTEX_2)
            if(VERTEX_1 not \
               in self.__adj_list[VERTEX_2]):
                self.__adj_list[VERTEX_2] \
                    .append(VERTEX_1)  # For undirected graphs
        else:
            raise ValueError(
                "Vertices not found in graph.")

    def __add_directed_edge(self, 
            vertex1, vertex2): 
        #for directed graphs.
        if((vertex1 in self.__adj_list) 
        and (vertex2 in self.__adj_list)):
            self.__adj_list[vertex1]\
                .append(vertex2)
        else:
            raise ValueError(
                "Vertices not found in graph.")

    def __get_vertex_list(self)-> list[str]:
        return list(self.__adj_list.keys())

    def __get_edges(self):
        edges = []
        for vertex, neighbors in self.__adj_list.items():
            for neighbor in neighbors:
                if (neighbor, vertex) not in edges: #prevents duplicate edges in undirected graphs
                    edges.append((vertex, neighbor))
        return edges

    def __get_neighbors_short_vertex(self, 
            VERTEX)-> list[str]:
        if VERTEX in self.__adj_list:
            return self.__adj_list[VERTEX]
        else:
            return None

    def __translate_short_vertex_list(self, 
            vertex_list:list[str])\
            ->list[str]:
        key_list:list[str] = []
        key:str = ""
        for vertex in vertex_list:
            key = self.__translate_vertex(
                vertex)
            key_list.append(key)
        return key_list

    def __str__(self):
        return str(self.__adj_list)
    
    def __get_deep_search_path(self, 
            start_vertex, 
            end_vertex, 
            visited=None, 
            path=None
        ):
        """Depth-First Search traversal to find a path."""
        if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(start_vertex)
        path.append(start_vertex)

        if start_vertex == end_vertex:
            return path

        neighbors = self.__get_neighbors_short_vertex(start_vertex)
        if neighbors:
            for neighbor in neighbors:
                if neighbor not in visited:
                    result = self\
                        .__get_deep_search_path(
                            neighbor, 
                            end_vertex, 
                            visited, 
                            path
                        )
                    if result:
                        return result

        path.pop()  # Backtrack if no path found
        return None