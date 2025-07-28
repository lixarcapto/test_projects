


import tkinter as tk
from ..widget_composite.WidgetComposite \
    import WidgetComposite
from ..button.Button import Button
from ..frame.Frame import Frame
from ..standard_box.StandardBox import StandardBox

class ButtonBox(StandardBox):

    """
    Este componente es un grid de botones
    que comparten una unica callback 
    la cual recibe como argumento el
    texto que identifica a cada boton; 
    esto facilita añadir comportamientos
    iguales a varios botones.
    """

    def __init__(self, window, 
            is_horizontal, 
            title:str):
        super().__init__(window, 
            Button,
            is_horizontal, 
            title
        )

    def set_content(self, 
            TEXT_LIST:list[str])->None:
        """
        Funcion que asigna una lista
        de textos para los botones 
        previamente creados.
        """
        n = 0
        for button in self.component_list:
            button.set_title(
                TEXT_LIST[n])
            if(n > len(TEXT_LIST)):
                break
            n += 1
            