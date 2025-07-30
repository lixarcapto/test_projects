



def string_number_list_to_list(STRING:str)\
        ->list[int]:
    list_ = STRING.split(",")
    for i in range(len(list_)):
        if("." in list_[i]):
            list_[i] = float(
                list_[i].strip())
        else:
            list_[i] = int(
                list_[i].strip())
    return list_