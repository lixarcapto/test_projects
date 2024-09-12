


from persistence.Persistence import Persistence
from .read_docx_with_titles import*
from btpy.src.btpy.Btpy import Btpy
from .NodeOption import NodeOption

class Model:

    """
    Claves para escribir el NIF
    """
    class KEYS_TEXT:
        NEXT_KEY = "NEXT"
        END_KEYS = "*"
        IMAGE_KEY = "ROUTE"

    def __init__(self) -> None:
        self.__graph = Btpy.DesitionThree()
        self.__persistence = Persistence()
        self.__full_text:str = ""
        self.__is_playing = True
        self.__buffer_error_text = ""
        self.main_mode = "MAIN_MENU"
        self.__docx_route = ""
        self.__name_nif = ""
        self.init_the_reader = False
        self.an_error_ocurred = False
        self.nif_folder_route = ""
        self.__init_calls()
        
    def __init_calls(self):
        folder_route = Btpy\
            .seek_folder_route()
        # crea el docx route
        r = folder_route.replace(
            ".docx", "")
        nif_name = Btpy.cut_from(r, "/", 
            last_appearance=True)
        docx_route =  folder_route\
            + "/" + nif_name + ".docx"
        # almacena los resultados
        self.__name_nif = nif_name
        self.nif_folder_route = folder_route
        self.__docx_route = docx_route
        # lee el docx document
        self.__load_nif_docx(
           self.__docx_route)

    # PUBLIC ACCESSORS-----------------------

    def get_is_playing(self)->bool:
        return self.__is_playing

    # PUBLIC MUTATORS -------------------------

    def request(self)->dict:
        if(not self.an_error_ocurred):
            self.__save_text_readed()
        message:dict = {}
        message["title"] = self.__name_nif
        message["text"] = self.__write()
        message["is_playing"] = self.get_is_playing()
        message["error_text"] = self.__buffer_error_text
        message["route_image"] = self\
            .get_actual_image()
        message["main_mode"] = self.main_mode
        return message
    
    def get_actual_image(self):
        return self.__graph\
            .get_actual_value().route_image
    
    def destroy(self):
        self.__is_playing = False
        import sys
        sys.exit(0)

    def receive(self, message:dict)->None:
        self.an_error_ocurred = False
        index = message["index_selected"]
        if(message["event"] == "turn_off"):
            self.destroy()
        if(not index.isdigit()):
            self.__buffer_error_text\
                += "key press is not index"
            return None
        self.__select_next_index(int(index))
            
    def reset(self):
        self.__full_text = ""
        self.__is_playing = True
        self.__graph.reset()

    # PRIVATE -------------------------------

    def __select_next_index(self, INDEX:int):
        real_index = INDEX -1
        actual_key = self.__graph\
            .get_actual_key()
        if(not self.__graph.has_next_index(
                real_index)):
            self.an_error_ocurred = True
            return None
        if(actual_key == "END"):
            print("is END KEY")
            self.destroy()
        else:
            self.__graph.set_key_by_index(
                real_index)

    def __write_keys_as_list(self):
        """
        Escribe la lista de opciones a 
        elegir como una lista.
        """
        txt = ""
        keys_list = self.__graph.get_next_key()
        for i, e in enumerate(keys_list, 1):
            txt += f"{i}. {e}\n"
        return txt
    
    def __load_nif_docx(self, ROUTE:str):
        """
        Funcion que lee el archivo NIF docx
        seleccionado por el usuario.
        """
        # lee el archivo NIF
        dict_nif = read_docx_with_titles(
            ROUTE)
        # convierte las claves a mayuscula
        dict_nif = Btpy.map_in_keys(
            dict_nif,
            lambda e:e.upper()
        )
        # añade los nodos cargados
        for k in dict_nif:
            self.__add_node(
                k,
                dict_nif[k]
            )

    def __write(self):
        """
        Escribe toda la informacion 
        que debe mostrar la interface
        grafica del modelo.
        """
        txt = self.__full_text
        txt += "\n"
        txt += self.__write_keys_as_list()
        return txt
    
    def __save_text_readed(self):
        """
        Almacena valor del texto ya leido
        """
        node = self.__graph\
            .get_actual_value()
        self.__full_text += node.text
        
    def __add_node(self, KEY, RAW_TEXT):
        """
        Añade un nuevo nodo al grafo de 
        titulos
        """
        option_list = self\
            .__extract_option_keys(RAW_TEXT)
        node_option = self.fill_node(RAW_TEXT)
        self.__graph.add_node(
            KEY, 
            node_option,
            option_list
        )

    def fill_node(self, RAW_TEXT):
        """
         Carga todos los datos importantes 
         de los nodos a partir del texto 
         enviado
        """
        text = Btpy.cut_until(RAW_TEXT,
            self.KEYS_TEXT.END_KEYS)
        node_option = NodeOption()
        node_option.text = text
        node_option = self.get_route_image(
            node_option, RAW_TEXT)
        return node_option

    def get_route_image(self, node_option, 
            RAW_TEXT):
        if(not self.KEYS_TEXT.IMAGE_KEY \
           in RAW_TEXT):
            return node_option
        route = Btpy.get_between(
            RAW_TEXT,
            self.KEYS_TEXT.IMAGE_KEY, 
            self.KEYS_TEXT.END_KEYS
        )
        route = route.strip()
        # completa la ruta automaticamente
        route = self.nif_folder_route\
            + f"/{route}.png"
        node_option.route_image = route
        return node_option

    def __extract_option_keys(self, TEXT):
        """
        Obtiene la lista de claves de 
        opciones del texto seleccionado.
        """
        keys_raw = Btpy.get_between(
            TEXT, 
            self.KEYS_TEXT.NEXT_KEY, 
            self.KEYS_TEXT.END_KEYS
        )
        keys_list = keys_raw.split(",")
        for i in range(len(keys_list)):
            keys_list[i] = keys_list[i]\
                .strip()
            keys_list[i] = keys_list[i]\
                .upper()
        return keys_list