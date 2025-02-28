

import sys
import os

# Obtiene el directorio del script actual
current_dir = os.path.dirname(os.path.abspath(__file__))
# Obtiene el directorio padre
parent_dir = os.path.dirname(current_dir)
# Agrega el directorio padre a sys.path
sys.path.append(parent_dir)

from btpy.btpy_utilitys.mod.emotion_translator.EmotionTranslator import EmotionTranslator
from get_root import*
from btpy.btpy_utilitys.mod.emotion_sim.EmotionSim import EmotionSim

from btpy.Btpy import Btpy


transl = EmotionTranslator()
transl.load_data_base_symbol(
        "../btpy/res/symbol_emotion.xlsx")
emotion = EmotionSim()






def get_emotion(string_serie):
    global transl
    global emotion
    serie_arr = string_serie.split(",")
    symbol = ""
    for word in serie_arr:
        if(not transl.has_word(word)): 
            continue
        symbol = transl.get_symbol(word)
        emotion.sum_symbol(symbol)
    emotion.update()
    return emotion.get_emotion()

def main():
    def pipe_function(request):
        print("recibe mensaje")
        print(request)
        return {"data":"funciona"}
    Btpy.ServerFlask.set_callback_post(
        pipe_function)
    Btpy.ServerFlask.set_port(5001)
    Btpy.ServerFlask.start()

main()