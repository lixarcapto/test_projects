



import os

# Check if the file exists using 
# os.path.exists()
def valid_path(route:str, extension:str):
    if(not type(route) == str):
        raise Exception(
            f"route is not string ({route})"
        )
    if(not extension in route):
        raise Exception(
            f"route is not format {extension} ({route})"
        )
    if os.path.exists(route):
        return None
    else:
        raise Exception(
            f"route dosnt exist ({route})"
        )