

import os
from tkinter import filedialog
import tkinter

def seek_folder_route(ROUTE = "/")->str:
    """
    Abre un cuadro de diálogo para 
    seleccionar una carpeta.
    """

    root = tkinter.Tk()
    root.withdraw()

    # Abrimos un cuadro de diálogo para seleccionar una carpeta
    folder_path = filedialog.askdirectory(
        initialdir=ROUTE,
        title="Selecciona una carpeta"
    )

    return folder_path