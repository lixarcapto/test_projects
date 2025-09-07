

from model.mod.date_asp.DateAsp import DateAsp

def main():
    date = DateAsp()
    for i in range(150):
        date.advance_one_day()
    print(date)

main()