


import tkinter as tk
from ..frame.Frame import Frame
from ..widget_composite.WidgetComposite import WidgetComposite
from ..switch_check.SwitchCheck import SwitchCheck

class CheckBox(WidgetComposite):

    def __init__(self, window, title:str,
            key_list:list[str]):
        super().__init__(window)
        self.__button_list = []
        self.set_title(title)
        self.create_button_list(key_list)

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
    
    def create_button_list(self, 
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
        