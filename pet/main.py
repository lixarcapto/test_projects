

from Model import Model

def main():
    print("init...")
    model = Model()
    user_input = ""
    output = ""
    while(True):
        user_input = input(output)
        if(user_input == "f"): break
        if(user_input == "a"): 
            model.advance_one_day()
        output = model.write()

main()