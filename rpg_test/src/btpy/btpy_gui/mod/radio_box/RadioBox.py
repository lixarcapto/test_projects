

import tkinter as tk
from ..widget_composite.WidgetComposite \
    import WidgetComposite
from ..frame.Frame import Frame
from ..switch_radio.SwitchRadio import SwitchRadio

class RadioBox(WidgetComposite):

    def __init__(self, window, title:str,
            key_list:list[str] = []):
        super().__init__(window)
        self.__value = tk.IntVar()
        self.__value.set(-1)
        self.__button_list:SwitchRadio = []
        if(key_list != []):
            self.__create_button_list(
                key_list)
        self.set_title(title)

    def add_on_change_listener(self, 
            CALLBACK):
        for i in range(len(self.__button_list)):
            self.__button_list[i]\
                .add_on_change_listener(
                    CALLBACK)

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
    
    def set_content(self, 
                KEY_LIST:list[str]):
        self.__format_button()
        self.__create_button_list(KEY_LIST)
    
    def __format_button(self):
        for button in self.__button_list:
            button.pack_forget()
        self.__button_list = []

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
                fill=tk.BOTH, expand=True
            )
            n += 1