

def find_file_name(PATH:str)->str:
    """
    Function that gets the name of 
    a file or folder by removing 
    extra paths and extensions.
    """
    end_path = ""
    if("/" in PATH):
        list_ = PATH.split("/")
        end_path = list_[len(list_) -1]
    else:
        end_path = PATH
    name = ""
    if("." in end_path):
        name = end_path.split(".")[0]
    else:
        name = end_path
    return name