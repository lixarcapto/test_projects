
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from PIL import Image, ImageTk

class SwiperImage:

    def __init__(self, widget, 
            TITLE:str = ""):
        self.widget = tk.Frame(
            widget,
            borderwidth=1,
            relief="solid"
        )
        self.path_image_list:list = []
        self.image_size_list:list[int] \
            = [0, 0]
        self.resize:bool = False
        self.index_image:int = 0
        self.__buffer_image = None
        self.label_title = None
        self.default_font = tkFont\
            .Font(
                family="Arial", 
                size=12
            )
        self.button_font = tkFont\
            .Font(
                family="Arial", 
                size=12,
                weight="bold"
            )
        self.label_counter = tk.Label(
            self.widget,
            font = self.default_font
        )
        self.label_image = tk.Label(
            self.widget,
            font = self.default_font,
            relief="solid",
            borderwidth=1
        )
        self.label_image.grid(
            row = 1,
            column= 1
        )
        self.label_counter.grid(
            row = 2,
            column= 1
        )
        self.__init_button_forward()
        self.__init_button_back()
        self.__init_label_title()
        self.set_title(TITLE)
        self.add_default_listener()

    def set_title(self, TITLE:str):
        self.label_title.config(
            text=TITLE
        )

    def add_default_listener(self):
        self.button_forward.config(
            command= self.__forward_image
        )
        self.button_back.config(
            command= self.__back_image
        )

    def __forward_image(self):
        leng = len(self.path_image_list)
        if(self.index_image < leng -1):
            self.index_image += 1
        self.__update_image()

    def __back_image(self):
        if(self.index_image > 0):
            self.index_image -= 1
        self.__update_image()

    def set_resize(self, 
            IMAGE_SIZE_LIST:list[int]):
        self.image_size_list \
            = IMAGE_SIZE_LIST
        self.resize = True
        self.__update_image()

    def set_content(self, 
            PATH_IMAGE_LIST:list[str]):
        self.path_image_list \
            = PATH_IMAGE_LIST
        self.__update_image()

    def set_index(self, INDEX:int):
        self.index_image = INDEX

    def get_index(self):
        return self.index_image

    def get_value(self):
        list_ = self.image_size_list
        return list_[self.index_image]
        
    def __set_path_image(self, PATH:str,
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
        self.label_image.config(
            image=imagen_tk)
        
    def __update_image(self):
        idx = self.index_image
        path = self.path_image_list[idx]
        if(self.resize):
            self.__set_path_image(
                path,
                self.image_size_list
            )
        else:
            self.__set_path_image(path)
        self.__update_counter()

    def __update_counter(self):
        leng = len(self.path_image_list)
        number = self.index_image + 1
        txt = f"{number} / {leng}"
        self.label_counter.config(
            text = txt
        )

    def __init_button_back(self):
        self.button_back = tk.Button(
            self.widget, 
            text = " < ",
            font = self.button_font,
            borderwidth=1,
            relief="solid"
        )
        self.button_back.grid(
            row = 1,
            column= 0,
            sticky="ns"
        )

    def __init_button_forward(self):
        self.button_forward = tk.Button(
            self.widget, 
            text = " > ",
            font =  self.button_font,
            borderwidth=1,
            relief="solid"
        )
        self.button_forward.grid(
            row = 1,
            column= 2,
            sticky="ns"
        )

    def __init_label_title(self):
        self.label_title = tk.Label(
            self.widget,
            font = self.default_font 
        )
        self.label_title.grid(
            row=0, 
            column=0, 
            sticky="ew",
            ipadx=5,
            ipady=5,
            columnspan=3
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