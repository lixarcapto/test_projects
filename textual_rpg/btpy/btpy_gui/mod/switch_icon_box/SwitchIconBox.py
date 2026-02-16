

import tkinter as tk
from ..widget_composite.WidgetComposite \
    import WidgetComposite
from ..switch_icon.SwitchIcon import SwitchIcon
from ..frame.Frame import Frame
from ..sort_in_grid.sort_in_grid import sort_in_grid

class SwitchIconBox(WidgetComposite):

    """
    Este componente es un grid de botones
    que comparten una unica callback 
    la cual recibe como argumento el
    texto que identifica a cada boton; 
    esto facilita añadir comportamientos
    iguales a varios botones.
    """

    def __init__(self, window, 
            is_horizontal,
            title:str = ""):
        super().__init__(window, 
            is_horizontal)
        self.grid_size:int = 1
        self.button_list = []
        self.set_title(title)
        
    def set_grid_size(self, SIZE:int):
        self.grid_size = SIZE

    def set_components(self, SIZE:int, 
            COLUMNS:int):
        self.format_button_list()
        self.create_button_list(SIZE)
        self.grid_size = COLUMNS
        self.__arrange_button_dict()

    def set_content_text(self, TEXT_LIST):
        i = 0
        for button in self.button_list:
            button.set_title(TEXT_LIST[i])
            i += 1

    def set_path_list_true(self, 
                PATH_LIST):
        i = 0
        for button in self.button_list:
            button.set_path_image_true(
                PATH_LIST[i]
            )
            i += 1
    
    def set_path_list_false(self, 
                PATH_LIST):
        i = 0
        for button in self.button_list:
            button.set_path_image_false(
                PATH_LIST[i]
            )
            i += 1

    def create_button(self):
        button = SwitchIcon(
                self.widget, ""
            )
        self.button_list.append(button)

    def create_button_list(self, 
            QUANTITY)->None:
        for i in range(QUANTITY):
            self.create_button()
            
    def add_listener_to(self, 
            INDEX_BUTTON:0, 
            CALLBACK:callable):
        button = self.__button_dict\
            [INDEX_BUTTON]
        button.add_listener(CALLBACK)
            
    def add_single_listener(self, 
                CALLBACK_ARGS_X1:callable):
        """
        Esta funcion recibe una callback
        que ejecutara el boton cada
        vez que se presione enviando
        el indice del boton
        como argumento. Sirve para
        crear un listener unico para
        todos los botones.
        """
        button = None
        for i in range(len(self.button_list)):
            button = self.button_list[i]
            def aux(key):
                def fn(e):
                    CALLBACK_ARGS_X1(key)
                return fn
            button.add_listener(
                aux(i)
            )
            self.button_list[i] = button

    def format_button_list(self):
        button = None
        for i in range(len(self.button_list)):
            button = self.button_list[i] 
            button.grid_forget()
        self.button_list = []

    def __arrange_button_dict(self):
        sort_in_grid(self.button_list,
                self.grid_size)