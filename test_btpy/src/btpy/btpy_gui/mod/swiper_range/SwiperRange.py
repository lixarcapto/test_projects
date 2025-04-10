

import tkinter as tk
from ..widget_composite.WidgetComposite import WidgetComposite
from ....btpy_maths.mod.set_in_range.set_in_range import*
from ..button.Button import Button
from ..frame.Frame import Frame
import tkinter as tk

class SwiperRange(WidgetComposite):

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
        super().__init__(window, True)
        self.__value:int|float = 0
        self.__increment = 1
        self.__range_list:list = [0, 1]
        self.__button_back = None
        self.__label_number = None
        self.__button_next = None
        self.__init_components(window)
        self.__init_default_listener()
        self.set_title(TEXT)
        self.set_values_list(RANGE_LIST)
        self.__update_label_number()

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
        self.__add_increment_listener()
        self.__add_decrement_listener()

    def __update_label_number(self):
        self.__label_number.config(
            text = f" {self.__value} ")

    def __init_components(self, window):
        self.__button_back = tk.Button(
            self.widget, text = "<<")
        self.__label_number = tk.Label(
            self.widget)
        self.__label_number.config(
            bg = "white",
            borderwidth = 1,
            relief= "solid"
        )
        self.__button_next = tk.Button(
            self.widget, text = ">>")
        # dibujar -------------------------
        self.__button_back.grid(
            row=0, column=2)
        self.__label_number.grid(
            row=0, column=3, 
            sticky="nsew", 
        )
        self.__button_next.grid(
            row=0, column=4, 
        )
        
    def __add_increment_listener(self):
        self.__button_next.config(
            command=self.increment)
        
    def increment(self):
        result = self.__value + self\
            .__increment
        maximum = self.__range_list[1]
        if(maximum > result):
            self.__value = result
        else:
            self.__value = maximum
        self.__update_label_number()
        
    def __add_decrement_listener(self):
        self.__button_back.config(
            command=self.decrement)
        
    def decrement(self):
        result = self.__value - self\
            .__increment
        minimum = self.__range_list[0]
        if(minimum < result):
             self.__value = result
        else:
            self.__value = minimum
        self.__update_label_number()