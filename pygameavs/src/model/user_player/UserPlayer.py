


class UserPlayer:

    """
     clase que sirve para almacenar 
     los datos del usuario sobre 
     sucesión y objetos bajo su 
     propiedad.
    """

    def __init__(self) -> None:
        self.name = ""
        self.password = ""
        self.last_connect_date = None
        self.ip = ""
        self.cam_id = ""
        self.main_id = ""
        self.property_go_arr = []