


import tkinter as tk
from ..widget_composite.WidgetComposite import WidgetComposite
from ..frame.Frame import Frame
from ..standard_box.StandardBox import StandardBox
from ..button_icon.ButtonIcon import ButtonIcon

class ButtonBoxIcon(StandardBox):

    """
    Este componente sirve para crear
    una caja de botones de tipo icono 
    de forma facil y rapida.
    """

    def __init__(self, window,
                is_horizontal, 
                title:str):
        super().__init__(
            window, 
            ButtonIcon,
            is_horizontal,
            title
        )

    def set_content(self, TEXT_LIST,
            PATH_LIST):
        n = 0
        for widget in self.component_list:
            widget.set_title(
                TEXT_LIST[n]
            )
            widget.set_path_image(
                PATH_LIST[n]
            )
            n += 1