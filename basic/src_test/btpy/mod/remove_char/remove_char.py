

#Función que elimina un carácter de un 
# String por su índice
def remove_char(string, index):
    array = list(string)
    del(array[index])
    array = "".join(array)
    return array
