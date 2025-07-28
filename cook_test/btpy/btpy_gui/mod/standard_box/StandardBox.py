

import tkinter as tk
from ..widget_composite.WidgetComposite \
    import WidgetComposite
from ..switch_icon.SwitchIcon import SwitchIcon
from ..frame.Frame import Frame
from ..sort_in_grid.sort_in_grid import sort_in_grid

class StandardBox(WidgetComposite):

    def __init__(self, window, 
            CLASS_WIDGET,
            is_horizontal,
            title:str = ""):
        super().__init__(window, 
            is_horizontal)
        self.class_widget = CLASS_WIDGET
        self.grid_size:int = 1
        self.component_list = []
        self.set_title(title)

    def set_font(self, FONT):
        self.label_title.config(
            font = FONT)
        for e in self.component_list:
            self.component_list\
                .config(font = FONT)
            
    def set_background_color(self, COLOR):
        color = self\
            .convert_to_tk_color(COLOR)
        self.label_title.widget.config(
            bg = color)
        for e in self.component_list:
            e.set_background_color(
                color
            )

    def set_foreground_color(self, COLOR):
        color = self\
            .convert_to_tk_color(COLOR)
        self.label_title.widget.config(
            fg = color)
        for e in self.component_list:
            e.set_foreground_color(
                color
            )

    def set_components(self, SIZE:int, 
            COLUMNS:int):
        self.format_components()
        self.create_component_list(SIZE)
        self.sort_components_in_grid(
            COLUMNS)

    def create_component(self):
        button = self.class_widget(
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
        """
        Funcion que agrega un listener
        a uno de los componentes internos
        del widget enlistados; este se 
        hace mediante su indice.
        """
        max_ = len(self.component_list)
        if(INDEX < 0):
            raise Exception(
                "The INDEX parameter is not a valid index, it is less than zero."
            )
        if(INDEX > max_):
            raise Exception(
                "The INDEX parameter is not a valid index, it is greater than the size of the list."
            )
        button = self.component_list\
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
        size:int = len(self.component_list)
        for i in range(size):
            button = self.component_list\
                [i] 
            button.grid_forget()
        self.component_list = []

    def sort_components_in_grid(self,
            COLUMNS:int):
        self.grid_size = COLUMNS
        sort_in_grid(self.component_list,
                COLUMNS)