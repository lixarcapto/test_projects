
import tkinter as tk
from ..widget_composite.WidgetComposite import WidgetComposite
from ..frame.Frame import Frame
from tkinter import ttk
from ....btpy_gui.mod.text_field.TextField import TextField
from tkinter import filedialog
from tkinter import font

class InputFile(WidgetComposite):

    """
    FILE_TYPE:
        * folder
        * text
        * table
        * image
        * audio
        * any_file
    """

    def __init__(self, window, 
            file_type, title:str):
        super().__init__(window, True)
        self.button_load = None
        self.text_field = None
        self.key_type = ""
        self.title = title
        self.auto_fit_text:bool = False
        self.text_button = "search"
        self.__init_components()
        self.set_type_search(file_type)
        self.set_title(title)

    def set_type_search(self, FILE_TYPE:str):
        """
        FILE_TYPE:
        * folder
        * text
        * table
        * image
        * audio
        * any_file
        """
        self.key_type = FILE_TYPE
        self.button_load.config(
                text = self.text_button \
                + f" {self.key_type}"
            )
        if(FILE_TYPE == "folder"):
            self.search_folder()
        elif(FILE_TYPE == "image"):
            self.search_file_image()
        elif(FILE_TYPE == "text"):
            self.search_file_text()
        elif(FILE_TYPE == "any_file"):
            self.search_file()

    def __init_components(self):
        font_ = font.Font(
                family="Arial", 
                size=8, 
                weight="bold"
                )
        self.button_load = tk.Button(
            self.widget, 
            text = "search",
            font = font_,
            bg = "gray",
            fg = "white"
        )
        self.text_field = TextField(
            self.widget, ""
        )
        # dibujar ------------------------
        self.button_load.grid(
            row = 0, column= 0
        )
        self.text_field.grid(
            0, 1
        )

    def search_folder(self):
        def fn():
            path = filedialog.askdirectory(
                title=self.title
            )
            if(self.auto_fit_text):
                self.text_field\
                    .set_character_width(
                    len(path))
            self.text_field.set_value(
                path)
        self.button_load.config(
            command = fn)
        
    def search_file_image(self):
        filetypes_ = (
            ("Imágenes (SVG, PNG, JPG, JPEG, GIF)", "*.svg;*.png;*.jpg;*.jpeg;*.gif"),
            ("Todos los archivos", "*.*")
        )
        def fn():
            path = filedialog\
                .askopenfilename(
                title=self.title,
                filetypes = filetypes_
            )
            if(self.auto_fit_text):
                self.text_field\
                    .set_character_width(
                    len(path))
            self.text_field.set_value(
                path)
        self.button_load.config(
            command = fn)
        
    def search_file_text(self):
        filetypes_ = (
            ("Imágenes (DOCX, PDF, TXT)", "*.docx;*.pdf;*.txt"),
            ("Todos los archivos", "*.*")
        )
        def fn():
            path = filedialog\
                .askopenfilename(
                title=self.title,
                filetypes = filetypes_
            )
            if(self.auto_fit_text):
                self.text_field\
                    .set_character_width(
                    len(path))
            self.text_field.set_value(
                path)
        self.button_load.config(
            command = fn)
        
    def search_file(self):
        def fn():
            path = filedialog\
                .askopenfilename(
                title=self.title
            )
            if(self.auto_fit_text):
                self.text_field\
                    .set_character_width(
                    len(path))
            self.text_field.set_value(
                path)
        self.button_load.config(
            command = fn)

    def get_value(self)->str:
        return self.text_field.get_value()
    
    def set_value(self, TEXT:str):
        self.text_field.set_value(TEXT)