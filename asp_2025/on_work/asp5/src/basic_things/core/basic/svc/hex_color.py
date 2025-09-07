


"""
    Funcion que entrega un hex color por un nombre de color
"""
# return string
def hex_color(key_color):
    found_the_key = False
    key_color_map = None
    result_color_name = ""
    # busca si existe el color en el map
    if(key_color in color_hex_map_of_maps):
        found_the_key = True
        key_color_map = color_hex_map_of_maps[key_color]
        result_color_name =  key_color_map["hex"]
    # si no encuentra el color buscara uno parecido
    if(not found_the_key):
        for key in color_hex_map_of_maps:
            if((key in key_color) \
            or (key_color in key)):
                found_the_key = True
                key_color_map = color_hex_map_of_maps[key]
                result_color_name =  key_color_map["hex"]
                break
    # busca un color similar en similar_color_array
    if(not found_the_key):
        for key in color_hex_map_of_maps:
            key_color_map = color_hex_map_of_maps[key]
            for similar_color in key_color_map["similar_color_array"]:
                if(key_color in similar_color):
                    found_the_key = True
                    result_color_name =  key
                    break
    return result_color_name

color_hex_map_of_maps = {
    "red": {
        "hex":"#EA2C2C",
        "similar_color_array" : [\
                                ]
    },
    "yellow": {
        "hex":"#F3F04B",
        "similar_color_array" : [\
                                ]
    },
    "oranje": {
        "hex":"#FF9B35",
        "similar_color_array" : [\
                                ]
    },
    "green": {
        "hex":"#87F654",
        "similar_color_array" : [\
                                ]
    },
    "aquamarine": {
        "hex":"#60F2B9",
        "similar_color_array" : [\
                                ]
    },
    "skyblue": {
        "hex":"#5FF6ED",
        "similar_color_array" : [\
                                "sky_blue",
                                "heavenly",
                                "celestial"
                                ]
    },
    "blue": {
        "hex":"#457AF3",
        "similar_color_array" : [\
                                ]
    },
    "purple": {
        "hex":"#A144F3",
        "similar_color_array" : [\
                                "purpure",
                                "scarlet",
                                "purpura"
                                ]
    },
    "pink": {
        "hex":"#F54EF3",
        "similar_color_array" : [\
                                ]
    },
    "fuxia": {
        "hex":"#F54EA9",
        "similar_color_array" : [\
                                ]
    },
    "black": {
        "hex":"#000000",
        "similar_color_array" : [\
                                ]
    },
    "white": {
        "hex":"#FFFFFF",
        "similar_color_array" : [\
                                ]
    },
    "darkgreen": {
        "hex":"#1C5F2A",
        "similar_color_array" : [\
                                ]
    },
    "darkblue": {
        "hex":"#211976",
        "similar_color_array" : [\
                                ]
    },
    "ocher": {
        "hex":"#CF9B20",
        "similar_color_array" : [\
                                ]
    },
    "beige": {
        "hex":"#F5F5DC",
        "similar_color_array" : [\
                                ]
    },
    "cyan": {
        "hex":"#00FFFF",
        "similar_color_array" : [\
                                ]
    },
    "gray": {
        "hex":"#808080",
        "similar_color_array" : [\
                                "grey",
                                "grizzly",
                                "cinereous"
                                ]
    },
    "ivory": {
        "hex":"#FFFFF0",
        "similar_color_array" : [\
                                ]
    },
}
