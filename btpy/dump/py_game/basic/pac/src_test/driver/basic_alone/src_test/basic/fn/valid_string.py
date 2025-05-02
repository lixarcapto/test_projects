

"""
    function to validate the sent string; 
    this validates if the string is a 
    string, is not empty and is greater 
    than the minimum (optional)
"""
def valid_string(data: str, min_size = -1, 
        is_strict:bool = False):
    text = ""
    if(not type(data) == str):
        text = f"Error: data is not "\
        + f"string ({data})"
        if(is_strict):
            raise Exception(text)
        else:
            print(text)
            return None
    if(data == ""):
        text = f"Error: data is void string"
        if(is_strict):
            raise Exception(text)
        else:
            print(text)
            return None
    if(min_size != -1):
        if(len(data) < min_size):
            text = f"Error: data is less "\
            + f"minimum {len(data)}"
            if(is_strict):
                raise Exception(text)
            else:
                print(text)
                return None
