
import tkinter as tk
from ..widget_composite.WidgetComposite \
    import WidgetComposite
from ..button.Button import Button
from ..frame.Frame import Frame
from ..standard_box.StandardBox import StandardBox

class ButtonBox(StandardBox):

    def __init__(self, window, 
            title:str):
        super().__init__(window, 
            Button,
            False, 
            title
        )
        self.set_title(title)
        self.__button_list = []

    def set_components(self, 
            KEY_LIST:list[str]):
        button = None
        for i in range(len(KEY_LIST)):
            button = Button(
                self.widget, KEY_LIST[i]
            )
            self.__button_list.append(
                button
            )
        self.set_columns(1)

    def set_content(self, 
            TEXT_LIST:list[str]):
        i = 0
        button:Button = None 
        for button in self.__button_list:
            button.set_title(
                TEXT_LIST[i]
            )
            i += 1

    def set_columns(self, COLUMNS):
        leng = len(self.__button_list)
        x = 0
        y = 0
        for i in range(leng):
            self.__button_list[i]\
                .draw_in_grid(y, x, "EW")
            x += 1
            if(x >= COLUMNS):
                x = 0
                y += 1

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
        for i in range(len(self.__button_list)):
            button = self.__button_list[i]
            def aux(key):
                def fn(e):
                    CALLBACK_ARGS_X1(key)
                return fn
            button.add_listener(
                aux(i)
            )
            self.__button_list[i] = button

    def add_listener_to(self, INDEX:int, 
            CALLBACK_ARGS_X1):
        self.__button_list[INDEX]\
            .add_listener(
                CALLBACK_ARGS_X1
            )
    
