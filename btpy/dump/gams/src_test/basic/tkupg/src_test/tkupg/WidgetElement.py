


from .WidgetBase import WidgetBase
import tkinter as tk

class WidgetElement(WidgetBase):

    """
    Clase raíz de envoltura para los widgets 
    de tkinter. Esta busca simplificar la 
    raíz de los widgets para reducir la 
    cantidad de código escribir, y reducir 
    los parámetros indefinidos para 
    facilitar la comprensión.
    """

    """
    Parámetros de configuración para la 
    expansión del widget tk.
    """
    class AXE_EXPANSION:
        X = "x"
        Y = "y"
        NONE = "none"
        BOTH = "both"

    def __init__(self, widget):
        self.widget = widget.widget
        self.default_config()

    def default_config(self):
        self.widget.pack(expand=False, 
            fill = None)

    def set_size(self, range_arr):
        self.widget.pack_propagate(False)
        self.widget.config(
            height= range_arr[1],
            width= range_arr[0]
        )

    def set_location(self, point_ar):
        #self.widget.config(anchor='center')
        #self.widget.pack_propagate(False)
        self.widget.place(y = point_ar[0],
            x = point_ar[1])

    def pack_in_axe(self,
            axe_name:str)->None:
        self.widget.pack(expand=True, 
            fill = axe_name)
        
    def pack_without_expansion(self):
        self.widget.pack(expand=False, 
            fill = self.AXE_EXPANSION.NONE)

    def grid(self, row, column):
        self.widget.grid(
            row,
            column,
            columnspan = 3,
            sticky ='nsew',
            padx=10,
            pady=10
        )
