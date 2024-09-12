

def calcule_first_day(YEAR:int):
    reference = {
        "YEAR": 2000,
        "INDEX_DAY": 5
    }
    temp_year = reference["YEAR"]
    index_day = reference["INDEX_DAY"]
    while(temp_year < YEAR):
        temp_year += 1
        if(index_day == 6):
            index_day = 0
        else: 
            index_day += 1
        print(index_day)
    return index_day