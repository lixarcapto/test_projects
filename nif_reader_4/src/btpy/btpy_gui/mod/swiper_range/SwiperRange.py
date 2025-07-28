

import tkinter as tk
from ..widget_composite.WidgetComposite import WidgetComposite
from ....btpy_maths.mod.set_in_range.set_in_range import*
from ..button.Button import Button
from ..frame.Frame import Frame
from ..button.Button import Button
import tkinter as tk
from tkinter import font

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
        self.__range_list:list = [0, 1]
        self.__button_back = None
        self.__label_number = None
        self.__button_next = None
        self.__margin_value = 3
        self.__change_callback = None
        self.__init_components(window)
        self.__init_default_listener()
        self.set_title(TEXT)
        self.set_content(RANGE_LIST)
        self.__update_label_number()

    def get_value(self)->int|float:
        return self.__value
    
    def set_value(self, NUMBER:int|float):
        r = set_in_range(NUMBER,
            self.__range_list)
        self.__value = r
        self.__identify_enabled_buttons()

    def add_listener(self, CALLBACK):
        self.__change_callback = CALLBACK

    def set_content(self, RANGE_LIST
            :list[int|float]):
        """
        Funcion que recibe un rango en
        formato lista que servira
        como rango de numeros 
        que pueden seleccionarse.
        """
        self.__range_list = RANGE_LIST
        self.__value = RANGE_LIST[0]
        self.__update_label_number()
        self.__identify_enabled_buttons()

    # -------------------------------------
    # PRIVATE ------------------------------
        
    def __init_default_listener(self):
        self.__add_increment_listener()
        self.__add_decrement_listener()

    def __update_label_number(self):
        margin = " " * self.__margin_value
        text_ = margin\
            + str(self.__value) + margin
        self.__label_number.config(
            text = text_
        )

    def __init_components(self, window):
        font_ = font.Font(
            size=10, weight="bold")
        self.__button_back = Button(
            self.widget, 
            " < "
        )
        self.__button_back\
            .set_background_color(
                "#9b9b9b")
        self.__button_back\
            .set_foreground_color(
                "#FFFFFF")
        self.__button_back.set_font(
            font_)
        self.__label_number = tk.Label(
            self.widget)
        self.__label_number.config(
            bg = "white",
            borderwidth = 1,
            relief= "solid"
        )
        self.__button_next = Button(
            self.widget, 
            " > "
        )
        self.__button_next\
            .set_background_color(
                "#9b9b9b")
        self.__button_next\
            .set_foreground_color(
                "#FFFFFF")
        self.__button_next.set_font(font_)
        # dibujar -------------------------
        self.__button_back.grid(2, 0)
        self.__label_number.grid(
            row=0, column=3, 
            sticky="nsew", 
        )
        self.__button_next.grid(4, 0)
        
    def __add_increment_listener(self):
        self.__button_next.add_listener(
            self.__increment)
        
    def __identify_enabled_buttons(self):
        maximum = self.__range_list[1]
        minimum = self.__range_list[0]
        if(self.__value == maximum):
            self.__button_next.disable()
        if(self.__value != maximum):
            self.__button_next.enable()
        if(self.__value == minimum):
             self.__button_back.disable()
        if(self.__value != minimum):
            self.__button_back.enable()
        
    def __increment(self, event):
        maximum = self.__range_list[1]
        if(self.__value < maximum):
            self.__value += 1
        self.__identify_enabled_buttons()
        if(self.__change_callback!= None):
            self.__change_callback(
                event)
        self.__update_label_number()
        
    def __add_decrement_listener(self):
        self.__button_back.add_listener(
            self.__decrement)
        
    def __decrement(self, event):
        minimum = self.__range_list[0]
        if(self.__value > minimum):
             self.__value -= 1
        self.__identify_enabled_buttons()
        if(self.__change_callback!= None):
            self.__change_callback(
                event)
        self.__update_label_number()