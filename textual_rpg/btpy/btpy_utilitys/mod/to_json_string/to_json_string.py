



import json

def to_json_string(objeto):
    """
    Convierte un objeto Python en una 
    cadena JSON
    """
    # Convertimos el objeto a JSON
    json_data = json.dumps(objeto)
    # Convertimos el JSON a una cadena (en realidad, ya es una cadena)
    json_string = str(json_data)
    return json_string