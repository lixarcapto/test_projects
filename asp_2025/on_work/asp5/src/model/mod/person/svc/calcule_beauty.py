


def calcule_beauty(data):
    if(data.caste == "noble"):
        data.BEAUTY_STAT_SUM.sum_stat("is_noble")
    if(data.age_code < 5):
        data.BEAUTY_STAT_SUM.sum_stat("age_less_middle")
    if(data.weight_code == 2):
        data.BEAUTY_STAT_SUM.sum_stat("weight_fit")
    if(not data.actual_height_code == 0):
        data.BEAUTY_STAT_SUM.sum_stat("not_dwarf")
    if(not data.is_bald):
        data.BEAUTY_STAT_SUM.sum_stat("not_is_bald")
    percent = data.BEAUTY_STAT_SUM.calcule()
    index = convert_to_index(percent, 4)
    return index

def convert_to_index(percent, limit):
    part = 100 / limit
    percent_for_index = 0
    for index in range(limit):
        percent_for_index = index * part
        if(percent <= percent_for_index):
            return index
