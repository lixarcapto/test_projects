



def is_tree_graph_dict(ANY : any):
    """
    Funcion que verifica si el dato
    enviado tiene un formato de 
    grafo de nodos en forma de arbol.
    Este grafo utiliza como ramas 
    diccionarios vacios.
    """
    if(not type(ANY) == dict): return False
    return search(ANY)
        
def search(DICT):
    for k in DICT:
        if(type(DICT[k]) == dict):
            if(DICT[k] == {}):
                return True
            else:
                if(search(DICT[k])):
                    continue
                else: 
                    return False
        else:
            return False
    return True