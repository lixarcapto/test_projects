


import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
import webbrowser
import tkinter.font as font

class Link(WidgetStandard):

    def __init__(self, window, 
            TITLE:str, URL:str):
        super().__init__()
        self.__hyperlink_URL:str = ""
        self.__was_clicked:bool = False
        self.widget = tk.Button(
                window.widget,
                text= TITLE
        )
        self.widget.config(
            font = font.Font(
                underline=True,
                weight="bold"
        ))
        self.widget.config(
            fg = "#0D0AE1")
        self.__add_default_listener()
        self.set_hyperlink_URL(URL)

    def __add_default_listener(self):
        self.widget.config(
            command = self\
                .__react_to_click
        )

    def get_was_clicked(self):
        return self.__was_clicked

    def __react_to_click(self):
        webbrowser.open(
                self.__hyperlink_URL)
        self.widget.config(fg = "#7C60B0")
        self.__was_clicked = True

    def set_title(self, TEXT:str)->None:
        self.widget.config(text = TEXT)

    def get_title(self)->str:
        return self.widget.cget("text")

    def set_hyperlink_URL(self, URL:str):
        self.__hyperlink_URL = URL

    def get_hyperlink_URL(self)->str:
        return self.__hyperlink_URL
        
    