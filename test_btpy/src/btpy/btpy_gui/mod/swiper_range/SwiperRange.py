

import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ....btpy_maths.mod.set_in_range.set_in_range import*
from ..button.Button import Button
from ..frame.Frame import Frame

class SwiperRange(WidgetStandard):

    """
    Esta modulo crea un widget de tipo
    swiper para seleccionar un numero
    dentro de un rango especifico.
    Sus funciones son:
    * set_title: para asignar un titulo.
    * get_title: para obtener el titulo.
    * set_increment: para asignar un 
        incremento al cambio de los 
        numeros.
    * get_increment: obtiene el valor
        de incremento actual.
    * set_value: asigna un valor al 
        widget dentro del rango.
    * get_value: retorna el valor actual
        del widget.
    * set_values_list: asigna un rango
        determinado en formato lista 
        al widget.
    * pack: dibuja el componente dentro
        de su contenedor.
    * unpack: quita el componente de su
        contenedor.
    """

    def __init__(self, window, TEXT = "",
            RANGE_LIST:list[int] = [0, 1]):
        super().__init__()
        self.widget = None
        self.__value:int|float = 0
        self.__increment = 1
        self.__range_list:list = [0, 1]
        self.__label_title = None
        self.__button_min = None
        self.__button_back = None
        self.__label_number = None
        self.__button_next = None
        self.__button_max = None
        self.__init_components(window)
        self.__init_default_listener()
        self.set_title(TEXT)
        self.set_values_list(RANGE_LIST)
        self.__update_label_number()

    def set_title(self, TEXT:str):
        self.__label_title.config(text = TEXT)

    def get_title(self)->str:
        return self.__label_title.cget("text")

    def get_increment(self)->int|float:
        return self.__increment
    
    def set_increment(self, 
            INCREMENT:int|float)-> None:
        self.__increment = INCREMENT

    def get_value(self)->int|float:
        return self.__value
    
    def set_value(self, NUMBER:int|float):
        r = set_in_range(NUMBER,
            self.__range_list)
        self.__value = r

    def set_values_list(self, RANGE_LIST
            :list[int|float]):
        self.__range_list = RANGE_LIST
        self.__value = RANGE_LIST[0]
        self.__update_label_number()

    # -------------------------------------
    # PRIVATE ------------------------------
        
    def __init_default_listener(self):
        self.__add_set_min_listener()
        self.__add_increment_listener()
        self.__add_decrement_listener()
        self.__add_set_max_listener()

    def __update_label_number(self):
        self.__label_number.config(
            text = f" {self.__value} ")
        self.__update_max_and_min()

    def __update_max_and_min(self):
        maxstr = str(self.__range_list[1])
        minstr = str(self.__range_list[0])
        self.__button_max.set_title(maxstr)
        self.__button_min.set_title(minstr)

    def __init_components(self, window):
        self.widget = Frame(window)
        self.widget.set_border(1)
        self.__label_title = tk.Label(
            self.widget.widget)
        self.__button_min = Button(
            self.widget)
        self.__button_back = Button(
            self.widget, text = "<<")
        self.__label_number = tk.Label(
            self.widget.widget
        )
        self.__label_number.config(
            bg = "white",
            borderwidth = 1,
            relief= "solid"
        )
        self.__button_next = Button(
            self.widget, text = ">>")
        self.__button_max = Button(
            self.widget)
        # dibujar ------------------------
        inner_margin_y = 3
        self.__label_title.grid(
            row=0, column=0, 
            padx=3, 
            pady=inner_margin_y
        )
        self.__button_min.widget.grid(
            row=0, column=1, 
            pady=inner_margin_y
        )
        self.__button_back.widget.grid(
            row=0, column=2, 
            pady=inner_margin_y
        )
        self.__label_number.grid(
            row=0, column=3, sticky="nsew", 
            pady=inner_margin_y
        )
        self.__button_next.widget.grid(
            row=0, column=4, 
            pady=inner_margin_y
        )
        self.__button_max.widget.grid(
            row=0, column=5, 
            pady=inner_margin_y
        )
        
    def __add_increment_listener(self):
        def increment():
            result = self.__value + self\
                .__increment
            maximum = self.__range_list[1]
            if(maximum > result):
                self.__value = result
            else:
                self.__value = maximum
            self.__update_label_number()
        self.__button_next.widget.config(
            command=increment)
        
    def __add_set_max_listener(self):
        def fn():
            self.__value = self\
                .__range_list[1]
            self.__update_label_number()
        self.__button_max.widget.config(
            command=fn)

    def __add_set_min_listener(self):
        def fn():
            self.__value = self\
                .__range_list[0]
            self.__update_label_number()
        self.__button_min.widget.config(
            command=fn)
        
    def __add_decrement_listener(self):
        def decrement():
            result = self.__value - self\
                .__increment
            minimum = self.__range_list[0]
            if(minimum < result):
                self.__value = result
            else:
                self.__value = minimum
            self.__update_label_number()
        self.__button_back.widget.config(
            command=decrement)