



import json

def since_json_string(json_string):
    """
    Convierte una cadena JSON en 
    un objeto Python
    """

    try:
        # Deserializamos la cadena JSON a un objeto Python
        python_object = json.loads(json_string)
        return python_object
    except json.JSONDecodeError as e:
        print(f"Error al deserializar: {e}")
        return None