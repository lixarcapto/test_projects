

from model.Model import Model

def main():
    print("init..")
    model = Model()
    user_input = ""
    output = ""
    while(True):
        user_input = input(output)
        if(user_input == "f"): break
        output = model.write_narrative()
        model.advance_time()

main()