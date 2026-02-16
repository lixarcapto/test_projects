

import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class Table:

    def __init__(self, widget, 
            TITLE:str):
        self.widget = tk.Frame(
            widget,
            borderwidth=1,
            relief="solid"
        )
        self.columns = 0
        self.table_matrix = []
        self.default_font = tkFont\
            .Font(
                family="Arial", 
                size=12
            )

    def set_row_dict_list(self, row_dict):
        self.__format()
        size = 0
        for k in row_dict:
            size = len(row_dict[k])
            break
        self.set_components(size + 1)
        list_ = []
        for k in row_dict:
            list_ = [k] + row_dict[k]
            self.__create_row(list_)
        self.__draw_components()

    def __format(self):
        for widget_list in self.table_matrix:
            for widget in widget_list:
                widget.grid_forget()
        self.table_matrix = []
            

    def set_components(self, COLUMNS):
        self.__format()
        self.columns = COLUMNS

    def __create_row(self, text_list):
        label = None
        label_list = []
        for i in range(self.columns):
            if(i >= len(text_list)):
                continue
            label = self.__create_label_cell(
                text_list[i]
            )
            label_list.append(label)
        self.table_matrix.append(
            label_list)
        
    def __create_label_cell(self, TEXT):
        label = tk.Label(
            self.widget,
            text = f"  {TEXT}  ",
            relief = "solid",
            border= 1,
            bg = "white",
            font = self.default_font
        )
        return label
        
    def __draw_components(self):
        x = 0
        y = 0
        for widget_list in self.table_matrix:
            for widget in widget_list:
                widget.grid(
                    row = y, 
                    column = x,
                    sticky = "ew"
                )
                x += 1
            x = 0
            y += 1

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