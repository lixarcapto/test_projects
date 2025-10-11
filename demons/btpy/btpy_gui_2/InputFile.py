

import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from tkinter import filedialog

class InputFile:

    def __init__(self, widget, TITLE:str):
        self.widget = tk.Frame(
            widget,
            borderwidth=1,
            relief="solid"
        )
        self.__folder_path:str = ""
        self.__file_types = None
        self.default_font = tkFont\
            .Font(
                family="Arial", 
                size=12
            )
        self.label_title = None
        self.entry = tk.Entry(
            self.widget,
            font = self.default_font
        )
        self.entry.grid(
            row = 0,
            column = 2
        )
        self.default_font = tkFont\
            .Font(
                family="Arial", 
                size=12
            )
        self.default_style = ttk.Style()
        self.default_style.configure(
            "TButton", 
            font=self.default_font
        )
        self.button_search = ttk.Button(
            self.widget,
            text = "Search",
            style="TButton"
        )
        self.button_search.grid(
            row = 0,
            column = 1
        )
        self.__init_label_title()
        self.__add_default_listener()
        self.set_character_width(30)
        self.set_title(TITLE)

    def set_file_types(self, KEY:str):
        if(KEY == "TEXT"):
            self.__file_types = (
                ("Imágenes (DOCX, PDF, TXT)", "*.docx;*.pdf;*.txt"),
                ("Todos los archivos", "*.*")
            )
        elif(KEY == "FOLDER"):
            self.__file_types = None
        elif(KEY == "IMAGE"):
            self.__file_types = (
                ("Imágenes (SVG, PNG, JPG, JPEG, GIF)", "*.svg;*.png;*.jpg;*.jpeg;*.gif"),
                ("Todos los archivos", "*.*")
            )

    def set_folder_path(self, PATH:str):
        self.__folder_path = PATH

    def __add_default_listener(self):
        self.button_search.config(
                command= self.__search_file
            )

        
    def __search_file(self):
        if(self.__file_types == None):
            path = filedialog.askdirectory(
                    title=self.label_title\
                        .cget("text"),
                    initialdir= self.__folder_path
                )
            self.set_value(path)
        else:
            path = filedialog.askopenfilename(
                    title=self.label_title\
                        .cget("text"),
                    initialdir= self.__folder_path,
                    filetypes = self.__file_types
                )
            self.set_value(path)

    def set_title(self, TEXT:str):
        self.label_title.config(
            text = TEXT
        )

    def set_button_text(self, TEXT:str):
        self.button_search.config(
            text = TEXT
        )

    def __init_label_title(self):
        self.label_title = tk.Label(
            self.widget,
            anchor="w",
            font = self.default_font
        )
        self.label_title.grid(
            row=0, 
            column=0, 
            sticky="nsew",
            ipadx=5,
            ipady=5
        )

    def get_value(self)->str:
        return self.entry.get()

    def set_value(self, TEXT:str):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, TEXT)

    def set_character_width(self, 
            CHAR_NUMBER:int):
        self.entry.config(
            width = CHAR_NUMBER)

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