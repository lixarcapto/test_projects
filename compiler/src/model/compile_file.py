

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
def compile_file(path, name):
    array = read_js_folder(path)
    array = remove_comments_array(array)
    # obtiene un diccionario de dos claves
    # con listas de clases y scripts
    dict = create_script_js_data_list(array)
    for e in dict["class_list"]:
        print("CLASS NAME", e.class_name)
        print("EXTENDS KEY", e.extends_key)
    # convierte el arbol en una ruta 
    # jerarquizada para escribir las clases
    three = create_class_three(
        dict["class_list"])
    print("three", three.write())
    order_list = three.create_keys_list()
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
            for e in dict["class_list"]:
                if(e.class_name 
                        == order_list[i]):
                    new_array.append(e)
        dict["class_list"] = new_array
        # ------------------------------
        class_SDJS_list \
            = remove_import_from_SDJS_list(
                dict["class_list"])
    # elimina las claves import export
    # de los scripts
    array = remove_import_from_SDJS_list(
        dict["no_class_list"])
    # CONVIERTE A TEXTO LAS LISTAS
    text = ""
    # convierte las clases a texto
    if(file_has_class):
        text += script_data_list_to_text(
            class_SDJS_list)
    # convierte los scripts a texto
    text += script_data_list_to_text(
            array)
    path_root = os.getcwd()
    path_to_create = f"../user/" + name \
        + ".html"
    # remplaza el SRC
    str_t = path_root.replace("\src", "")
    final_path = "file:///" + str_t \
        + "/user/" + name + ".html"
    # remplaza los slash por los del 
    # navegador
    final_path = final_path.replace(
        "\\", "/")
    print("final_path", final_path)
    crear_archivo_html(path_to_create, text)
    # abre el archivo HTML creado
    webbrowser.open(final_path)
    