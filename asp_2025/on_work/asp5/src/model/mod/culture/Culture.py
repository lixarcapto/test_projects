


class Culture:

    def __init__(self, key):
        self.name = ""
        self.family = ""
        self.origin_region_coordinate = []
        self.map_traits = {
            "ideologys": [],
            "descriptions": [],
            "eye_type": [],
            "hair_color": [],
            "skin_color": [],
            "maximum_height": [],
            "hair_type": [],
            "eye_color": [],
            "is_bald": [],
            "has_frekkles": []
        }

    def build(self, key):
        if(nokai == key):
            self.create_nokai()
            return None

    def create_nokai(self):
        self.name = ""
        self.family = ""
        self.map_traits["ideologys"] = [
            "",
            "",
            "",
            "",
            ""
        ]
        self.map_traits["descriptions"] = [
            "",
            "",
            "",
            "",
            ""
        ]
        self.map_traits["eye_type"] = [
            "asian",
            "distant"
        ]
        self.map_traits["hair_color"] = [
            "brown",
            "pink"
        ]
        self.map_traits["skin_color"] = [
            "",
            "",
            "",
            "",
            ""
        ]
        self.map_traits["maximum_height"] = [
            "",
            "",
            "",
            "",
            ""
        ]
        self.map_traits["hair_type"] = [
            "",
            "",
            "",
            "",
            ""
        ]
        self.map_traits["eye_color"] = [
            "brown",
            "red",
            "black"
        ]
        self.map_traits["is_bald"] = [
            True,
            True,
            True,
            False
        ]
        self.map_traits["has_frekkles"] = [
            False
        ]
