


from btpy.src.btpy.Btpy import*
from emotion_sim.EmotionSim import EmotionSim
from chat_bot.KeysTranslator import KeysTranslator

class ChatBot:

    """
     Clase modelo con todas las 
     funcionalidades de un chatbot
    """

    IMAGE_DICT = {
        "angry":"./res/image/angry_expression.png",
        "bored":"./res/image/bored_expression.png",
        "disgust":"./res/image/disgust_expression.png",
        "fear":"./res/image/fear_expression.png",
        "happiness":"./res/image/happiness_expression.png",
        "sadness":"./res/image/sadness_expression.png",
        "pain":"./res/image/sadness_expression.png",
        "surprise":"./res/image/surprise_expression.png"
    }

    def __init__(self) -> None:
        self.keys_translator = KeysTranslator()
        self.actual_image = self.IMAGE_DICT["bored"]
        self.emotion_sim = EmotionSim()

    def update(self):
        self.emotion_sim.advance_time()
        main_emotion = self.emotion_sim\
            .get_main_emotion()
        self.actual_image = self.IMAGE_DICT\
            [main_emotion]

    def request(self):
        return {
            "image":self.actual_image
        }
    
    def receibe(self, message):
        self.read(message["text"])

    def write(self):
        return self.emotion_sim.write()

    def read(self, text):
        keys_arr = self.keys_translator\
            .translate_phrase(text)
        self.emotion_sim\
            .analize_concept_list(keys_arr)