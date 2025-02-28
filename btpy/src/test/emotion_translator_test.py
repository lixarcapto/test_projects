

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


from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Habilita CORS para todas las rutas

transl = EmotionTranslator()
transl.load_data_base_symbol(
        "../btpy/res/symbol_emotion.xlsx")
emotion = EmotionSim()

def get_emotion(word):
    global transl
    global emotion
    if(transl.has_word(word)):
            symbol = transl.get_symbol(
                word)
            emotion.sum_symbol(symbol)
    emotion.update()
    return emotion.get_emotion()

@app.route('/', methods=['POST'])
def recibir_json():
    # Obtener los datos JSON del 
    # cuerpo de la solicitud
    data = request.get_json()
    # Procesar los datos recibidos
    # Por ejemplo, puedes imprimir 
    # los datos o realizar alguna 
    # operación con ellos
    # Crear la respuesta JSON
    respuesta = {
        'mensaje': 'Datos recibidos correctamente',
        'data': get_emotion(data["data"])
    }
    # Enviar la respuesta JSON
    return jsonify(respuesta)

def main():
    app.run(debug=True)

main()