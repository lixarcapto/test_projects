

import tkinter as tk
from ..frame.Frame import Frame
from ..widget_standard.WidgetStandard import WidgetStandard
from ..select_button.SelectButton import SelectButton

class SelectorBox(WidgetStandard):

    def __init__(self, window, title:str,
            key_list:list[str]):
        super().__init__()
        self.widget = None
        self.label = None
        self.inner_frame = None
        self.grid_size = 1
        self.__button_list = []
        self.__init_components(window)
        self.__create_button_list(key_list)

    def set_grid_size(self, SIZE:int):
        self.grid_size = SIZE

    def get_value(self)->list[str]:
        key_list = []
        for button in self.__button_list:
            if(button.get_value()):
                key_list.append(
                    button.get_text())
        return key_list
    
    def set_value(self, KEY_LIST:list[str]):
        for button in self.__button_list:
            for k in KEY_LIST:
                if(button.get_text() == k):
                    button.set_value(True)
                else:
                    button.set_value(False)

    def __create_button_list(self,
            KEY_LIST:list[str])->None:
        button = None
        for e in KEY_LIST:
            button = SelectButton(
                self.inner_frame, e)
            self.__button_list.append(
                button)
            
    def __arrange_button_in_grid(self):
        x:int = 0
        y:int = 0
        for button in self.__button_list:
            button.widget.grid(
                row=x, column=y,
                sticky=tk.NSEW
            )
            x += 1
            if(x == self.grid_size):
                y += 1
                x = 0

    def __init_components(self, window):
        self.widget = Frame(
            window
        )
        self.label = tk.Label(
            self.widget.widget)
        self.inner_frame = Frame(
            self.widget
        )
        self.widget.set_border(1)
        self.inner_frame.set_border(1)
        # dibujar ------------------------
        self.label.pack(anchor=tk.W)
        self.inner_frame.pack()
        self.__arrange_button_in_grid()
    
