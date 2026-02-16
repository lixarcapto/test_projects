

import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from PIL import Image, ImageTk
import os

class SwitchImageBox:

    def __init__(self, widget, 
            TITLE:str = ""):
        self.widget = tk.Frame(
            widget,
            borderwidth=1,
            relief="solid"
        )
        self.switch_list = []

    def set_seleted_image_path(self,
            PATH):
        widget:SwitchIcon = None
        for widget in self.switch_list:
            widget.set_seleted_image_path(
                PATH
            )

    def set_unseleted_image_path(self,
            PATH):
        widget:SwitchIcon = None
        for widget in self.switch_list:
            widget.set_unseleted_image_path(
                PATH
            )

    def set_columns(self, COLUMNS):
        leng = len(self.switch_list)
        x = 0
        y = 0
        for i in range(leng):
            self.switch_list[i]\
                .grid(x, y,"nsew"
                )
            x += 1
            if(x >= COLUMNS):
                x = 0
                y += 1

    def get_values(self):
        values_list = []
        widget:SwitchIcon = None
        for widget in self.switch_list:
            values_list.append(
                widget.get_value()
            )
        return values_list

    def set_components(self, quantity):
        widget = None
        self.switch_list:SwitchIcon = []
        for i in range(quantity):
            widget = SwitchIcon(
                self.widget
            )
            self.switch_list.append(
                widget
            )
        self.set_columns(1)

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







class SwitchIcon:

    def __init__(self, widget, 
            TITLE:str = ""):
        self.widget = tk.Button(
            widget
        )
        self.__path_img_true:str = ""
        self.__path_img_false:str = ""
        self.__is_seleted:bool = False
        self.__range_size\
            :list[int] = None
        self.__buffer_image = None
        self.__tooltip = None
        self.__add_default_listener()
        self.set_tooltip(TITLE)

    def set_range_size(self, 
            RANGE_LIST:list[int]):
        self.__range_size = RANGE_LIST
        self.__update_image()

    def __add_default_listener(self):
        def fn():
            if(self.__is_seleted):
                self.__is_seleted = False
            else:
                self.__is_seleted = True
            self.__update_image()
        self.widget.config(command = fn)

    def set_tooltip(self, TITLE:str):
        self.__tooltip = ToolTip(
            self.widget,
            TITLE
        )

    def __update_image(self):
        if(self.__is_seleted):
            self.__set_path_image(
                self.__path_img_true
            )
        else:
            self.__set_path_image(
                self.__path_img_false
            )

    def set_seleted_image_path(self, 
            PATH:str):
        self.__path_img_true = PATH
        self.__update_image()
    
    def get_value(self):
        return self.__is_seleted

    def set_unseleted_image_path(self, 
            PATH:str):
        self.__path_img_false = PATH
        self.__update_image()

    def set_size(self, 
            RANGE_SIZE:list[int]):
        self.__set_path_image(
            self.__path,
            RANGE_SIZE
        )

    def __set_path_image(self, PATH:str,
            RANGE_SIZE:list[int] = None):
        self.__path = PATH
        if(not os.path.exists(self.__path)):
            return None
        imagen_pil = Image.open(PATH)
        if(self.__range_size != None):
            imagen_pil = imagen_pil\
                    .resize((
                self.__range_size[0], 
                self.__range_size[1]
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
            