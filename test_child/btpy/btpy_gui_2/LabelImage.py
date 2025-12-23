
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class LabelImage:

    def __init__(self, widget, 
            PATH:str = "", 
            RANGE_LIST = None
        ):
        self.widget = tk.Label(
            widget
        )
        self.__path = PATH
        self.__buffer_image = None
        self.__tooltip = None
        if(PATH != ""):
            self.set_path_image(
                PATH,
                RANGE_LIST
            )


    def set_size(self, 
            RANGE_SIZE:list[int]):
        self.set_path_image(
            self.__path,
            RANGE_SIZE
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
        self.widget.config(
            image=imagen_tk)
        
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