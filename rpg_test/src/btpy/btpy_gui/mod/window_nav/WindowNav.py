

from ..window.Window import Window
from ..button_box.ButtonBox import ButtonBox
import tkinter as tk

class WindowNav(Window):

    def __init__(self, title):
        super().__init__(title)
        self.actual_key_frame = ""
        self.button_nav_bar = None
        self.__frame_dict = {}
        self.button_nav_bar = ButtonBox(
            self.widget,
            True,
            "nav",
            list(self.__frame_dict.keys())
        )
        self.button_nav_bar.margin.pack(
            anchor = "nw", fill ="x"
        )

    def update_nav_bar(self):
        self.button_nav_bar.set_components(
            list(self.__frame_dict.keys())
        )
        def fn(key):
            self.select_frame(key)
        self.button_nav_bar\
            .add_single_listener(fn)

    def add_frame(self, KEY:str, FRAME):
        self.__frame_dict[KEY] = FRAME
        self.update_nav_bar()

    def start(self):
        self.widget.mainloop()

    def delete_frame(self, KEY:str):
        if(KEY == self.actual_key_frame):
            self.__frame_dict[KEY]\
                .margin.pack_forget()
            self.actual_key_frame = ""
        del(self.__frame_dict[KEY])

    def select_frame(self, KEY:str):
        # quita el anterior frame
        if(self.actual_key_frame != ""):
            last_key = self.actual_key_frame
            self.__frame_dict[last_key]\
                .margin.pack_forget()
        # muestra el nuevo frame
        self.__frame_dict[KEY].pack()
        self.actual_key_frame = KEY

