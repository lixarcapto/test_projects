
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class ButtonBox:

    def __init__(self, widget, 
            TITLE:str = ""):
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
        self.container = tk.Frame(
            self.widget
        )
        self.container.grid(
            row = 1,
            column= 0,
            sticky= "news"
        )
        self.button_list:list = []
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
            font = self.default_font,
            borderwidth=1,
            relief="solid" 
        )
        self.label_title.grid(
            row=0, 
            column=0, 
            sticky="ew",
            ipadx=5,
            ipady=5
        )

    def set_components(self, 
            KEY_LIST:list[str]
        ):
        button = None
        for k in KEY_LIST:
            button = tk.Button(
                self.container,
                text = k,
                font = self.default_font
            )
            self.button_list.append(
                button)
        self.set_columns(1)
            
    def set_columns(self, COLUMNS):
        leng = len(self.button_list)
        x = 0
        y = 0
        for i in range(leng):
            self.button_list[i]\
                .grid(
                    column = x,
                    row = y,
                    sticky = "nsew"
                )
            x += 1
            if(x >= COLUMNS):
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

    def add_listener_to(self, INDEX:int,
            CALLBACK:any):
        button = self.button_list\
            [INDEX]
        button.config(
            command = CALLBACK
        )

    def add_single_listener(self, 
                CALLBACK_ARGS_X1:callable):
        """
        Esta funcion recibe una callback
        que ejecutara el boton cada
        vez que se presione enviando
        el indice del boton
        como argumento. Sirve para
        crear un listener unico para
        todos los botones.
        """
        button = None
        for i in range(len(self.button_list)):
            button = self.button_list[i]
            def aux(key):
                def fn():
                    CALLBACK_ARGS_X1(key)
                return fn
            button.config(
                command = aux(i)
            )
            self.button_list[i] = button