


def find_nearest_mayor_key(
        diccionario, valor_referencia):
    """
    Busca la clave numérica más pequeña dentro del diccionario 
    que sea estrictamente mayor al valor_referencia.
    """
    # Filtramos solo las claves que son números y que son mayores al valor dado
    claves_candidatas = [k for k in diccionario.keys() if isinstance(k, (int, float)) and k > valor_referencia]
    
    # Si hay candidatas, devolvemos la menor de ellas
    if claves_candidatas:
        return min(claves_candidatas)
    
    # Si no se encuentra ninguna, retornamos None
    return None