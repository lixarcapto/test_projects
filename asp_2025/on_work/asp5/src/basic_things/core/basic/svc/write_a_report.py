


SIZE_CONSOLE_IN_CHARACTERS = 70

"""
    Funcion que crea un reporte ordenado en string
    para escribir en consola; segun el tamaño de los
    datos los escribira en una linea o varias.
"""
# return string
def write_a_report(report_name, data_string, file_name,
        function_name):
    text = ""
    jump_line = ""
    data_string_leng = len(data_string)
    if(data_string_leng >= SIZE_CONSOLE_IN_CHARACTERS):
        jump_line = "\n"
    text += "<!> Report "+ report_name + ": in "
    text += file_name + "." + function_name + " "
    text += "(" + jump_line
    text += data_string + jump_line + ")"
    text += "end " + report_name
    return text
