


from model.Model import Model

class Controller:

    def __init__(self):
        self.model = Model()

    def request(self, KEY_MESSAGE, 
            DICT_MESSAGE:dict)->dict:
        """
        Keys para mensajes.
        * render_map
        {
            "citizen_id_list": list,
            "citizen_id_select": int,
            "citizen_path_list": list
        }
        * render_society
        """