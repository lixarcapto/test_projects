

# TODO: No funciona
# para basic things
def split_file_path(file_path):

    split_path = Btpy.cut_from(file_path, ".")
    print(split_path)
    format_img = split_path[1]
    route = split_path[0]
    split_path = split_path[0].split("/")
    name = split_path[len(split_path) -1]

    # Create a dictionary with the extracted data
    file_info = {
        'formato': format_img,
        'nombre': name,
        'ruta': route,
    }
    return file_info