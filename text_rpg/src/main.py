
from btpy.Btpy import Btpy
from Model import Model

def main():
    input_text = ""
    to_write = "responde"
    model = Model()
    while(model.is_on):
        print(model.get_output())
        input_text = input()
        model.set_input(input_text)
main()
