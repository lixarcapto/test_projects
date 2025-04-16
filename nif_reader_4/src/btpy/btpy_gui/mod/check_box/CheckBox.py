


import tkinter as tk
from ..frame.Frame import Frame
from ..widget_composite.WidgetComposite import WidgetComposite
from ..switch_check.SwitchCheck import SwitchCheck

class CheckBox(WidgetComposite):

    def __init__(self, window, 
            TITLE:str,
            KEY_LIST:list[str] = []):
        super().__init__(window)
        self.__button_list:SwitchCheck = []
        if(KEY_LIST != []):
            self.__create_button_list(
                KEY_LIST)
        self.set_title(TITLE)

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
    
    def add_on_change_listener(self, 
            CALLBACK_X0:callable)->None:
        """
        Funcion que activa la callback
        cuando el listener detecta 
        los eventos on_change sobre
        los botones SwitchCheck.
        La callback recibe cero argumentos,
        por eso su nombre X0.
        """
        leng = self.__button_list
        for i in self.__button_list:
            self.__button_list[i]\
                .add_on_change_listener(
                    CALLBACK_X0
                )
            
    def set_content(self, KEY_LIST:str):
        self.__format_button()
        self.__create_button_list(KEY_LIST)
            
    def __format_button(self):
        button:SwitchCheck = None
        for button in self.__button_list:
            button.pack_forget()
        self.__button_list = []

    def __create_button_list(self, 
                TITLE_LIST:str):
        leng = len(TITLE_LIST)
        button = None
        for i in range(leng):
            button = SwitchCheck(
                self.widget, TITLE_LIST[i]
            )
            self.__button_list.append(
                button)
            button.pack(True)
        