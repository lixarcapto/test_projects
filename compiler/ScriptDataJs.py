


class ScriptDataJs:
    
    def __init__(self): 
        self.class_name:str = ""
        self.string_js:str = ""
        self.extends_key:str = ""
        self.file_type:str = "script"

    def write(self)->str:
        return f"${self.class_name=} "\
        + f"${self.string_js=} "\
        + f"${self.extends_key=} "\
        + f"${self.file_type=} "