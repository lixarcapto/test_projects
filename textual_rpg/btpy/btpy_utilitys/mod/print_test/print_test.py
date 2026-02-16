

from ....btpy_list.mod.true_percentage.true_percentage import*


def print_test(function)->None:
    """
    Función decoradora para decorar 
    funciones de test que recibe 
    un array por referencia para 
    almacenar resultados boolean 
    que calculará al final de la 
    función mostrando un porcentaje 
    de verdaderos en consola; 
    además de mostrar al inicio 
    el nombre de la función como 
    título en consola.
    """
    array = []
    def wrapper():
        print("<<-- " + function.__name__ + " function")
        function(array)
        r = true_percentage(array)
        r = round(r)
        print(f"-->> {r}% of the tests were successful")
    return wrapper