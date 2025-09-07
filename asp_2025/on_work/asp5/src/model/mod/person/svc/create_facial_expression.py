



def create_facial_expression(data):
    key = data.main_emotion
    if("tedium" == key):
        data.facial_expression = "serious_face"
    elif("happiness" == key):
        data.facial_expression = "smiling_face"
    elif("anger" == key):
        data.facial_expression = "annoyed_face"
    elif("fear" == key):
        data.facial_expression = "horror_face"
    elif("disgust" == key):
        data.facial_expression = "disgusted_face"
    elif("sadness" == key):
        data.facial_expression = "crying_face"
    return data
