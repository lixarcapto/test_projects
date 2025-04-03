
import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ..label_image.LabelImage import LabelImage
from ..frame.Frame import Frame
from ..button.Button import Button

class SwiperStandard(WidgetStandard):

    """
    Este es un modulo estandard para
    crear otros modulos de tipo swiper
    o deslizadores para listas de elementos;
    este ofrece un widget
    que crea un titulo, botones de cambio
    y un contador.
    Para crear un nuevo swipper solo
    debe heredarse esta clase, añadir un 
    update_callback que obtenga el
    elemento actual con get_element
    y crear un widget para el center_frame
    que sera el wiget central.
    """

    def __init__(self, window, 
            TEXT:str = "")->None:
        super().__init__()
        self.__index:int = 0
        self.__element_list\
            :list[str] = []
        self.__is_cyclical:bool = False
        self.__update_callback = lambda e:e
        # OBJECTS -------------------------
        self.widget = None
        self.__label_title = None
        self.__button_max = None
        self.__button_back = None
        self.__frame_center = None
        self.__button_next = None
        self.__button_min = None
        self.__label_counter = None
        # CALLS ---------------------------
        self.__init_components(window)
        self.__add_listener_default()
        self.set_title(TEXT)

    def get_center_frame(self):
        return self.__frame_center
    
    def set_update_callback(self, 
            CALLBACK:callable):
        self.__update_callback = CALLBACK

    def get_value(self)->str:
        """
        Funcion que retorna la PATH de 
        la imagen seleccionada.
        """
        return self.__element_list\
            [self.__index]
    
    def set_is_cyclical(self, BOOL:bool)\
            ->None:
        self.__is_cyclical = BOOL

    def get_is_cyclical(self)->bool:
        return self.__is_cyclical
    
    def set_values_list(self, ARRAY):
        self.__element_list = ARRAY
        self.__update_element()

    def set_title(self, TEXT:str):
        self.__label_title.config(
            text = TEXT)
    
    def get_title(self)->str:
        return self.__label_title\
            .cget("text")
        
    # ------------------------------------
    # PRIVATE ----------------------------

    def __init_components(self, window):
        self.widget = Frame(window)
        self.widget.set_border(1)
        self.__label_title = tk.Label(
            self.widget.widget)
        self.__button_min = Button(
            self.widget, "<|")
        self.__button_back = Button(self.widget,
            "<<")
        self.__frame_center = Frame(
            self.widget)
        self.__frame_center.set_border(1)
        self.__button_next = Button(self.widget,
            ">>")
        self.__button_max = Button(
            self.widget, "|>")
        self.__label_counter = tk.Label(
            self.widget.widget)
        # dibujar --------------------------
        self.__label_title.grid(
            row=0, column=0, columnspan=3, 
            sticky="ns")
        self.__button_back.widget.grid(
            row=1, column=0, sticky="ns")
        self.__frame_center.widget.grid(
            row=1, column=1)
        self.__button_next.widget.grid(
            row=1, column=2, sticky="ns")
        self.__label_counter.grid(
            row=2, column=0, sticky="ns")
        
    def set_arroy_is_bold(self, BOOL:bool):
        self.__button_back.set_is_bold(BOOL)
        self.__button_next\
            .set_is_bold(BOOL)
        
    def __add_listener_default(self):
        self.__button_next.widget.config(
            command = self.__next_element)
        self.__button_back.widget.config(
            command = self.__back_element)

    def __next_element(self):
        leng = len(self.__element_list)
        if(self.__index < leng -1):
            self.__index += 1
        else:
            if(self.__is_cyclical):
                self.__index = 0
        self.__update_element()

    def __update_element(self):
        if(len(self.__element_list) > 0):
            self.__update_callback()
        self.__update_counter()
        
    def __update_counter(self):
        leng = len(self.__element_list) -1
        fraction = str(self.__index)\
        + " / " + str(leng)
        self.__label_counter.config(
            text = fraction)

    def __back_element(self):
        leng = len(self.__element_list)
        if(self.__index > 0):
            self.__index -= 1
        else:
            if(self.__is_cyclical):
                self.__index = leng - 1
        self.__update_element()