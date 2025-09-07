
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont

class CheckBox:

    def __init__(self, widget, 
            TITLE:str = ""):
        # 3. Crear los Radiobuttons y asociarlos a la variable
        self.widget = tk.Frame(
            widget
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
        self.__variable_list = []
        self.__key_list:list[str] = []
        self.button_list:list = []
        self.label_title = None
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
        self.__callback_args_x0 = None
        self.__init_label_title()
        self.set_title(TITLE)

    def __add_default_listener(self):
        for button in self.button_list:
            button.config(
                command = self
                    .__callback_args_x0
            )

    def add_change_listener(self, 
            CALLBACK_ARGS_X0:any):
        self.__callback_args_x0\
            = CALLBACK_ARGS_X0
        self.__add_default_listener()

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
            sticky= STICKY
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
        self.__key_list = KEY_LIST
        button = None
        self.__variable_list = []
        variable_ = None
        for i in range(len(KEY_LIST)):
            variable_ = tk.IntVar(
                value=0
            )
            button = ttk.Checkbutton(
                self.subframe,
                text=KEY_LIST[i],
                variable=variable_,
                onvalue=1,
                offvalue=0,
                style="TRadiobutton"
            )
            self.__variable_list.append(
                variable_
            )
            self.button_list.append(
                button
            )
        self.set_columns(1)

    def get_value(self):
        value_list = []
        variable:tk.IntVar = None 
        i = 0
        for variable in self.__variable_list:
            if(variable.get() == 1):
                value_list.append(
                    self.__key_list[i]
                )
            i += 1
        return value_list
    
    def set_value(self, 
            KEY_LIST:list[str]):
        variable:tk.IntVar = None 
        idx_list = []
        idx = 0
        for variable in self.__variable_list:
            variable.set(0)
        for key in KEY_LIST:
            idx = self.__key_list\
                .index(key)
            self.__variable_list[idx]\
                .set(1)

    def set_columns(self, COLUMNS):
        leng = len(self.button_list)
        x = 0
        y = 0
        for i in range(leng):
            self.button_list[i]\
                .grid(
                    column = x,
                    row = y,
                    sticky = "ew",
                    ipadx = 5
                )
            x += 1
            if(x >= COLUMNS):
                x = 0
                y += 1
