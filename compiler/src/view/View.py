

import tkinter as tk
from model.Model import Model
from btpy_lib.btpy.src.btpy.Btpy import Btpy
from tkinter import filedialog
from tkinter import PhotoImage

class View:

    def __init__(self):
        # Crear la ventana principal
        self.model = Model()
        self.window = tk.Tk()
        self.window.title(
            "Nioi Compiler prototype")
        self.maximize()
        # Crear un label con un título
        self.title_label = tk.Label(
            self.window, 
            text="write a path to a folder with .js files to compile them into an html.")
        self.title_label.pack()
        self.name_label = tk.Label(
            self.window, 
            text="Name:")
        self.name_label.pack()
        self.input_name = tk.Entry(
           self.window)
        self.input_name.pack()
        self.button_search = tk.Button(
            self.window, 
            text="search file"
        )
        self.button_search.pack()
        # Crear un campo de texto
        self.input_text = tk.Entry(
           self.window)
        self.input_text.pack()
        self.button_pack_html = tk.Button(
            self.window, 
            text="pack html"
        )
        self.button_pack_html.pack()
        # Crear un label para mostrar mensajes
        self.message_label = tk.Label(
            self.window, text="")
        self.message_label.pack()
        self.n = 0
        self.path_selected = ""
        def fn():
            self.path_selected = filedialog\
                .askdirectory()
            self.input_text.insert(
                 0, self.path_selected)
        self.button_search.config(
            command=fn)
        def fn():
            path = self.input_text.get()
            name = self.input_name.get()
            self.model.request(
                {"command":"compile_html",
                 "path": path,
                 "name": name})
        self.button_pack_html.config(
            command=fn)
        # Crear un label para la imagen
        self.label_image = tk.Label(
            self.window)
        self.buffer_image = None
        self.label_image.pack()
        self.load_image(
            "../res/image/nordic_woman_cartoon_1.png")
        self.window.mainloop()

    def load_image(self, path):
        self.buffer_image = PhotoImage(
            file=path)
        self.label_image.config(
            image= self.buffer_image)

    def maximize(self):
        # Obtener el tamaño de la pantalla
        ancho_pantalla = self\
            .window.winfo_screenwidth()
        alto_pantalla = self\
            .window.winfo_screenheight()
        # Establecer el tamaño de la ventana igual al tamaño de la pantalla
        self.window.geometry(
            f"{ancho_pantalla}x{alto_pantalla}")
        