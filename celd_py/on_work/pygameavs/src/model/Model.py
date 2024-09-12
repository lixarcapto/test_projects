

from btpy.src.btpy.Btpy import Btpy
import pygame
from .go_factory.GoFactory import GoFactory
import sys
from .fn.create_bar import*
from .fn.dict_types import*
from view.View import View
from .scene.Scene import Scene

class Model:

    def __init__(self, title)-> None:
        self.view = None
        self.screen = None
        self.size_scene_x = 1000
        self.size_scene_y = 1000
        self.scene = None
        self.title = title
        # datos escenario --------------------
        # nombre de la escena
        self.name:str = "" 
        # ----------------------------------
        # datos de camara -----------------
        self.__background_color = (0,0,0)
        self.limit_FPS = 2
        # ----------------------------------
        # BUFFERS--------------------------
        self.buffer_image = []
        self.object_in_cam_arr = []
        # cola de eventos
        self.event_queue = []
        self.input_event_queue = []
        self.is_runing = True
        #---------------------------------
        self.init()

    def init(self):
        self.view = View(self.title, 
            1200, 700)
        
    def set_size_screen(self, size_x:int, 
            size_y:int)->None:
        self.view.set_size_screen(size_x, 
            size_y)
        
    def set_map_size(self, size_x, size_y):
        self.scene = Scene(size_x, size_y)

    def execute_input_event(self):
        for event in self.input_event_queue:
            if(event[0] == "key_press"):
                self.detect_AWSD(event[1])
            if(event[0] == "exit"):
                sys.exit()

    def add_go_class(self, class_name, 
        class_reference):
        self.scene.add_go_class(
            class_name, 
            class_reference
        )

    def create_gobject(self, id, 
            class_name, point = [0,0]):
        self.scene.create_gobject(
            id, class_name, point)
        
    def insert_gobject(self, gobject):
        self.scene.insert_gobject(gobject)
    
    def clear_event_asociated(self, name):
        new_array = []
        for e in self.event_queue:
            if(not name in e):
                new_array.append(e)
        self.event_queue = new_array

    def start(self):
        self.is_runing = True
        clock = pygame.time.Clock()
        render_object = []
        while(self.is_runing):
            self.update()
            render_object = self.scene.render()
            self.view.render(render_object)
            self.free()
            clock.tick(self.limit_FPS)
        # detiene el programa
        pygame.quit()

    """
    ORDEN CORRECTO
    1 liberar buffers
    2 detectar colisiones
    3 update objects
    5 user events
    4 internal sygnals
    """
    def update(self):
        self.input_control()
        self.moves_time()

    def moves_time(self):
        self.view.update()
        self.scene.update()
        self.process_time_event()

    def input_control(self):
        self.collect_actions()
        self.execute_input_event()

    def process_time_event(self):
        self.__pick_events()
        self.__process_event()#sygnals

    def collect_actions(self):
        action_arr = self.view\
            .collect_actions()
        self.input_event_queue \
            = self.input_event_queue \
            + action_arr

    def free(self):
        self.scene.free()
        # limpia el buffer de imagenes
        self.buffer_image.clear()
        self.object_in_cam_arr.clear()

    def detect_AWSD(self, data):
        # si no existen players lo ignora
        if(not self.scene.has_player()):
            return None
        player_id = self.scene\
            .get_player_main_id()
        match data:
            case "w":
                self.scene.sense_change(
                    player_id, "N")
            case "a":
                self.scene.sense_change(
                    player_id,"E")
            case "d":
                self.scene.sense_change(
                    player_id,"W")
            case "s":
                self.scene.sense_change(
                    player_id,"S")

    # SYGNALS -------------------------------

    def __process_event(self):
        """
        Función selectora que procesa los 
        eventos almacenados en la cola de 
        eventos.
        """
        for event in self.event_queue:
            print(f"{event} from __process_event")
            if(event[0] == "sense_change"):
                self.scene.sense_change(
                    event[1],
                    event[2]
                )
            if(event[0] == "move"):
                self.scene.move_in_matrix(
                    event[1],
                    event[2]
                )
            if(event[0] == "move_cam"):
                self.scene.move_cam(
                    event[1]
                )
        # solo para kill
        for event in self.event_queue:
            if(event[0] == "kill"):
                self.delete_event(
                    event[1])
            if(event[0] == "transform"):
                self.scene.transform(
                    event[1],
                    event[2],
                    event[3]
                )
        self.event_queue.clear()

    def delete_event(self, id):
        self.scene.delete_gobject(id)
        self.clear_event_asociated(id)

    def __pick_events(self):
        """
        Función que recolecta los eventos 
        desencadenados en los objetos de 
        la lista de objetos y los almacena 
        en la cola de eventos.
        """
        event_list = self.scene.pick_events()
        self.event_queue = self.event_queue \
            + event_list
            
    