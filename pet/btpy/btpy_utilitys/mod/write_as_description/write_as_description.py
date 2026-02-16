


def write_as_description(DATA, 
        CONJUNCTION)->str:
    """
    function that writes a list 
    as if it were a literary 
    description separated by commas 
    and the final conjunction sent.
    """
    txt = ""
    for i in range(len(DATA)):
        txt += DATA[i]
        if(i < len(DATA) -2):
            txt += ", "
        elif(i == len(DATA) -2):
            txt += f" {CONJUNCTION} "
    txt += "."
    return txt
