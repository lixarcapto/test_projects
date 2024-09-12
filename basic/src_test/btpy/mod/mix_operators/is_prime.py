


def is_prime(num:int)->bool:
    """
    Comprueba si un número es primo 
    retornando un booleano.
    """
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True