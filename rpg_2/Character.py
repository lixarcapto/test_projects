


class Character:

    last_id = 0

    def __init__(self):
        self.id = 0
        self.appearance = "appaearance"
        self.vision_text = ""
        Character.last_id += 1
        self.id = Character.last_id