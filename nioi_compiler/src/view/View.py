

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
        self.maximize()
        # Crear un label con un título
        self.title_label = tk.Label(
            self.window)
        self.title_label.pack()
        self.name_label = tk.Label(
            self.window)
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
            self.window
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
            self.__compile_html()
        self.button_pack_html.config(
            command=fn)
        # Crear un label para la imagen
        self.label_image = tk.Label(
            self.window)
        self.buffer_image = None
        self.label_image.pack()
        self.__first_update()
        self.window.mainloop()


    def __first_update(self):
        response = self.model.request(
            {"function": "update"}
        )
        self.paint_render(response["return"])

    def paint_render(self, main_screen_render):
        render = main_screen_render
        self.window.title(render[
            "title_window"])
        self.title_label.config(
            text = render["label_title"])
        self.name_label.config(
            text = render["name_label"])
        self.set_input_name(
            render["default_name"])
        self.set_input_path(
            render["default_path"])
        self.button_search.config(
            text = render["button_search"])
        self.button_pack_html.config(
            text = render["button_pack"])
        self.message_label.config(
            text = render["message_label"])
        self.load_image(render["label_image"])
        

    def __compile_html(self):
        self.model.request({
            "function": "set_name",
            "args": {
                "name": self.input_name.get()
            }
        })
        self.model.request({
            "function": "set_folder_path",
            "args": {
                "folder_path": self
                    .input_text.get()
            }
        })
        self.model.request({
            "function":"compile_html"
        })
        self.model = Model()
        self.__update()

    def __update(self):
        response = self.model.request(
            {"function": "update"}
        )
        self.paint_render(response["return"])

    def set_input_name(self, text):
        self.input_name.delete(0, tk.END)
        self.input_name.insert(
                 0, text)
        
    def set_input_path(self, text):
        self.input_text.delete(0, tk.END)
        self.input_text.insert(
                 0, text)

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
        