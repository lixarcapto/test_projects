


from .valid_index import*

def valid_index_test():
    print("valid_index_test")
    # ingreso de indice cualquiera
    valid_index(2, [0,0,0])
    print(True)
    # ingreso de 0
    valid_index(0, [0,0,0])
    print(True)
    # excepcion al limite
    try:
        valid_index(3, [0,0,0])
    except: print(True)
    else: print(False)
    # excepcion al negativo
    try:
        valid_index(-1, [0,0,0])
    except: print(True)
    else: print(False)
