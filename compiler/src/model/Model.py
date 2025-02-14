

from .compile_file import compile_file

class Model:

    """
    Clase que sirve como el modelo principal
    de la aplicacion.
    """

    def request(self, message):
        if(message["command"] 
                == "compile_html"):
            self.__compile_html(
                message["path"],
                message["name"]
            )
            
    def __compile_html(self, path, name):
        compile_file(path, name)

