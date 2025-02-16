

from btpy_lib.btpy.src.btpy.Btpy import Btpy
from .get_js_text_list import*
from .create_html_file import*
from .create_script_js_data_list import*
from .read_js_folder import*
from .create_class_three import*
from .scriptdata_list_to_list import*
from .remove_import_from_SDJS_list import*
from .remove_comments_array import*
from .script_data_list_to_text import*
import webbrowser
import os

"""
Compila una carpeta de codigo full .js
en un solo archivo HTML.
TODO: Ordanizar y modularizar esta funcion.
"""
def compile_file(
        path_return,
        path_folder_js, 
        url_file, 
        name):
    array = read_js_folder(path_folder_js)
    array = remove_comments_array(array)
    # obtiene un diccionario de dos claves
    # con listas de clases y scripts
    dict_ = create_script_js_data_list(array)
    # convierte el arbol en una ruta 
    # jerarquizada para escribir las clases
    three = create_class_three(
        dict_["class_list"])
    print("three", three.write())
    order_list = three.create_keys_list()
    print("order_list", order_list)
    file_has_class:bool = False
    if(len(order_list) > 0):
        file_has_class = True
    # elimina las claves import export
    # de las clases
    class_SDJS_list = []
    if(file_has_class):
        # ordena las listas --------------
        new_array = []
        for i in range(len(order_list)):
            for e in dict_["class_list"]:
                if(e.class_name 
                        == order_list[i]):
                    new_array.append(e)
        dict_["class_list"] = new_array
        # ------------------------------
        class_SDJS_list \
            = remove_import_from_SDJS_list(
                dict_["class_list"])
    # elimina las claves import export
    # de los scripts
    array = remove_import_from_SDJS_list(
        dict_["no_class_list"])
    # CONVIERTE A TEXTO LAS LISTAS
    text = ""
    # convierte las clases a texto
    if(file_has_class):
        text += script_data_list_to_text(
            class_SDJS_list)
        print("TEXT CLASS: ", text)
    # convierte los scripts a texto
    text += script_data_list_to_text(
            array)
    print("local_path", path_folder_js)
    print("url_file", url_file)
    crear_archivo_html(path_return, text)
    # abre el archivo HTML creado
    webbrowser.open(url_file)
    