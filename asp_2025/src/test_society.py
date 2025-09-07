

from model.mod.society.Society import Society

def main():
    society = Society()
    society.populate_society(6, "nordic")
    for i in range(50):
        society.advance_one_day()
    print(society.write())

main()