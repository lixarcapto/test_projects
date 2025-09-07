


from .is_boring import*

def define_main_emotion(data):
    # max para dicts
    emotion_map = data.emotion_states_map
    if(is_boring(data)):
        key = "tedium"
    else:
        key = max(emotion_map, key=emotion_map.get)
    data.main_emotion = key
    return data
