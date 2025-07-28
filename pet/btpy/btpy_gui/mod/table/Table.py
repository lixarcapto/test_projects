


import tkinter as tk
from ..widget_composite.WidgetComposite \
    import WidgetComposite
from ..switch_icon.SwitchIcon import SwitchIcon
from ..frame.Frame import Frame
from ..sort_in_grid.sort_in_grid import sort_in_grid

class Table(WidgetComposite):

    def __init__(self, widget, 
                 is_horizontal, 
                 title = ""):
        super().__init__(
            widget,
            is_horizontal
        )
        self.columns = 0
        self.table_matrix = []
        self.set_title(title)

    def set_row_dict(self, row_dict):
        size = 0
        for k in row_dict:
            size = len(row_dict[k])
            break
        self.set_components(size + 1)
        list_ = []
        for k in row_dict:
            list_ = [k] + row_dict[k]
            self.create_row(list_)

    def format(self):
        for widget_list in self.table_matrix:
            for widget in widget_list:
                widget.pack_forget()

    def set_components(self, COLUMNS):
        self.format()
        self.columns = COLUMNS

    def create_row(self, text_list):
        label = None
        label_list = []
        for i in range(self.columns):
            if(i >= len(text_list)):
                continue
            label = self.create_label_cell(
                text_list[i]
            )
            label_list.append(label)
        self.table_matrix.append(
            label_list)
        
    def create_label_cell(self, TEXT):
        label = tk.Label(
            self.widget,
            text = f"  {TEXT}  ",
            relief = "solid",
            border= 1,
            bg = "white"
        )
        return label
        
    def draw_components(self):
        x = 0
        y = 0
        for widget_list in self.table_matrix:
            for widget in widget_list:
                widget.grid(
                    row = y, 
                    column = x,
                    sticky = "ew"
                )
                x += 1
            x = 0
            y += 1
