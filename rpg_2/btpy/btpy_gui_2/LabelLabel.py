
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont

class LabelLabel:

    def __init__(self, widget, TITLE:str):
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
        self.label_title = tk.Label(
            self.widget,
            font = self.default_font,
            borderwidth=1,
            relief="solid"
        )
        self.label_title.grid(
            row = 0,
            column= 0
        )
        self.label_value = tk.Label(
            self.widget,
            font = self.default_font,
            background="white",
            borderwidth=1,
            relief="solid"
        )
        self.label_value.grid(
            row = 0,
            column= 1
        )
        self.set_title(TITLE)

    def set_title(self, TITLE:str):
        self.label_title.config(
            text = f" {TITLE} "
        )

    def set_value(self, TITLE:str):
        self.label_value.config(
            text = f" {TITLE} "
        )

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