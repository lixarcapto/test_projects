

from persistence.Persistence import Persistence
from btpy.Btpy import Btpy

class Model:

    def __init__(self):
        self.path_nif:str = "./res/docx/nif_test.docx"
        self.persistence = Persistence()
        self.graph:Btpy.Graph = Btpy.Graph()
        self.__start_key:str = ""
        self.text_history:str = ""
        self.nif_name = ""
        self.key_index:str = ""
        self.key_used_list = []
        self.is_end = False

    def __get_is_end(self)->bool:
        return self.is_end
    
    def __set_is_end(self, BOOL):
        self.is_end = BOOL

    def request(self, KEY:str, 
            ARG_DICT:dict):
        """
        Esta funcion request sirve para
        separar el modelo de la vista,
        de esta forma se puede añadir 
        un controlador en medio para 
        comunicar ambos componentes
        como cliente-servidor.
        """
        response = None
        if(KEY == "get_nif_name"):
            response = self.__get_nif_name()
        if(KEY == "get_render"):
            response = self.__get_render()
        if(KEY == "set_key"):
            response = self.__set_key(
                ARG_DICT["key"]
            )
        if(KEY == "start_nif"):
            self.__start_nif()
        if(KEY == "get_is_end"):
            response = self.__get_is_end()
        if(KEY == "set_is_end"):
            self.__set_is_end(
                ARG_DICT["bool"]
            )
        if(KEY == "load_nif_file"):
            self.__load_nif_file(
                ARG_DICT["path"]
            )
        return response

    def __get_nif_name(self):
        title = self.nif_name
        title = title.lower()
        return title.title()

    def __find_nif_name_from_path(self, 
            PATH:str):
        t_string = PATH.replace(
            ".docx", "")
        split_list = t_string\
            .split("/")
        return split_list[
            len(split_list) -1]
        

    def __start_nif(self):
        self.text_history = ""
        self.key_used_list = []
        self.__set_key(self.__start_key)

    def __load_nif_file(self, PATH:str):
        self.path_nif = PATH
        self.nif_name = self.__find_nif_name_from_path(
            PATH
        )
        self.load_nif_graph()
    
    def load_nif_graph(self):
        nif_list:dict = self.persistence\
            .load_nif_docx(
                self.path_nif
            )
        for scene_dict in nif_list:
            self.graph.add_node(
                scene_dict["KEY"], 
                scene_dict["TEXT"]
            )
        scene_keys = []
        for scene_dict in nif_list:
            scene_keys = Btpy.clean_voids(
                scene_dict\
                ["SCENE_KEYS"])
            if(scene_keys == []):
                continue
            self.graph.add_neighbors_list(
                scene_dict["KEY"],
                scene_keys
            )
        self.__start_key = nif_list[0]\
            ["KEY"]
        self.key_index = nif_list[0]["KEY"]

    def __get_render(self):
        option = self.__get_key_options()
        return {
            "TEXT":self.text_history,
            "KEY":self.key_index,
            "SCENE_KEYS":option
        }

    def __set_key(self, KEY:str):
        """
        Funcion que selecciona una clave
        del grafo para cargar.
        """
        self.key_index = KEY
        print("key sleect", KEY)
        self.key_used_list.append(
            self.key_index)
        value = self.graph.get_value(
            self.key_index)
        self.text_history += value + " "
            

    def __get_key_options(self)->list:
        key_neighbors = self.graph\
            .get_neighbors_keys(
                self.key_index
            )
        print("key_neighbors", key_neighbors)
        for key in self.key_used_list:
            if(key in key_neighbors):
                key_neighbors.remove(key)
        if(key_neighbors == []):
            self.is_end = True
        return key_neighbors
