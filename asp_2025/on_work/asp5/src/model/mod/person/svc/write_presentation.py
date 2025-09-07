


# return string
def write_presentation(data):
    pj = data
    text = ""
    text += pj.name + " " + pj.second_name +  " "
    text += pj.lastname + " " + pj.second_lastname + " "
    text += "the " + pj.nickname + " "
    text += "is a " + pj.culture + " "
    text += "from " + pj.country_origin
    return text
