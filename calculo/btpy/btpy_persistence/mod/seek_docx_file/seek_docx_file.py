



import tkinter as tk
from tkinter import filedialog

def seek_docx_file(ROUTE = "/")->str:
    """
    Abre un cuadro de diálogo para 
    seleccionar un archivo .docx y 
    devuelve la ruta.
    """

    root = tk.Tk()
    root.withdraw()  # Ocultamos la ventana principal

    # Abrimos un cuadro de diálogo para seleccionar archivos .docx
    file_path = filedialog.askopenfilename(
        initialdir=ROUTE,
        title="select file DOCX",
        filetypes=(
            ("Documentos Word", "*.docx"), 
            ("Todos los archivos", "*.*")
        )
    )

    return file_path