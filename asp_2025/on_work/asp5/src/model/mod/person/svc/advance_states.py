


def advance_states(data):
    if(data.pregnant_time > 0):
        data.pregnant_time -= 1
    elif(data.pregnant_time == 1):
        data.baby_can_walk = True
    return data
