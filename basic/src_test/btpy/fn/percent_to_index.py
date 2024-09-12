

def percent_to_index(percent, limit):
    part = 100 / limit
    percent_for_index = 0
    for index in range(limit):
        percent_for_index = index * part
        if(percent <= percent_for_index):
            return index
    return -1