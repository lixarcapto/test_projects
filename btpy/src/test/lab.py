

import sys
import os

# Obtiene el directorio del script actual
current_dir = os.path.dirname(os.path.abspath(__file__))
# Obtiene el directorio padre
parent_dir = os.path.dirname(current_dir)
# Agrega el directorio padre a sys.path
sys.path.append(parent_dir)

from btpy.Btpy import Btpy

def main():
    g = Btpy.Graph()
    g.load_graph_dict({
        "Castilla y la mancha":
        [
            "Madrid", 
            "Castilla y Leon"
        ],
        "Madrid":
        [
            "Castilla y la mancha",
            "Castilla y Leon"
        ],
        "Castilla y Leon":
        [
            "Castilla y la mancha",
            "Madrid",
            "La Rioja"
        ],
        "La Rioja":
        [
            "Castilla y la mancha"
        ],
        "Navarra":
        [
            "La Rioja"
        ]
    },
    {
        "Castilla y la mancha": None,
        "Madrid": None,
        "Castilla y Leon": None,
        "La Rioja":None,
        "Navarra":None
    })
    print(g.get_neighbors_keys(
        "Castilla y la mancha"))
    print("path", g.get_deep_search_path(
        "Castilla y la mancha",
        "Navarra"
    ))
    print(g)

main()