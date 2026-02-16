
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont

class LabelList:

    def __init__(self, widget, TITLE:str):
        self.widget = tk.Frame(
            widget,
            borderwidth=1,
            relief="solid"
        )
        self.__symbol = ")"
        self.default_font = tkFont\
            .Font(
                family="Arial", 
                size=12
            )
        self.label_title = tk.Label(
            self.widget,
            font = self.default_font,
            borderwidth=1,
            relief="solid"
        )
        self.label_title.grid(
            row = 0, 
            column= 0,
            sticky= "we"
        )
        self.label_list = []
        self.__content_list:list[str] = []
        self.set_title(TITLE)

    def __format(self):
        for label in self.label_list:
            label.grid_forget()
        self.label_list = []

    def set_symbol(self, SYMBOL:str):
        self.__symbol = SYMBOL
        self.set_content(
            self.__content_list
        )

    def set_title(self, TITLE:str):
        self.label_title.config(
            text = TITLE
        )

    def grid(self, ROW, COLUMN, 
             STICKY = ""):
        self.widget.grid(
            row = ROW, column= COLUMN,
            sticky= STICKY,
            padx=3, pady=3
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

    def set_content(self, 
            TEXT_LIST:list[str]):
        self.__format()
        self.__content_list = TEXT_LIST
        label = None
        n = 1
        text_ = ""
        for e in TEXT_LIST:
            text_ = f"{n}{self.__symbol} {e}"
            label = tk.Label(
                self.widget,
                text = text_,
                anchor="w",
                background="white",
                font = self.default_font
            )
            self.label_list.append(label)
            n += 1
        self.set_columns(1)

    def set_columns(self, COLUMNS):
        leng = len(self.label_list)
        x = 0
        y = 0
        for i in range(leng):
            self.label_list[i]\
                .grid(
                    column = x,
                    row = y,
                    sticky = "ew"
                )
            x += 1
            if(x >= COLUMNS):
                x = 0
                y += 1