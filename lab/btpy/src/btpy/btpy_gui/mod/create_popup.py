

import tkinter as tk

def create_popup(text_message:str, 
        opciones:list[str])\
        ->str:
    """
    Funcion que muestra un pop-up con 
    botones para seleccionar una opción. 
    Recibe una lista de opciones en 
    formato string y retorna el indice 
    de la opcion seleccionada.
    """
    top = tk.Toplevel()
    top.title("Selecciona una opción")
    top.wm_attributes('-topmost', True)
    
    indice_seleccionado = 0

    label = tk.Label(top, 
        text=text_message)
    label.pack(pady=2)

    def auxiliar(i):
        def seleccionar_opcion():
            top.destroy()
            nonlocal indice_seleccionado 
            indice_seleccionado =  i
        return seleccionar_opcion

    for i, opcion in enumerate(opciones):
        boton = tk.Button(top, 
                         text=opcion, 
                         command=auxiliar(i))
        boton.pack(pady=2)

    # Para evitar que el programa se 
    # bloquee antes de obtener el resultado
    top.wait_window()
    return indice_seleccionado