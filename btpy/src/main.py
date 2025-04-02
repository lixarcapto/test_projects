

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
    
    Btpy.init_html_gui(Model(), 
        "index.html")

    #---------------------------------
    print(r)

main() 