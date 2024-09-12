

from write import*

def write_test():
    animales = {
    "perro": {
        "tipo": "mamífero",
        "sonido": "ladrido",
        "habitat": "domestico",
        "alimentacion": "carnívoro"
    },
    "gato": {
        "tipo": "mamífero",
        "sonido": "maullido",
        "habitat": "domestico",
        "alimentacion": "carnívoro"
    }
    }
    countries = [
    ["Brazil", "Argentina", "Colombia"],  # America
    ["Spain", "France", "Germany"],  # Europe
    ["Egypt", "Ethiopia", "South Africa"],  # Africa
    ["China", "Japan", "India"],        # Asia
    ["Australia", "New Zealand", "Papua New Guinea"]  # Oceania
    ]
    r = write(countries)
    print(r)
    r = write(animales)
    print(r)

write_test()