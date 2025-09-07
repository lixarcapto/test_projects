


from ..index import write_error

"""
    Funcion que extrae una letra del string en
    una posicion especifica usando slicing.
"""
# char
def charat(string, index):
    if(not index < len(string)):
        text = write_error(\
                error = "string out of range",
                file_name = "charat",
                function_name = "charat",
                data_error = "index " + str(index) \
                + " of leng " + str(len(string))
                )
        print(text)
        return ""
    return string[index:index + 1]
