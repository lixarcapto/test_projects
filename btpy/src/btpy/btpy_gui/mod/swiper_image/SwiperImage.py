
import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ..label_image.LabelImage import LabelImage
from ..frame.Frame import Frame
from ..button.Button import Button

class SwiperImage(WidgetStandard):

    """
    Este es un modulo que crea un 
    deslizador de imagenes de una manera
    facil y comoda.
    """

    def __init__(self, window, 
            TEXT:str = "")->None:
        super().__init__()
        self.__index:int = 0
        self.__path_image_list\
            :list[str] = []
        self.is_cyclical:bool = False
        # OBJECTS -------------------------
        self.widget = None
        self.__label_title = None
        self.__button_back = None
        self.__label_image = None
        self.__button_next = None
        self.__label_counter = None
        # CALLS ---------------------------
        self.__init_components(window)
        self.__add_default_listener()
        self.set_title(TEXT)

    def get_value(self)->str:
        """
        Funcion que retorna la PATH de 
        la imagen seleccionada.
        """
        return self.self.__path_image_list\
            [self.__index]

    def set_title(self, TEXT:str):
        self.__label_title.config(
            text = TEXT)
    
    def get_title(self)->str:
        return self.__label_title\
            .cget("text")
        
    def set_image_size(self, WIDTH:int,
            HEIGHT:int)->None:
        self.__label_image.set_size(WIDTH,
            HEIGHT)

    def set_path_image_list(self, 
            PATH_LIST:list[str])->None:
        self.__path_image_list = PATH_LIST
        self.__update_image()

    def pack(self, MARGIN = 0)->None:
        self.widget.pack(MARGIN)
        self.__label_title.grid(
            row=0, column=0, columnspan=3, 
            sticky="ns")
        self.__button_back.widget.grid(
            row=1, column=0, sticky="ns")
        self.__label_image.widget.grid(
            row=1, column=1)
        self.__button_next.widget.grid(
            row=1, column=2, sticky="ns")
        self.__label_counter.grid(
            row=2, column=0, sticky="ns")
        
    def unpack(self):
        self.__label_title.grid_forget()
        self.__button_back.widget\
            .grid_forget()
        self.__label_image.widget\
            .grid_forget()
        self.__button_next.widget\
            .grid_forget()
        self.__label_counter.grid_forget()
        self.widget.widget.pack_forget()
        
    # ------------------------------------
    # PRIVATE ----------------------------

    def __init_components(self, window):
        self.widget = Frame(window)
        self.widget.set_border(1)
        self.__label_title = tk.Label(
            self.widget.widget)
        self.__button_back = Button(self.widget,
            "<<")
        self.__button_back.set_is_bold(True)
        self.__label_image = LabelImage(
            self.widget)
        self.__label_image.set_border(1)
        self.__button_next = Button(self.widget,
            ">>")
        self.__button_next\
            .set_is_bold(True)
        self.__label_counter = tk.Label(
            self.widget.widget)

    def __add_default_listener(self):
        self.__button_back.widget.config(
            command = self.__back_image)
        self.__button_next.widget.config(
            command = self.__next_image)

    def __next_image(self):
        leng = len(self.__path_image_list)
        if(self.__index < leng -1):
            self.__index += 1
        else:
            if(self.is_cyclical):
                self.__index = 0
        self.__update_image()

    def __update_image(self):
        path =  self.__path_image_list\
            [self.__index]
        self.__label_image.set_path_image(
            path)
        self.__update_counter()
        
    def __update_counter(self):
        leng = len(self.__path_image_list) -1
        fraction = str(self.__index)\
        + " / " + str(leng)
        self.__label_counter.config(
            text = fraction)

    def __back_image(self):
        leng = len(self.__path_image_list)
        if(self.__index > 0):
            self.__index -= 1
        else:
            if(self.is_cyclical):
                self.__index = leng - 1
        self.__update_image()
