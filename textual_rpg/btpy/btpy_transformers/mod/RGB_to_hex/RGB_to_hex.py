

def RGB_to_hex(RGB_OR_RGBA:list[int])\
        ->str:
    """
    Converts an RGB color to its
    hexadecimal representation.
    """
    return "" \
    + f"#{RGB_OR_RGBA[0]:02x}"\
    + f"{RGB_OR_RGBA[1]:02x}"\
    + f"{RGB_OR_RGBA[2]:02x}"