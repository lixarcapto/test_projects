



import os

# Check if the file exists using 
# os.path.exists()
def check_path(PATH:str, 
        FILE_EXTENSION:str = "")->bool:
    if(not type(PATH) == str):
        raise Exception(
            f"route is not string ({PATH})"
    )
    if(FILE_EXTENSION != ""):
        if(not FILE_EXTENSION in PATH):
            raise Exception(
                f"route is not format {FILE_EXTENSION} ({PATH})"
            )
    if os.path.exists(PATH): return True
    return False
        