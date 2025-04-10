

from btpy.Btpy import Btpy

class Model:

    def request(self, dict):
        response = {}
        response["message"] = "esta es la respuesta"
        return response

def main():
    print("init...")
    r = None
    # -------------------------------------
    
    import sys

    variable_nula = None
    tamaño_en_bytes = sys.getsizeof(
        variable_nula)

    print(f"El tamaño en memoria de una variable con None es: {tamaño_en_bytes} bytes")

    """
    Btpy.init_html_gui(Model(), 
        "index.html")
    """

    #---------------------------------
    print(r)

main() 