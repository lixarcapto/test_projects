
import tkinter as tk
from ..widget_composite.WidgetComposite import WidgetComposite
from ..frame.Frame import Frame
from tkinter import ttk
from ....btpy_gui.mod.text_field.TextField import TextField
from tkinter import filedialog
from tkinter import font
from ..button.Button import Button

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
        self.onchange_callback = None
        self.set_type_search(file_type)
        self.set_title(title)

    def add_listener_onchange(self, 
            CALLBACK:any):
        self.onchange_callback\
            = CALLBACK

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
        self.button_load.set_title(
            self.text_button \
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
        self.button_load = Button(
            self.widget, "search"
        )
        self.text_field = TextField(
            self.widget, ""
        )
        # dibujar ------------------------
        self.button_load.draw_in_grid(0, 0,  "we")
        self.text_field.draw_in_grid(
            1, 0, "we"
        )

    def search_folder(self):
        def fn(e):
            path = filedialog.askdirectory(
                title=self.title
            )
            if(self.auto_fit_text):
                self.text_field\
                    .set_character_width(
                    len(path))
            self.text_field.set_value(
                path)
            self.__call_onchange_callback()
        self.button_load.add_listener(fn)
        
    def search_file_image(self):
        filetypes_ = (
            ("Imágenes (SVG, PNG, JPG, JPEG, GIF)", "*.svg;*.png;*.jpg;*.jpeg;*.gif"),
            ("Todos los archivos", "*.*")
        )
        def fn(e):
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
            self.__call_onchange_callback()
        self.button_load.add_listener(fn)
        
    def search_file_text(self):
        filetypes_ = (
            ("Imágenes (DOCX, PDF, TXT)", "*.docx;*.pdf;*.txt"),
            ("Todos los archivos", "*.*")
        )
        def fn(e):
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
            self.__call_onchange_callback()
        self.button_load.add_listener(fn)
        
    def search_file(self):
        def fn(e):
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
            self.__call_onchange_callback()
        self.button_load.add_listener(fn)

    def __call_onchange_callback(self):
        if(self.onchange_callback\
                == None):
            return None
        e = None
        self.onchange_callback(e)

    def get_value(self)->str:
        return self.text_field.get_value()
    
    def set_value(self, TEXT:str):
        self.text_field.set_value(TEXT)