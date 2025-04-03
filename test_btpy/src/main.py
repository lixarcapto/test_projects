

from btpy.Btpy import Btpy

class Model:

    def request(self, REQUEST_DICT):
        return {"message": "funciona"}

def main():
    print("init...")
    Btpy.init_html_gui(Model(), 
        "index.html")

main()