

from tkinter import colorchooser

def color_popup(CALLBACK)->tuple:
    """
    Retorna una tupla con dos valores,
    primero un RGB tuple y el otro un 
    HEX color string
    """
    color = colorchooser.askcolor()
    if color:
        CALLBACK(color)
        # Aquí puedes usar el color 
        # seleccionado