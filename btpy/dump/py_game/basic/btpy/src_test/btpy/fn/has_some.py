

"""
Función que itera sobre los elementos del
array enviado buscando si alguno de los 
elementos del array retornan true a la 
función enviada.
"""
def has_some(array, function):
        for e in array:
            if(function(e)):
                return True
        return False