


import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ..canvas.Canvas import Canvas

class IconFace(WidgetStandard):

    resource_path = "../res/image/icon_face/"
    image_extension = ".png"
    name_image_dict = {
        "EYES":{
            "EYES_ASIAN_NORMAL":
                "eyes_asian_normal",
            "EYES_ASIAN_NORMAL":
                "eyes_asian_close",
            "EYES_ASIAN_NORMAL":
                "eyes_asian_happy",
            "EYES_ASIAN_NORMAL":
                "eyes_asian_angry",
        },
        "FACE":{
            "FACE_PALE": "face_pale",
            "FACE_WHITE": "face_white",
            "FACE_ALMOND": "face_almond",
            "FACE_BROWN": "face_brown",
            "FACE_BLACK": "face_black"
        },
        "HAIR":{
            "HAIR_POT_BLACK": 
                "hair_pot_black"
        },
        "MOUTH":{
            "MOUTH_NORMAL": "mouth_normal"
        },
        "NOSE":{
            "NOSE_TYPE_A":"nose_type_a"
        }
    }

    def __init__(self, window):
        super().__init__(window)
        self.widget = Canvas(window, 
            "icon face")
        self.widget.set_size(150, 150)
        self.widget.pack()
        self.face_key = "FACE_WHITE"
        self.mouth_key = "MOUTH_NORMAL"
        self.hair_key = "HAIR_POT_BLACK"
        self.nose_key = "NOSE_TYPE_A"
        self.eyes_key = "EYES_ASIAN_NORMAL"

    def set_face_key(self, KEY:str):
        self.face_key = KEY
    
    def set_mouth_key(self, KEY:str):
        self.mouth_key = KEY
    
    def set_hair_key(self, KEY:str):
        self.hair_key = KEY
    
    def set_nose_key(self, KEY:str):
        self.nose_key = KEY
    
    def set_eyes_key(self, KEY:str):
        self.eyes_key = KEY

    def get_eyes_keys_list(self):
        return list(
            IconFace.name_image_dict\
                ["EYES"].keys()
        )
    
    def get_face_keys_list(self):
        return list(
            IconFace.name_image_dict\
                ["FACE"].keys()
        )
    
    def get_mouth_keys_list(self):
        return list(
            IconFace.name_image_dict\
                ["MOUTH"].keys()
        )
    
    def get_hair_keys_list(self):
        return list(
            IconFace.name_image_dict\
                ["HAIR"].keys()
        )
    
    def get_nose_keys_list(self):
        return list(
            IconFace.name_image_dict\
                ["NOSE"].keys()
        )

    def set_face_dict(self, DICT):
        """
        {
            "FACE": "FACE_WHITE",
            "MOUTH": "MOUTH_NORMAL",
            "HAIR": "HAIR_POT_BLACK",
            "NOSE": "NOSE_TYPE_A",
            "EYES": "EYES_ASIAN_NORMAL"
        }
        """
        self.face_key = DICT["FACE"]
        self.mouth_key = DICT["MOUTH"]
        self.hair_key = DICT["HAIR"]
        self.nose_key = DICT["NOSE"]
        self.eyes_key = DICT["EYES"]

    def set_path_resources(self, PATH):
        IconFace.resource_path = PATH

    def create_path(self, NAME_IMAGE):
        return IconFace.resource_path \
            + NAME_IMAGE\
            + IconFace.image_extension

    def get_path_list(self):
        face_path = IconFace.name_image_dict\
            ["FACE"][self.face_key]
        mouth_path = IconFace.name_image_dict\
            ["MOUTH"][self.mouth_key]
        hair_path = IconFace.name_image_dict\
            ["HAIR"][self.hair_key]
        nose_path = IconFace.name_image_dict\
            ["NOSE"][self.nose_key]
        eyes_key = IconFace.name_image_dict\
            ["EYES"][self.eyes_key]
        return [
            self.create_path(face_path),
            self.create_path(nose_path),
            self.create_path(mouth_path),
            self.create_path(eyes_key),
            self.create_path(hair_path)
        ]
        
    def paint(self):
        self.widget.repaint()
        path_list = self.get_path_list()
        self.widget.draw_image_layers(
            [0, 0],
            path_list
        )

        
    