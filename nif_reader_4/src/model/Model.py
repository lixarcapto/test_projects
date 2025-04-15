

from persistence.Persistence import Persistence
from btpy.Btpy import Btpy

class Model:

    def __init__(self):
        self.path_nif:str = "./res/docx/nif_test.docx"
        self.persistence = Persistence()
        self.graph:Btpy.Graph = Btpy.Graph()
        self.__start_key:str = ""
        self.key_index:str = ""
        self.key_used_list = []
        self.is_end = False

    def start_nif(self):
        self.key_index = self.__start_key
        print("start key", self.__start_key)
        self.key_used_list = [
            self.__start_key
        ]

    def load_nif_file(self, PATH:str):
        self.path_nif = PATH
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

    def get_actual_scene_dict(self):
        value = self.graph.get_value(
            self.key_index)
        option = self.get_key_options()
        return {
            "TEXT":value,
            "KEY":self.key_index,
            "SCENE_KEYS":option
        }

    def set_key(self, KEY:str):
        self.key_index = KEY
        print("key sleect", KEY)
        self.key_used_list.append(
            self.key_index)
        print("self.key_used_list", self.key_used_list)
            

    def get_key_options(self)->list:
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
