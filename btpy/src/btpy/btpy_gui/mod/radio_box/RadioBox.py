

import tkinter as tk
from ..widget_composite.WidgetComposite \
    import WidgetComposite
from ..frame.Frame import Frame
from ..switch_radio.SwitchRadio import SwitchRadio

class RadioBox(WidgetComposite):

    def __init__(self, window, title:str):
        super().__init__(window)
        self.__value = tk.IntVar()
        self.__value.set(-1)
        self.__button_list:SwitchRadio = []
        self.__text_list:list[str] = []
        self.__key_list:list[str] = []
        self.set_background_color(
            "#808080")
        self.set_title(title)

    def add_on_change_listener(self, 
            CALLBACK):
        for i in range(len(self.__button_list)):
            self.__button_list[i]\
                .add_on_change_listener(
                    CALLBACK)

    def set_value(self, KEY:str):
        """
        Si la clave enviada es "" o
        None no se selecciona ningun
        switch button.
        """
        if(KEY == "" 
        or KEY == None):
            self.__value.set(-1)
            return None
        index = self.__key_list\
            .index(KEY)
        self.__value.set(index)

    def get_value(self)->str:
        index = self.__value.get()
        text = self.__key_list[index]
        return text
            
    def set_components(self, 
            KEY_LIST:list[str])->None:
        """
        Function that draws a list of 
        texts on each button according 
        to the order of their indices.
        """
        self.__key_list = KEY_LIST
        self.__format_button()
        self.__create_button_list(
            len(KEY_LIST))
        self.set_columns(1)

    def set_content(self, 
            TEXT_LIST:list[str]):
        """
        function that draws a list 
        of texts for the components
        """
        self.__set_text_list(TEXT_LIST)
    
    def __format_button(self):
        for button in self.__button_list:
            button.pack_forget()
        self.__button_list = []

    def __set_text_list(self, TEXT_LIST:list[str]):
        leng = len(self.__button_list)
        self.__text_list = TEXT_LIST
        for i in range(leng):
            self.__button_list[i]\
                .set_content(TEXT_LIST[i])

    def set_columns(self, COLUMNS):
        leng = len(self.__button_list)
        x = 0
        y = 0
        for i in range(leng):
            self.__button_list[i]\
                .grid(x, y, "EW")
            x += 1
            if(x >= COLUMNS):
                x = 0
                y += 1

    def __create_button_list(self,
            SIZE)->None:
        for i in range(SIZE):
            button = SwitchRadio(
                self.widget, 
                self.__value,
                i, 
                ""
            )
            self.__button_list.append(
                button)