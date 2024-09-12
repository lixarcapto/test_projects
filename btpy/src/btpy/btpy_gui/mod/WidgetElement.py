


from .WidgetBase import WidgetBase
import tkinter
import tkinter.font
from PIL import ImageTk

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

    class STYLE:
        ROMAN = "roman"
        BOLD = "bold"

    class FONT:
        ARIAL = "Arial"
        TIMES_NEW_ROMAN = "Times New Roman"
        HELVETICA = "Helvetica"
        COURIER = "Courier"
        VERDANA = "Verdana"

    class SIDE:
        RIGHT = tkinter.RIGHT
        LEFT = tkinter.LEFT
        TOP = tkinter.TOP
        BOTTOM = tkinter.BOTTOM

    def __init__(self):
        super().__init__()
        self.widget = None
        #self.default_config()

    def unpack(self):
        self.widget.pack_forget()
        self.widget.grid_forget()
        self.widget.place_forget()

    def default_config(self):
        self.widget.pack(expand=False, 
            fill = None)

    def set_size(self, SIZE_X, SIZE_Y):
        self.widget.pack_propagate(False)
        self.widget.config(
            height= SIZE_X,
            width= SIZE_Y
        )

    def set_location(self, point_ar):
        #self.widget.config(anchor='center')
        #self.widget.pack_propagate(False)
        self.widget.place(y = point_ar[0],
            x = point_ar[1])

    
    def pack_in_axe(self, 
            axe_name:str = AXE_EXPANSION.BOTH,
            SIDE_KEY = tkinter.LEFT)\
            ->None:
        """
        función que organiza el componente 
        para que se expanda en el eje 
        determinado
        """
        self.widget.pack(
            side = SIDE_KEY,
            expand=True, 
            fill = axe_name
        )
        
    def pack_without_expansion(self, 
            SIDE_KEY = tkinter.LEFT):
        self.widget.pack(side = SIDE_KEY, 
            expand=False, 
            fill = self.AXE_EXPANSION.NONE
        )

    def grid(self, row, column):
        self.widget.grid(
            row,
            column,
            columnspan = 3,
            sticky ='nsew',
            padx=10,
            pady=10
        )

    def set_foreground(self, color):
        color = self.get_color(color)
        self.widget.config(fg=color)

    def set_font(self, FONT_NAME:str, 
        SIZE:int, STYLE:str = "roman"):
        self.widget.config(font=(
            FONT_NAME, 
            SIZE,
            STYLE
        ))
        
    def set_line_spacing(self, SIZE:int):
        self.widget.config(
            spacing1=SIZE)

    def set_text(self, text):
        pass

    def add_text(self, text):
        pass

    def get_text(self):
        pass

    def extract_text(self):
        pass

    def set_photo(self, photoimage):
        self.img = photoimage
        self.widget.config(image = self.img)

    def set_image(self, route:str):
        self.img = tkinter.PhotoImage(file=route)
        self.widget.config(image = self.img)