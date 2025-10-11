

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ButtonIcon:

    def __init__(self, widget, 
            PATH:str = "", 
            RANGE_LIST = None
        ):
        self.widget = tk.Button(
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

    def set_tooltip(self, TITLE:str):
        self.__tooltip = ToolTip(
            self.widget,
            TITLE
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

    def add_listener(self, 
            CALLBACK_ARGS_X1)\
            ->None:
        self.widget.bind(
            "<Button-1>", 
            CALLBACK_ARGS_X1
        )

class ToolTip:
    """
    Crea una burbuja de información 
    para un widget de Tkinter.
    TODO: arreglar esto, lo creo GEMINI
    y no se que hace, y esta muy raro.
    """
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0
        self.size_font = 12
        self.background_color = "white"
        self.foreground_color = "black"
        def showtip(event):
            """Muestra la burbuja de información"""
            self.x, self.y = event.x_root, event.y_root
            self.showtip()

        def hidetip(event):
            """Esconde la burbuja de información"""
            self.hidetip()

        self.widget.bind("<Enter>", showtip)
        self.widget.bind("<Leave>", hidetip)

    def showtip(self):
        """Muestra la burbuja de información"""
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("anchor")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # Crea una ventana emergente
        self.tipwindow = tw = tk.Toplevel(self.widget)
        # Quita la decoración de la ventana
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(
            tw, 
            text=self.text, 
            justify=tk.LEFT,
            background="#ffffe0", 
            relief=tk.SOLID, 
            borderwidth=1,
            bg = self.background_color,
            fg = self.foreground_color,
            font=(
                "tahoma", 
                self.size_font, 
                "normal")
            )
        label.pack(ipadx=1)

    def hidetip(self):
        """Esconde la burbuja de información"""
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()