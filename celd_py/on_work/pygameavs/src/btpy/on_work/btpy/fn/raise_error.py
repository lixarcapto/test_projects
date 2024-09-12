

"""
Función que lanza una excepción de 
forma más ordenada mostrando el dato 
enviado y una solución al final.
"""
def raise_error(text:str, data, 
            correction:str)->None:
        margin = " " * 3
        raise Exception("\n\n" \
            + f"Error <!>: \n" \
            + f"{margin}Type: {text}\n" \
            + f"{margin}cause by: {data}\n"\
            + f"{margin}how to fix:" + correction\
            + "\n"
        )