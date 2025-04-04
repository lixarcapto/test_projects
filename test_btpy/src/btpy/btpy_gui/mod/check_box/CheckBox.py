


import tkinter as tk
from ..frame.Frame import Frame
from ..widget_standard.WidgetStandard import WidgetStandard
from ...mod.check_button.CheckButton import CheckButton


class CheckBox(WidgetStandard):

    def __init__(self, window, title:str,
            key_list:list[str]):
        super().__init__()
        self.widget = None
        self.label = None
        self.__button_list = []
        self.__init_components(window)
        self.__create_button_list(key_list)
        self.set_title(title)

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
            button = CheckButton(
                self.widget, e)
            button.widget.config(
                borderwidth=0)
            self.__button_list.append(
                button)
            
    def __init_components(self, window):
        self.widget = Frame(
            window
        )
        self.label = tk.Label(
            self.widget.widget)
        self.widget.widget.config(
            borderwidth=1,
            relief = "solid"
        )
        # dibujar ----------------------
        self.label.pack(anchor=tk.W)
        for button in self.__button_list:
            button.widget.pack(anchor=tk.W)
        