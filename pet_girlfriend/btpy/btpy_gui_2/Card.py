

from tkinter import ttk
import tkinter.font as tkFont
import tkinter as tk
from PIL import Image, ImageTk

class Card:

    def __init__(self, widget, 
            TEXT = ""):
        self.__path = ""
        self.__buffer_image = None
        self.default_font = tkFont\
            .Font(
                family="Arial", 
                size=12
            )
        self.title_font = tkFont\
            .Font(
                family="Arial", 
                size=14,
                weight="bold"
            )
        self.widget = tk.Frame(
            widget,
            relief="solid",
            borderwidth=1
        )
        self.label_title = tk.Label(
            self.widget,
            font = self.title_font,
            background="white"
        )
        self.image = tk.Label(
            self.widget
        )
        self.label_description = tk.Label(
            self.widget,
            background="white",
            font = self.default_font
        )
        self.sort_vertically()

    def sort_vertically(self):
        self.label_title.grid(
            row=0, column=0, 
            sticky="nswe"
        )
        self.image.grid(
            row=1, column=0
        )
        self.label_description.grid(
            row=2, column=0, 
            sticky="nswe"
        )

    def set_title(self, TEXT:str):
        self.label_title.config(
            text = TEXT
        )

    def set_description(self, TEXT:str):
        self.label_description.config(
            text = TEXT
        )

    def set_path_image(self, PATH:str,
            RANGE_SIZE:list[int] = None):
        self.__path = PATH
        imagen_pil = Image.open(PATH)
        if(RANGE_SIZE != None):
            imagen_pil = imagen_pil\
                    .resize((
                RANGE_SIZE[0], 
                RANGE_SIZE[1]
            ))
        photo_image = tk.PhotoImage(
            imagen_pil
        )
        imagen_tk = ImageTk.PhotoImage(
            imagen_pil)
        self.__buffer_image = imagen_tk
        self.image.config(
            image=imagen_tk
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