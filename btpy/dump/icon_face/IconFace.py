


import tkinter as tk
from ..widget_standard.WidgetStandard import WidgetStandard
from ..canvas.Canvas import Canvas
from .key_const import*

class IconFace(WidgetStandard):

    resource_path = "../res/image/icon_face/"
    image_extension = ".png"
    name_image_dict = {
            "EYES_ASIAN_NORMAL":
                "eyes_asian_normal",
            "FACE_PALE": "face_pale",
            "FACE_WHITE": "face_white",
            "FACE_ALMOND": "face_almond",
            "FACE_BROWN": "face_brown",
            "FACE_BLACK": "face_black",
            "HAIR_POT_BLACK": "hair_pot_black",
            "MOUTH_NORMAL": "mouth_normal",
            "NOSE_TYPE_A":"nose_type_a"
    }

    def __init__(self, window):
        super().__init__(window)
        self.widget = Canvas(window, 
            "icon face")
        self.widget.set_size(150, 150)
        self.widget.pack()

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
        return EYES_KEYS_TUPLE
    
    def get_face_keys_list(self):
        return SKIN_KEYS_TUPLE
    
    def get_mouth_keys_list(self):
        return MOUTH_TUPLE
    
    def get_hair_keys_list(self):
        return HAIR_TUPLE
    
    def get_nose_keys_list(self):
        return NOSE_TUPLE

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
            [self.face_key]
        mouth_path = IconFace.name_image_dict\
            [self.mouth_key]
        hair_path = IconFace.name_image_dict\
            [self.hair_key]
        nose_path = IconFace.name_image_dict\
            [self.nose_key]
        eyes_key = IconFace.name_image_dict\
            [self.eyes_key]
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

        
    