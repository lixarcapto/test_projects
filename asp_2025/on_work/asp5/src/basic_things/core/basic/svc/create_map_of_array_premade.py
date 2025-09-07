


"""
    Funcion para crear map_of_string_array prediseñados
    para pruebas de codigo y funciones.
"""
# map_of_string_array
def create_map_of_array_premade(topic = "animals"):
    if("animals" == topic):
        animals_map_of_array = {
            "canidos" : [\
                "coyote",
                "perro",
                "lobo"
            ],
            "cetaceos" : [\
                "ballena",
                "orca",
                "cachalote"
            ],
            "moluscos" : [\
                "caracol",
                "calamar",
                "ostras"
            ],
            "artropodos" : [\
                "arañas",
                "escarabajos",
                "hormigas"
            ],
            "primates" : [\
                "humano",
                "gorila",
                "chimpance"
            ],
            "felinos" : [\
                "gato",
                "tigre",
                "leon"
            ]
        }
        return animals_map_of_array
    elif("vehicles" == topic):
        vehicles_map_of_array = {
            "avion" : [\
                "caza",
                "aeroplano",
                "jet"
            ],
            "barco" : [\
                "carguero",
                "lancha",
                "fragata"
            ],
            "motorizado" : [\
                "camion",
                "automobil",
                "motocicleta"
            ],
            "traccion" : [\
                "carrosa",
                "caballo",
                "camello"
            ]
        }
        return vehicles_map_of_array
    elif("foods" == topic):
        foods_map_of_array = {
            "verdura" : [\
                "papa",
                "lechuga",
                "lentejas"
            ],
            "cereal" : [\
                "arroz",
                "maiz",
                "trigo"
            ],
            "carnes" : [\
                "pollo",
                "cerdo",
                "vaca"
            ],
            "dulce" : [\
                "mermelada",
                "caramelo",
                "algodon"
            ],
            "lacteos" : [\
                "leche",
                "yogurt",
                "quezo"
            ]
        }
        return foods_map_of_array
