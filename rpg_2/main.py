

from Model import Model

def main():
    model = Model()
    char = model.create_character()
    model.add_character(char, [0, 0])
    user_input = ""
    output = ""
    while(True):
        user_input = input(output)
        if(user_input == "f"):
            break
        elif(user_input == "a"):
            model.update()
    print("init...")

main()