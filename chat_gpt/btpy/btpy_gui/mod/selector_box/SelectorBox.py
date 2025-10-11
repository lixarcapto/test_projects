

import tkinter as tk
from ..frame.Frame import Frame
from ..switch_color.SwitchColor import SwitchColor
from ..widget_composite.WidgetComposite import WidgetComposite
from ..standard_box.StandardBox import StandardBox

class SelectorBox(StandardBox):

    def __init__(self, window, 
                 is_horizontal,
                 title:str = ""):
        super().__init__(
            window,
            SwitchColor,
            is_horizontal,
            title
        )

    def set_content(self, TEXT_LIST):
        n = 0
        for button in self.component_list:
            button.set_title(TEXT_LIST[n])
            n += 1

    def get_value(self)->list[int]:
        index_list = []
        n = 0
        for button in self.component_list:
            if(button.get_value()):
                index_list.append(n)
            n += 1
        return index_list
    
    def set_value(self, index_list):
        n = 0
        for button in self.component_list:
            if(not (n in index_list)):
                button.set_value(False)
            else:
                button.set_value(True)
            n += 1
        return index_list
    
