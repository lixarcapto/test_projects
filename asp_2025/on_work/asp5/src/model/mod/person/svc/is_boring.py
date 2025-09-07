


"""
      Funcion que analiza si las emociones son inferiores
      a la mitad para declarar al personaje como aburrido.
"""
# return boolean
def is_boring(data):
    emotion_map = data.emotion_states_map
    middle_emotion_number = data.EMOTION_LIMIT
    for k in emotion_map:
        if (emotion_map[k] >= middle_emotion_number):
            return False
    return True
