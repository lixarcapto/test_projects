

from btpy.Btpy import Btpy
from Capture import Capture
from read_json_folder_as_dict import*

class CaptureStore:

    def __init__(self):
        self.capture_nested_dict:dict = {}
        self.init_capture_dict()

    def get(self, KEY:str)->Capture:
        return self.capture_nested_dict\
            [KEY.upper()]

    def init_capture_dict(self):
        folder_path = "./res/capture_json/"
        nested_dict = read_json_folder_as_dict(
            folder_path
        )
        dict_ = {}
        capture = None
        for k in nested_dict:
            capture = Capture()
            capture.load_capture_dict(
                nested_dict[k]
            )
            self.capture_nested_dict[k]\
                = capture
            
        