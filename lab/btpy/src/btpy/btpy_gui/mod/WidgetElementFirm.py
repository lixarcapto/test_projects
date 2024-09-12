

from .WidgetBaseFirm import WidgetBaseFirm

class WidgetElementFirm(WidgetBaseFirm):

    def set_text(self, string):
        pass

    def add_text(self, new_text):
        pass

    def get_text(self):
        pass

    def extract_text(self):
        pass

    def set_photo(self, photoimage):
        pass

    def set_image(self, route:str):
        pass

    def set_font(self, font_name, size, 
                 style = "roman"):
        pass

    def pack_in_axe(self,
            axe_name:str)->None:
        pass
        
    def pack_without_expansion(self):
        pass

    def grid(self, row, column):
        pass