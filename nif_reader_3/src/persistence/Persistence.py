


from btpy.src.btpy.Btpy import Btpy
from .read_docx_with_titles import*

class Persistence:

    def __init__(self) -> None:
        pass

    def load_nif_docx(self, ROUTE:str):
        """
        Funcion que lee el archivo NIF docx
        seleccionado por el usuario.
        """
        # lee el archivo NIF
        dict_nif = read_docx_with_titles(
            ROUTE)
        # convierte las claves a mayuscula
        dict_nif = Btpy.map_in_keys(
            dict_nif,
            lambda e:e.upper()
        )
        return dict_nif
    
