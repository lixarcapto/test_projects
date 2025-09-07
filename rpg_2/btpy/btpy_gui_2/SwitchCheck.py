
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class SwitchCheck:

    def __init__(self, widget, TITLE:str):
        self.__variable = tk\
            .IntVar(value=0)
        self.widget = tk.Frame(
            widget,
            borderwidth=1,
            relief="solid" 
        )
        self.default_font = tkFont\
            .Font(
                family="Arial", 
                size=12
            )
        self.label_title = None
        self.checkbox = ttk.Checkbutton(
            self.widget,
            variable=self.__variable,
            offvalue=0,
            onvalue=1
        )
        self.checkbox.grid(
            row=0, 
            column=1, 
            sticky="ew"
        )
        self.__init_label_title()
        self.set_title(TITLE)

    def set_title(self, TEXT:str):
        self.label_title.config(
            text = TEXT
        )

    def get_title(self):
        return self.label_title\
            .cget("text")

    def __init_label_title(self):
        self.label_title = tk.Label(
            self.widget,
            anchor="w",
            font = self.default_font
        )
        self.label_title.grid(
            row=0, 
            column=0, 
            sticky="ew",
            ipadx=5,
            ipady=5
        )

    def get_value(self):
        if(self.__variable.get()):
            return True
        else:
            return False

    def set_value(self, BOOL:bool):
        self.__variable.set(BOOL)

    def grid(self, ROW, COLUMN, 
             STICKY = ""):
        self.widget.grid(
            row = ROW, column= COLUMN,
            sticky= STICKY
        )

    def place(self, 
            LOCATION_X:int, 
            LOCATION_Y:int):
        self.widget.place(
            x=LOCATION_X,
            y=LOCATION_Y
        )