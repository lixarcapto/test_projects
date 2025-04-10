

import tkinter as tk
from ..widget_composite.WidgetComposite \
    import WidgetComposite
from ..frame.Frame import Frame

class RadioBox(WidgetComposite):

    def __init__(self, window, title:str,
            key_list:list[str]):
        super().__init__(window)
        self.__value = tk.IntVar()
        self.__button_list = []
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
                self.widget, 
                text = e, 
                variable= self.__value,
                value = n
            )
            self.__button_list.append(
                button)
            button.pack(anchor=tk.W)
            n += 1