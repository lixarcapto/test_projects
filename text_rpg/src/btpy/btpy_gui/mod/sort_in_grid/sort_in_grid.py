

import tkinter as tk

def sort_in_grid(tk_widget_list:list,
        COLUMNS:int)->None:
    """
    Funcion que inserta en la ventana
    los widgets enviados con grid 
    definiendo la cantidad de columnas
    del grid.
    """
    x:int = 0
    y:int = 0
    widget_tk = None
    for i in range(len(tk_widget_list)):
        widget_tk = tk_widget_list[i]
        if(hasattr(widget_tk, "widget")): 
            widget_tk.margin.grid(
            row=y, column=x,
            sticky=tk.NSEW
        )
        else:
            widget_tk.grid(
                row=y, column=x,
                sticky=tk.NSEW
            )
        x += 1
        if(x == COLUMNS):
            y += 1
            x = 0