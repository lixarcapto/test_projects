
import sys
import os

# Obtiene la ruta absoluta del directorio del script actual.
directorio_actual = os.path.dirname(os.path.abspath(__file__))
# Sube dos niveles en la jerarquía de directorios.
directorio_padre = os.path.dirname(directorio_actual)
directorio_abuelo = os.path.dirname(directorio_padre)
# Añade el directorio abuelo al sys.path.
sys.path.append(directorio_abuelo)

from btpy.Btpy import Btpy

def main(): 
    graph = Btpy.Graph()
    graph.add_node("manzana", "apple")
    graph.add_node("platano", "banana")
    graph.add_neighbors_list(
        "manzana", ["platano"])
    print(graph.get_neighbors_keys(
        "manzana"))

main()