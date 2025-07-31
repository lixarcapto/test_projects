


class Model:

    def __init__(self):
        self.comik_name = "new"
        self.vignette_index:list = 0
        self.vignette_list:list = []
        self.actual_layout_text = 0
        self.layouts_text = 10
        self.buble_text_idx = 0

    def set_vignette_index(self, INDEX):
        self.vignette_index = INDEX

    def get_vignette_list_size(self):
        return len(self.vignette_list)

    def create_new_vignette(self)->dict:
        dict_ = {
            "IMAGE": "",
            "TEXT_BUBLE_LIST": []
        }
        self.vignette_list.append(dict_)

    def set_layouts_text(NUMBER:int):
        pass

    def create_buble_text(self,
            POINT_CURSOR:list[list],
            TEXT_LIST):
        dict_ = self.get_actual_vignette()
        text_buble_dict = {
            "TEXT_LAYOUT": TEXT_LIST,
            "POINT_LIST": POINT_CURSOR
        }
        dict_["TEXT_BUBLE_LIST"]\
            .append(text_buble_dict)
        self.set_actual_vignette(dict_)

    def modify_buble_text(self,
            POINT_CURSOR:list[list],
            TEXT_LIST):
        dict_ = self.get_actual_vignette()
        idx = self.buble_text_idx
        text_buble_dict = dict_\
            ["TEXT_BUBLE_LIST"][idx]
        text_buble_dict["TEXT_LAYOUT"]\
            = TEXT_LIST
        dict_\
            ["TEXT_BUBLE_LIST"][idx] \
            = text_buble_dict
        self.set_actual_vignette(dict_)

    def reset(self):
        self.comik_name = "new"
        self.vignette_list = []
        self.create_new_vignette()

    def set_image_name(self, NAME:str):
        dict_ = self.get_actual_vignette()
        dict_["IMAGE"] = NAME
        self.set_actual_vignette(dict_)

    def get_image_name(self):
        dict_ = self.get_actual_vignette()
        return dict_["IMAGE"]

    def get_buble_text_list(self)->list:
        dict_ = self.get_actual_vignette()
        layout_n = self.actual_layout_text
        text_list = dict_["TEXT_BUBLE_LIST"]
        return text_list

    def get_actual_vignette(self):
        return self.vignette_list\
            [self.vignette_index]
    
    def set_actual_vignette(self, DICT):
        self.vignette_list\
            [self.vignette_index] = DICT
        
    def get_comik_name(self):
        return self.comik_name