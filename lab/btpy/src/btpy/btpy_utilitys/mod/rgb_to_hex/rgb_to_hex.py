

def rgb_to_hex(rgb_list:list)->str:
    """
    Convierte un color RGB en su 
    representación hexadecimal.
    """
    txt = ""
    txt += f"#{rgb_list[0]:02x}"
    txt += f"{rgb_list[1]:02x}"
    txt += f"{rgb_list[2]:02x}"
    return txt