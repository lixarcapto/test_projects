


import tkinter as tk
import webbrowser
import tkinter.font as font

class Link():

    def __init__(self, window, 
            TITLE:str, URL:str):
        self.__hyperlink_URL:str = URL
        self.__was_clicked:bool = False
        self.tooltip = None
        self.widget = tk.Button(
                window,
                text= TITLE,
                bg = "white"
        )
        self.widget.config(
            font = font.Font(
                underline=True
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
    
    def grid(self, ROW, COLUMN, 
             STICKY = ""):
        self.widget.grid(
            row = ROW, column= COLUMN,
            sticky= STICKY,
            ipadx=5, ipady=5
        )

    def place(self, 
            LOCATION_X:int, 
            LOCATION_Y:int):
        self.widget.place(
            x=LOCATION_X,
            y=LOCATION_Y
        )

    def pack(self, 
            IS_EXPANDABLE:bool = False,
            SIDE_KEY:str = "left"):
        """
        SIDE_KEY:
        * left
        * top
        * right
        * bottom
        """
        if(IS_EXPANDABLE):
            self.widget.pack(
                fill=tk.BOTH, 
                expand=True,
                side = SIDE_KEY
            )
        else:
            self.widget.pack(
                side = SIDE_KEY
            )
        
    