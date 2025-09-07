
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class RadioBox:

    def __init__(self, widget, 
            TITLE:str = ""):
        # 3. Crear los Radiobuttons y asociarlos a la variable
        self.widget = tk.Frame(
            widget
        )
        self.__variable = tk.StringVar(
            self.widget, 
            value=""
        )
        self.subframe = tk.Frame(
            self.widget,
            borderwidth=1,
            relief="solid" 
        )
        self.subframe.grid(
            row=1, 
            column=0, 
            sticky="news"
        )
        self.button_list:list = []
        self.default_font = tkFont\
            .Font(
                family="Arial", 
                size=12
            )
        self.default_style = ttk.Style()
        self.default_style.configure(
            "TRadiobutton", 
            font=self.default_font
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

    def set_font_family(self, 
            FONT_FAMILY_KEY:str):
        self.default_font.config(
            size = FONT_FAMILY_KEY
        )
        self.default_style.configure(
            "TRadiobutton", 
            font=self.default_font
        )

    def set_font_size(self, SIZE):
        estilo = ttk.Style()
        self.default_font.config(
            size = SIZE
        )
        self.default_style.configure(
            "TRadiobutton", 
            font=self.default_font
        )

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

    def set_content(self, 
            TEXT_LIST:list[str]):
        leng = len(self.button_list)
        for i in range(leng):
            self.button_list[i]\
                .config(
                    text = TEXT_LIST[i]
                )

    def set_components(self, 
            KEY_LIST:list[str]):
        button = None
        for i in range(len(KEY_LIST)):
            button = ttk.Radiobutton(
                self.subframe, 
                text=KEY_LIST[i], 
                variable=self.__variable, 
                value=KEY_LIST[i]
            )
            self.button_list.append(
                button
            )
        self.set_columns(1)

    def get_value(self):
        return self.__variable.get()
    
    def set_value(self, KEY:str):
        self.__variable.set(KEY)

    def set_columns(self, COLUMNS):
        leng = len(self.button_list)
        x = 0
        y = 0
        for i in range(leng):
            self.button_list[i]\
                .grid(
                    column = x,
                    row = y,
                    sticky = "ew"
                )
            x += 1
            if(x >= COLUMNS):
                x = 0
                y += 1
