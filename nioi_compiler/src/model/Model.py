
from btpy_lib.btpy.src.btpy.Btpy import Btpy
from .compile_file import compile_file

class Model:

    """
    Clase que sirve como el modelo principal
    de la aplicacion.
    """

    def __init__(self):
        # este es un reflejo en dict de 
        # los datos de la pantalla/vista
        self.main_screen_render = {}
        self.counter_compilations = 0
        #
        self.__init_main_screen()
        

    def __init_main_screen(self):
        self.main_screen_render = {
            "title_window": "Nioi Compiler prototype",
            "label_title": "write a path to a folder with .js files to compile them into an html.",
            "name_label": "Name:",
            "default_name": "compiler",
            "default_path": "",
            #  ruta de la carpeta javascript
            "button_search": "search",
            "button_pack": "pack html",
            "message_label": "",
            "path_root": "", 
            # ruta de guardado
            "url_file": "",
            "local_path": "",
            # ruta completa de guardado
            "label_image": "../res/image/nordic_woman_cartoon_1.png"
        }
        self.__create_path_root()
        self.generate_default_name()

    def generate_default_name(self):
        n = self.counter_compilations
        name = self.main_screen_render\
            ["default_name"]
        self.main_screen_render\
            ["default_name"] \
                = name + "_" + str(n)
        self.counter_compilations += 1

    def generate_unique_path(self):
        self.__create_full_local_path()
        while(self.local_path_exist()):
            self.main_screen_render[
                "message_label"]\
                = "<!> Error: the file "\
                + "already exists"
            self.generate_default_name()
            self.__create_full_local_path()

    """
    Este es el metodo de comunicacion 
    unico para el modelo; recibe un dict
    con dos claves; function y args; function
    es un string con la funcion a llamar
    y data es un dict con los argumentos
    de la funcion. Los mensajes de respuesta
    son dict que responden con un dict
    que tenga un atributo response que puede 
    ser fail o success; y return que contiene
    el retorno de la funcion en un dict
    """
    def request(self, message):
        response = {"function": "",
                    "args": {}}
        print("MESSAGE RECIEVED:", message)
        if(message["function"] 
                == "compile_html"):
            self.__compile_html()
        elif(message["function"] 
                == "set_name"):
            self.__set_name(
                message["args"]["name"]
            )
        elif(message["function"] 
                == "set_folder_path"):
            self.__set_folder_path(
                message["args"][
                    "folder_path"]
            )
        elif(message["function"] == "update"):
            response = {"result": "success",
                "return": self.main_screen_render}
        return response

    
    def __create_full_local_path(self):
        path_root = self.main_screen_render[
            "path_root"]
        name = self.main_screen_render[
            "default_name"]
        path = path_root + "\\" + name + ".html"
        self.main_screen_render[
            "local_path"] = path
    
    def __create_path_root(self):
        import os
        path_root = os.getcwd()
        path_root = path_root.replace(
            "\src", "")
        path_root = path_root+ "\\user"
        self.main_screen_render["path_root"]\
            = path_root

    def __create_url_file(self):
        path_root = self.main_screen_render[
            "path_root"]
        name = self.main_screen_render[
            "default_name"]
        url_file = "file:///" + path_root \
             + "/" + name + ".html"
        # remplaza los slash por los del 
        # navegador
        url_file = url_file.replace(
        "\\", "/")
        self.main_screen_render[
            "url_file"] = url_file
    
    def local_path_exist(self):
        import os
        path = self.main_screen_render[
            "local_path"]
        if(os.path.exists(path)):
            return True
        return False
    
    def __set_name(self, name):
        self.main_screen_render[
            "default_name"] = name
        
    def __get_name(self):
        return self.main_screen_render[
            "default_name"]
        
    def __set_folder_path(self, path):
        self.main_screen_render[
            "default_path"] = path
        
    def __get_folder_path(self):
        return self.main_screen_render[
            "default_path"]
        
    def __set_folder_result(self, path):
        self.main_screen_render[
            "default_path"] = path
        
    def __get_folder_result(self):
        return self.main_screen_render[
            "default_path"]
    
    def __get_path_root(self):
        return self.main_screen_render[
            "path_root"]

    def __compile_html(self):
        name = self.main_screen_render[
            "default_name"]
        folder_path = self.__get_folder_path()
        self.__create_full_local_path()
        self.__create_url_file()
        url_file = self.main_screen_render[
            "url_file"]
        path_root = self.main_screen_render[
            "path_root"]
        path_result = self.main_screen_render[
            "local_path"]
        print(self.main_screen_render)
        compile_file(
            path_result, 
            folder_path, 
            url_file, 
            name
        )

    

