


from .get_symbol import*


def abs_sum(a_chief:int|float, 
        b:int|float)->int|float:
    """
    Funcion que suma número a otro 
    ignorando los negativos y 
    manteniendo el símbolo del primer 
    número.
    """
    symbol_a = get_symbol(a_chief)
    a = abs(a_chief)
    b = abs(b)
    r = a + b
    if(symbol_a == -1):
        r *= -1
    return r