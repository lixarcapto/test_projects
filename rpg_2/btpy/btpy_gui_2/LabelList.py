
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

    def set_content(self, 
            TEXT_LIST:list[str]):
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
            label.grid(
                column=0,
                row=n
            )
            self.label_list.append(label)
            n += 1