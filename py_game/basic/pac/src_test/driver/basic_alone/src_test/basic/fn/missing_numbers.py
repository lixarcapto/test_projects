


"""
    Funcion que calcula todos los numeros que faltan
    en una lista hasta el numero mas alto, y retorna
    una lista de rangos array con esos numeros faltantes.
    ALG:
    * cuenta cada numero desde el 0 hasta el maximo
    almacenando los que no se encuentren dentro del array.
"""
# return int_array
def missing_numbers(number_list):
    max_number = max(number_list) +1
    missing_numbers_matrix = []
    range_numbers_array = [0, 0]
    missing_number = 0 # numberos faltantes en rango
    # cuenta hasta el numero maximo del array
    for n in range(max_number):
        range_numbers_array = [0, 0]
        # analiza si el numero esta en la lista enviada
        if(n in number_list):
            # guarda el anterior numero
            range_numbers_array[0] = missing_number
            # guarda en el rango el numero inicial
            range_numbers_array[1] = n -1
            missing_number = n +1
            # añade un range_numbers_array a la matriz
            missing_numbers_matrix \
                .append(range_numbers_array)
    return missing_numbers_matrix