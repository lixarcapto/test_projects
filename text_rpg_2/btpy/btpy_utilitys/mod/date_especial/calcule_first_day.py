



def calcule_first_day(YEAR:int):
    reference_list = [
        {"YEAR": 2000,
        "INDEX_DAY": 5,
        "CALENDAR": "gregorian"},
        {"YEAR": 1500,
        "INDEX_DAY": 2,
        "CALENDAR": "gregorian"},
        {"YEAR": 1700,
        "INDEX_DAY": 4,
        "CALENDAR": "gregorian"},
        {"YEAR": 1200,
        "INDEX_DAY": 5,
        "CALENDAR": "gregorian"},
        {"YEAR": 1000,
        "INDEX_DAY": 2,
        "CALENDAR": "gregorian"},
        {"YEAR": 1,
        "INDEX_DAY": 4,
        "CALENDAR": "julian"}
    ]
    minor_references = []
    for e in reference_list:
        if(e["YEAR"] <= YEAR):
            minor_references.append(e)
    year_indexed = []
    for e in minor_references:
        year_indexed.append(e["YEAR"])
    element = max(year_indexed)
    # encuentra el año seleccionado
    for e in reference_list:
        if(e["YEAR"] == element):
            reference = e
            break
    temp_year = reference["YEAR"]
    index_day = reference["INDEX_DAY"]
    while(temp_year < YEAR):
        temp_year += 1
        if(index_day == 6):
            index_day = 0
        else: 
            index_day += 1
    return {"index_day":index_day, 
            "calendar":reference["CALENDAR"]}