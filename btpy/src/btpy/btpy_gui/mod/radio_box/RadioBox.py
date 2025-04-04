

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ..frame.Frame import Frame

class RadioBox(WidgetStandard):

    def __init__(self, window, title:str,
            key_list:list[str]):
        super().__init__()
        self.widget = None
        self.label = None
        self.__value = None
        self.__button_list = []
        self.__init_components(window)
        self.__create_button_list(key_list)
        self.set_title(title)

    def set_value(self, KEY:str):
        n = 0
        for button in self.__button_list:
            if(button.cget("text") == KEY):
                self.__value.set(n)
                break
            n += 1

    def get_value(self)->list[str]:
        index = self.__value.get()
        return self.__button_list[index]\
            .cget("text")

    def __create_button_list(self,
            KEY_LIST:list[str])->None:
        button = None
        n = 0
        for e in KEY_LIST:
            button = tk.Radiobutton(
                self.widget.widget, 
                text = e, 
                variable= self.__value,
                value = n
            )
            self.__button_list.append(
                button)
            n += 1

    def __init_components(self, window):
        self.widget = Frame(
            window
        )
        self.label = tk.Label(
            self.widget.widget
        )
        self.widget.widget.config(
            borderwidth=1,
            relief = "solid"
        )
        self.__value = tk.IntVar()
        # dibujar ---------------------
        self.label.pack(anchor=tk.W)
        for button in self.__button_list:
            button.pack(anchor=tk.W)