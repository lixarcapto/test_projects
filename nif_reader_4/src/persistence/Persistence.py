


from .read_docx_with_titles import*
from btpy.Btpy import Btpy

class Persistence:

    NEXT_KEY = "Next;"
    END_KEY = "."
    SEPARATOR = ","

    def __init__(self):
        nif_dict = self.load_nif_docx(
            "./res/docx/nif_test.docx")
        print("persistence")
        print(nif_dict)

    def load_nif_docx(self, PATH_DOCX:str)\
            ->list[dict]:
        """
        Funcion que lee el archivo NIF docx
        seleccionado por el usuario. 
        Entrega un formato llamado NIF list
        que contiene SCENE dict.
        [
            {
                "KEY": "",
                "SCENE_KEYS": [""],
                "TEXT": ""
            }
        ]
        """
        # lee el archivo NIF
        dict_nif_raw = read_docx_with_titles(
            PATH_DOCX)
        # convierte las claves a mayuscula
        dict_nif_raw = Btpy.map_in_keys(
            dict_nif_raw,
            lambda e:e.upper()
        )
        nif_list = []
        scene_dict = {}
        for k in dict_nif_raw:
            scene_dict = self\
                .create_scene_dict(
                    k, dict_nif_raw[k]
                )
            nif_list.append(scene_dict)
        return nif_list
    
    def create_scene_dict(self, KEY, TEXT):
        """
        Crea un formato intermedio
        para el tipo de archivo NIF 
        llamado scene del que se compone
        el NIF dict.
        """
        scene_key_list = Btpy\
            .get_description(
                TEXT, 
                self.SEPARATOR, 
                [
                    self.NEXT_KEY, 
                    self.END_KEY
                ]
            )
        scene_key_list = Btpy.mapp(
            scene_key_list, 
            lambda e:e.upper()
        )
        text_value = Btpy.cut_until(
            TEXT, self.NEXT_KEY)
        return {
            "KEY": KEY,
            "SCENE_KEYS": scene_key_list,
            "TEXT": text_value
        }