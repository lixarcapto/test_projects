

import tkinter as tk
from ..widget_composite.WidgetComposite \
    import WidgetComposite
from ..frame.Frame import Frame
from ..switch_radio.SwitchRadio import SwitchRadio

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
            if(button.get_title() == KEY):
                self.__value.set(n)
                break
            n += 1

    def get_value(self)->list[str]:
        index = self.__value.get()
        return self.__button_list[index]\
            .get_title()

    def __create_button_list(self,
            KEY_LIST:list[str])->None:
        button = None
        n = 0
        for e in KEY_LIST:
            button = SwitchRadio(
                self.widget, 
                self.__value,
                n, 
                e
            )
            self.__button_list.append(
                button)
            button.margin.pack(
                fill=tk.BOTH, expand=True)
            n += 1