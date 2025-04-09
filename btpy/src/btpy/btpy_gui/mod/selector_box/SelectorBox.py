

import tkinter as tk
from ..frame.Frame import Frame
from ..select_button.SelectButton import SelectButton
from ..widget_composite.WidgetComposite import WidgetComposite

class SelectorBox(WidgetComposite):

    def __init__(self, window, title:str,
            key_list:list[str]):
        super().__init__(window)
        self.grid_size = 1
        self.__button_list = []
        self.set_title(title)
        self.set_components(key_list)

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

    def __format_buttons(self):
        for button in self.__button_list:
            button.grid_forget()
        self.__button_list = []

    def set_components(self, KEY_LIST):
        self.__format_buttons()
        self.__create_button_list(
            KEY_LIST)
        self.__arrange_button_in_grid()

    def __create_button_list(self,
            KEY_LIST:list[str])->None:
        button = None
        for e in KEY_LIST:
            button = SelectButton(
                self.widget, e)
            self.__button_list.append(
                button)
            
    def __arrange_button_in_grid(self):
        x:int = 0
        y:int = 0
        for button in self.__button_list:
            button.grid(x, y)
            x += 1
            if(x == self.grid_size):
                y += 1
                x = 0
    
