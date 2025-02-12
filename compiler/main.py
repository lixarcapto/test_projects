

from btpy_lib.btpy.src.btpy.Btpy import Btpy
from get_js_text_list import*
from create_html_file import*
from remove_import_from import*
import os


"""
Funcion que elimina las lineas de 
import from y export de cada texto
en el array enviado. Solo funciona si 
estan bien escritos.
"""
def process_array(array):
    for i in range(len(array)):
        while("import" in array[i]
        or "export" in array[i]):
            array[i] = remove_import_from(array[i])
    return array

def remove_comments_array(array):
    for i in range(len(array)):
        array[i] = remove_comments(array[i])
    return array

"""
Inicia una consola que pide la URL
de la carpeta javascript.
"""
def start_console():
    user_input = ""
    while(True):
        user_input = input("write path")
        if(user_input == ""):
            break
        compile_file(user_input)
        #Btpy.clean_console()

"""
Compila una carpeta de codigo full .js
en un solo archivo HTML.
TODO: Ordanizar y modularizar esta funcion.
"""
def compile_file(path):
    array = get_js_text_list(path)
    array = remove_comments_array(array)
    dict = create_js_file_data(array)
    print("dict", dict)
    three = create_three(
        dict["class_list"])
    order_list = get_order_list(
        three)
    has_class = False
    print("order_list", order_list)
    if(len(order_list) > 0):
        has_class = True
    text = ""
    if(has_class):
        str_js_class_list = write_js_str_as_list(
        dict["class_list"], order_list)
        print("three", three)
        str_js_class_list = process_array(
            str_js_class_list)
        for e in str_js_class_list:
            text += e
    array = process_array(
        dict["no_class_list"])
    for e in array:
        text += e
    crear_archivo_html(text)
 
if __name__ == "__main__":
    start_console()


