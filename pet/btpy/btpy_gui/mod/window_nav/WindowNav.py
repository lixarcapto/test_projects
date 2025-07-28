

from ..window.Window import Window
from ..button_box.ButtonBox import ButtonBox
import tkinter as tk

class WindowNav(Window):

    def __init__(self, title):
        super().__init__(title)
        self.actual_key_frame = ""
        self.frame_dict = {}
        self.button_nav_bar = ButtonBox(
            self.widget,
            True,
            "nav"
        )
        text_list = list(
            self.frame_dict.keys())
        self.button_nav_bar.set_components(
            len(text_list),
            len(text_list)
        )
        self.button_nav_bar.set_content(
            text_list
        )
        self.__on_change_callback\
            :callable = None
        self.button_nav_bar.grid(0, 0)

    def __update_nav_bar(self):
        text_list = list(
            self.frame_dict.keys())
        self.button_nav_bar.set_components(
            len(text_list),
            len(text_list)
        )
        self.button_nav_bar.set_content(
            text_list
        )
        def fn(index):
            list_keys = list(
                self.frame_dict.keys())
            key = list_keys[index]
            self.select_frame(key)
        self.button_nav_bar\
            .add_single_listener(fn)
        
    def get_actual_key_frame(self)->str:
        return self.actual_key_frame
        
    def set_on_change_callback(self, 
            FUNCTION_ARGSX1:callable):
        self.__on_change_callback \
            = FUNCTION_ARGSX1

    def add_frame(self, KEY:str, FRAME):
        self.frame_dict[KEY] = FRAME
        self.__update_nav_bar()

    def delete_frame(self, KEY:str):
        if(KEY == self.actual_key_frame):
            self.frame_dict[KEY]\
                .margin.pack_forget()
            self.actual_key_frame = ""
        del(self.frame_dict[KEY])

    def select_frame(self, KEY:str):
        # quita el anterior frame
        if(self.actual_key_frame != ""):
            last_key = self.actual_key_frame
            self.frame_dict[last_key]\
                .margin.grid_forget()
        # muestra el nuevo frame
        self.frame_dict[KEY].grid(
            0, 1)
        self.actual_key_frame = KEY
        self.__on_change_callback()

