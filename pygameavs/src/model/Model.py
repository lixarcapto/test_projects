

from btpy.src.btpy.Btpy import Btpy
import pygame
from .go_factory.GoFactory import GoFactory
import sys
from .fn.create_bar import*
from .fn.dict_types import*
from view.View import View
from .scene.Scene import Scene
from .go_manager.GoManager import GoManager

class Model:

    def __init__(self, title)-> None:
        self.view = None
        self.screen = None
        self.go_manager = None
        self.size_scene_x = 1000
        self.size_scene_y = 1000
        self.size_celd_x = 70
        self.size_celd_y = 70
        self.celd_number_x = 0
        self.celd_number_y = 0
        self.size_cam_x = 0
        self.size_cam_y = 0
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
        print("REPORT: init model")

    def init(self):
        self.view = View(self.title, 
            1200, 700)
        
    def set_size_screen(self, size_x:int, 
            size_y:int)->None:
        self.size_cam_x = size_x
        self.size_cam_y = size_y
        self.view.set_size_screen(size_x, 
            size_y)
        
    def calcule_map_data(self):
        self.size_scene_x = self.celd_number_x\
            * self.size_celd_x
        self.size_scene_y = self.celd_number_y\
            * self.size_celd_y
        
    def create_map(self, CELD_NUMBER_X, 
            CELD_NUMBER_Y):
        scene = Scene()
        self.celd_number_x = CELD_NUMBER_X
        self.celd_number_y = CELD_NUMBER_Y
        self.calcule_map_data()
        scene.set_celd_numbers(CELD_NUMBER_X,
            CELD_NUMBER_Y)
        scene.set_size_map(self.size_scene_x, 
            self.size_scene_y)
        scene.create_map()
        self.go_manager = GoManager(scene)

    def execute_input_event(self):
        for event in self.input_event_queue:
            if(event[0] == "key_press"):
                self.go_manager.scene.detect_AWSD(event[1])
            if(event[0] == "exit"):
                sys.exit()

    def delete_object(self, id):
        self.go_manager.scene\
            .delete_gobject(id)
        self.go_manager\
            .clear_event_asociated(id)

    def add_go_class(self, class_name, 
        class_reference):
        self.go_manager.scene.add_go_class(
            class_name, 
            class_reference
        )

    def create_gobject(self, id, 
            class_name, point = [0,0]):
        self.go_manager.scene.create_gobject(
            id, class_name, point)
        
    def insert_gobject(self, gobject):
        self.go_manager.scene.insert_gobject(
            gobject)

    def start(self):
        self.is_runing = True
        clock = pygame.time.Clock()
        render_object = []
        while(self.is_runing):
            self.update()
            render_object = self.go_manager.scene.render()
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
        self.go_manager.scene.update()
        self.go_manager.update()

    def input_control(self):
        self.collect_actions()
        self.execute_input_event()

    def collect_actions(self):
        action_arr = self.view\
            .collect_actions()
        self.input_event_queue \
            = self.input_event_queue \
            + action_arr

    def free(self):
        self.go_manager.scene.free()
        # limpia el buffer de imagenes
        self.buffer_image.clear()
        self.object_in_cam_arr.clear()
            
    