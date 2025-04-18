

import tkinter as tk
from ..widget_composite.WidgetComposite \
    import WidgetComposite
from ..switch_icon.SwitchIcon import SwitchIcon
from ..frame.Frame import Frame
from ..sort_in_grid.sort_in_grid import sort_in_grid

class StandardBox(WidgetComposite):

    def __init__(self, window, 
            is_horizontal,
            title:str = ""):
        super().__init__(window, 
            is_horizontal)
        self.grid_size:int = 1
        self.component_list = []
        self.set_title(title)

    def set_components(self, SIZE:int, 
            COLUMNS:int):
        self.format_button_list()
        self.create_component_list(SIZE)
        self.grid_size = COLUMNS
        self.__sort_components_in_grid()

    def create_component(self):
        button = SwitchIcon(
                self.widget, ""
            )
        self.component_list.append(button)

    def create_component_list(self, 
            QUANTITY)->None:
        for i in range(QUANTITY):
            self.create_component()
            
    def add_listener_to(self, 
            INDEX:0, 
            CALLBACK:callable):
        button = self.__button_dict\
            [INDEX]
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
        for i in range(len(self.component_list)):
            button = self.component_list[i]
            def aux(key):
                def fn(e):
                    CALLBACK_ARGS_X1(key)
                return fn
            button.add_listener(
                aux(i)
            )
            self.component_list[i] = button

    def format_components(self):
        button = None
        for i in range(len(self.component_list)):
            button = self.component_list[i] 
            button.grid_forget()
        self.component_list = []

    def __sort_components_in_grid(self,
            COLUMNS:int):
        self.grid_size = COLUMNS
        sort_in_grid(self.component_list,
                COLUMNS)